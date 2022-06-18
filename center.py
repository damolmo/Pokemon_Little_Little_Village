from resources import *
from bag import *
from save_game import *
from pika import *
from bank import *

def access_center (pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty) :
	trainer_pokeballs = []
	oakMessage = False
	pause = -1
	free_pika = 0
	VEL = 3

	if isAsh :
		TRAINER_IMG = ASH_BACK_IMG
	else :
		TRAINER_IMG = MISTY_BACK_IMG

	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	pokemon_trainer.x = 420
	pokemon_trainer.y = 370
	BACKGROUND_SOUND.stop()

	while inside :
		pause = 0
		create_center(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_p and len(trainer_pokeballs) < MAX_POKEBALL:
					free_pika = pokeball_out(trainer_pokeballs, free_pika)
					PIKACHU_SOUND.play()

			keys = pygame.key.get_pressed()
				
			if keys[pygame.K_LEFT]:

				if isAsh :
					TRAINER_IMG = ASH_LEFT_IMG
				else :
					TRAINER_IMG = MISTY_LEFT_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				OAK = OAK_RIGHT_IMG
				create_center(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				OAK = OAK_LEFT_IMG
				create_center(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				OAK = OAK_IMG
				create_center(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				OAK = OAK_BACK_IMG
				create_center(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				save_game()
				welcome()

			if pokemon_trainer.colliderect(CENTER_DOOR):
				CENTER_SOUND.stop()
				pokemon_trainer.x = 230
				pokemon_trainer.y = 330
				
				inside = False
				
				
			if keys[pygame.K_x]:
				pause += 1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG

				create_center(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				pause_menu(cursor_pause, pause)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1

		keys_pressed = pygame.key.get_pressed()
		trainer_movement_center(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)

		CENTER_SOUND.play()

def create_center (pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL)  :
	
	WIN.blit(CENTER_INSIDE_IMG, (0, 0)) # Background layout
	WIN.blit(JOY_IMG, (420, 115 ))
	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	fecha = today.strftime("%m %d")

	date = DIALOG_FONT.render("" + str(fecha), 1, BLACK)
	daysOfTheWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

	now = datetime.now()
	day = now.weekday()
	tuday = daysOfTheWeek[day]
	hora_str = now.strftime("%H:%M")

	dayofWeek = DIALOG_MINI_FONT.render("" + str(tuday), 1, BLACK)

	time = POKEBALLS_COUNTER.render("" + str(hora_str), 1, WHITE)

	if pause == 0 :
		WIN.blit(BACK_BG_IMG, (0,0))
		WIN.blit(BAG_IMG, (5,15))

	if free_pika % 2 == 0 :
		WIN.blit(PIKA_BG_IMG, (770,377))

	WIN.blit(SHOES_BG_IMG, (0,377))
	vel_counter = POKEBALLS_COUNTER.render(str(VEL), 1, GREY)
	WIN.blit(vel_counter, (57, 392))

	WIN.blit(CLOCK_IMG, (700, 0))
	WIN.blit(date, (725, 10))
	WIN.blit(dayofWeek, (830, 20))
	WIN.blit(time, (750, 50))

	#pygame.draw.rect(WIN, BLUE, JOY_RECT)
	#pygame.draw.rect(WIN, BLUE, CENTER_DOOR)
	#pygame.draw.rect(WIN, BLUE, CENTER_DESK)
	#pygame.draw.rect(WIN, BLUE, CENTER_PLANTS)
	#pygame.draw.rect(WIN, BLUE, CENTER_STAIRS_RIGHT)
	#pygame.draw.rect(WIN, BLUE, CENTER_STAIRS_EAST)
	#pygame.draw.rect(WIN, BLUE, CENTER_STAIRS_WEST)
	#pygame.draw.rect(WIN, BLUE, LIMIT_EAST)
	#pygame.draw.rect(WIN, BLUE, LIMIT_WEST)
	#pygame.draw.rect(WIN, BLUE, BANK_RECT)



	pygame.display.update()




def health_pokemon() :

	# Health the HP of all the trainer Pokemon

	# Slot 1
	variables["TRAINER"]["POKEMON_1"]["HP"] = variables["TRAINER"]["POKEMON_1"]["BASE_HP"]

	# Slot 2
	variables["TRAINER"]["POKEMON_2"]["HP"] = variables["TRAINER"]["POKEMON_2"]["BASE_HP"]

	# Slot 3
	variables["TRAINER"]["POKEMON_3"]["HP"] = variables["TRAINER"]["POKEMON_3"]["BASE_HP"]
	

def create_joy_animation (pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL, JOY, isHealthTime) :

	WIN.blit(CENTER_INSIDE_IMG, (0, 0)) # Background layout
	WIN.blit(JOY, (420, 115 ))
	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	# Trainer Available pokeballs

	pokeball = pygame.transform.scale(POKEBALL_ITEM, (20,20))

	if isHealthTime == 1 :

		if variables["TRAINER"]["POKEMON_1"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (380, 130))

	if isHealthTime == 2 :

		if variables["TRAINER"]["POKEMON_1"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (380, 130))

		if variables["TRAINER"]["POKEMON_2"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (400, 130))

	if isHealthTime == 3 :
		if variables["TRAINER"]["POKEMON_1"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (380, 130))

		if variables["TRAINER"]["POKEMON_2"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (400, 130))

		if variables["TRAINER"]["POKEMON_3"]["NAME"] != "NONE" :
			WIN.blit(pokeball, (400, 150))

	fecha = today.strftime("%m %d")

	date = DIALOG_FONT.render("" + str(fecha), 1, BLACK)
	daysOfTheWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

	now = datetime.now()
	day = now.weekday()
	tuday = daysOfTheWeek[day]
	hora_str = now.strftime("%H:%M")

	dayofWeek = DIALOG_MINI_FONT.render("" + str(tuday), 1, BLACK)

	time = POKEBALLS_COUNTER.render("" + str(hora_str), 1, WHITE)

	if pause == 0 :
		WIN.blit(BACK_BG_IMG, (0,0))
		WIN.blit(BAG_IMG, (5,15))

	if free_pika % 2 == 0 :
		WIN.blit(PIKA_BG_IMG, (770,377))

	WIN.blit(SHOES_BG_IMG, (0,377))
	vel_counter = POKEBALLS_COUNTER.render(str(VEL), 1, GREY)
	WIN.blit(vel_counter, (57, 392))

	WIN.blit(CLOCK_IMG, (700, 0))
	WIN.blit(date, (725, 10))
	WIN.blit(dayofWeek, (830, 20))
	WIN.blit(time, (750, 50))
	pygame.display.update()



def trainer_movement_center(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

def movement_left_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y


	if not wild :
		if isAsh :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.x -= VEL
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(CENTER_STAIRS_EAST):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(CENTER_DESK):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(LIMIT_EAST):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

def movement_right_center (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False

	if not wild :
		if isAsh :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 10
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(CENTER_DESK):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y 

		if pokemon_trainer.colliderect(CENTER_PLANTS):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y 

		if pokemon_trainer.colliderect(CENTER_STAIRS_RIGHT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y 

		if pokemon_trainer.colliderect(LIMIT_WEST):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y 

def movement_up_center (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	
	if not wild: 
		if isAsh :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.y -= VEL
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(CENTER_DESK):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(BANK_RECT):
			access_bank()
			

		if pokemon_trainer.colliderect(JOY_RECT):
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			isHealthTime = 0

			CENTER_SOUND.stop()
			if isAsh : 
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL,JOY_IMG, isHealthTime)
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_UP_IMG, isHealthTime)
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 1
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 2
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 3
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				HEALING_SOUND.play()
				health_pokemon()
				time.sleep(3)
				pokemon_trainer.y = previous_y + 50

			else :
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL,JOY_IMG, isHealthTime )
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_UP_IMG, isHealthTime)
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 1
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 2
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				isHealthTime = 3
				time.sleep(1)
				create_joy_animation(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, JOY_LEFT_IMG, isHealthTime)
				HEALING_SOUND.play()
				health_pokemon()
				time.sleep(3)
				pokemon_trainer.y = previous_y + 50


		if pokemon_trainer.colliderect(CENTER_STAIRS_EAST):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(CENTER_STAIRS_WEST):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(CENTER_STAIRS_RIGHT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x


def movement_down_center(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()
	isTree = False
	oakMessage = False

	if not wild :

		if isAsh :

			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL ) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_center(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.y += VEL
		pikachu_trainer.y = pokemon_trainer.y - 60
		pikachu_trainer.x = pokemon_trainer.x + 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(CENTER_PLANTS):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL
			pikachu_trainer.y = pokemon_trainer.y - 60
			pikachu_trainer.x = pokemon_trainer.x + 5
