from shopping import *
from bag import *
from save_game import *
from pika import *

counter_potions = 1
counter_revives = 1
counter_pokeballs = 1

def create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL)  :
	WIN.blit(SHOP_INSIDE_IMG, (0, 0))

	WIN.blit(DEPENDENT_IMG, (100, 150))

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


	#pygame.draw.rect(WIN, BLUE, MACETA_SURESTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MACETA_SUROESTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MACETA_NORTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MOSTRADOR_RECT)
	#pygame.draw.rect(WIN, BLUE, PUERTA_RECT)
	#pygame.draw.rect(WIN, BLUE, MESA_RECT)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_1)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_2)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_3)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_1)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_2)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_3)
	#pygame.draw.rect(WIN, BLACK, SHOP_DEPENDENT_RECT)


	pygame.display.update()



def trainer_movement_shop(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1




def movement_left_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False


	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y


	if not wild :
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.x -= VEL
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(MOSTRADOR_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(MESA_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(MACETA_SURESTE_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_2):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

		if pokemon_trainer.colliderect(SHOP_DEPENDENT_RECT):
			choosing = True
			cursor_pos.x = 715
			cursor_pos.y = 10
			counter_potions = 1
			counter_revives = 1
			counter_pokeballs = 1

			while (choosing) :
				if isAsh :
					choose_items(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, counter_pokeballs, counter_revives, counter_potions)
				else :
					choose_items(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL, counter_pokeballs, counter_revives, counter_potions)

				for event in pygame.event.get() : 

					if event.type == pygame.KEYDOWN :

						if event.key == pygame.K_UP and cursor_pos.x == 800 and cursor_pos.y == 50 :
							PRESS_A_SOUND.play()
							

						if event.key == pygame.K_DOWN and cursor_pos.x == 800 and cursor_pos.y == 50 :
							PRESS_A_SOUND.play()

						if event.key == pygame.K_UP and cursor_pos.y > 10  :
							cursor_pos.y-=70 

						if event.key == pygame.K_DOWN and cursor_pos.y < 360  :
							cursor_pos.y+=70

						if cursor_pos.y == 10 and event.key == pygame.K_a  :
							counter_pokeballs +=1

						if cursor_pos.y == 80 and event.key == pygame.K_a  :
							if counter_pokeballs > 0 :
								counter_pokeballs -=1

						if cursor_pos.y == 150 and event.key == pygame.K_a  :
							counter_potions +=1

						if cursor_pos.y == 220 and event.key == pygame.K_a  :
							if counter_potions > 0 :
								counter_potions -=1

						if cursor_pos.y == 290 and event.key == pygame.K_a  :
							counter_revives +=1

						if cursor_pos.y == 360 and event.key == pygame.K_a  :
							if counter_revives > 0 :
								counter_revives -=1

						if event.key == pygame.K_b :
							choosing = False

						if event.key == pygame.K_SPACE :
							buy_items (counter_revives, counter_potions, counter_pokeballs)
							choosing = False


def buy_items (counter_revives, counter_potions, counter_pokeballs) :

	available_pokeballs = variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_AVAILABLE"]
	available_potions = variables["TRAINER"]["TRAINER_BAG"]["POTIONS_AVAILABLE"]
	available_revives = variables["TRAINER"]["TRAINER_BAG"]["REVIVES_AVAILABLE"]

	max_pokeballs = variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_MAX"]
	max_potions = variables["TRAINER"]["TRAINER_BAG"]["POTIONS_MAX"]
	max_revives = variables["TRAINER"]["TRAINER_BAG"]["REVIVES_MAX"]

	pokeball_price = 200
	revives_price = 500
	potions_price = 350

	pokeballs_buying_price = counter_pokeballs * pokeball_price
	potions_buying_price = counter_potions * potions_price
	revives_buying_price = counter_revives * revives_price

	total_buying = pokeballs_buying_price + potions_buying_price + revives_buying_price

	trainer_money = variables["TRAINER"]["POKECOINS"]

	# Buy Pokeballs

	if total_buying <= trainer_money :
		variables["TRAINER"]["POKECOINS"] -= total_buying

		if counter_pokeballs > 0:
			if counter_pokeballs + available_pokeballs <= max_pokeballs :
				variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_AVAILABLE"] = available_pokeballs + counter_pokeballs

		if counter_potions > 0:
			if counter_potions + available_potions <= max_potions :
				variables["TRAINER"]["TRAINER_BAG"]["POTIONS_AVAILABLE"] = available_potions + counter_potions

		if counter_revives > 0:
			if counter_revives + available_revives <= max_revives :
				variables["TRAINER"]["TRAINER_BAG"]["REVIVES_AVAILABLE"] = available_revives + counter_revives

			

def movement_right_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False

	if not wild :
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(MESA_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(MACETA_SUROESTE_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(MACETA_NORTE_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

def movement_up_shop (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	
	if not wild: 
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.y -= VEL
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(MESA_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_1):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_2):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_3):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(MOSTRADOR_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

def movement_down_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()
	isTree = False
	oakMessage = False

	if not wild :

		if isAsh :

			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL ) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.y += VEL
		pikachu_trainer.y = pokemon_trainer.y - 60
		pikachu_trainer.x = pokemon_trainer.x + 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL


		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL

		if pokemon_trainer.colliderect(MESA_RECT):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL



def access_shop (pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty) :
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

	pokemon_trainer.x = 200
	pokemon_trainer.y = 330
	BACKGROUND_SOUND.stop()

	while inside :
		pause = 0
		create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

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
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				OAK = OAK_LEFT_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				OAK = OAK_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				OAK = OAK_BACK_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				save_game()
				welcome()

			if pokemon_trainer.colliderect(PUERTA_RECT):
				SHOP_SOUND.stop()
				inside = False
				

			if keys[pygame.K_x]:
				pause += 1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG

				create_shop(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
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
		trainer_movement_shop(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)

		SHOP_SOUND.play()


def choose_items (pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL, counter_pokeballs, counter_revives, counter_potions) :

	WIN.blit(SHOP_ITEMS_IMG, (0,0))
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))

	pokeballs = WINNER_LOOSER_DIALOG.render("" + str(counter_pokeballs), 1, WHITE)
	WIN.blit(pokeballs, (580, 50))

	pokeballs_price = SHOP_FONT.render("200¥", 1, WHITE)
	WIN.blit(pokeballs_price, (410, 50))

	potions = WINNER_LOOSER_DIALOG.render("" + str(counter_potions), 1, WHITE)
	WIN.blit(potions, (580, 200))

	potions_price = SHOP_FONT.render("350¥", 1, WHITE)
	WIN.blit(potions_price, (410, 200))

	revives = WINNER_LOOSER_DIALOG.render("" + str(counter_revives), 1, WHITE)
	WIN.blit(revives, (580, 350))

	revives_price = SHOP_FONT.render("500¥", 1, WHITE)
	WIN.blit(revives_price, (410, 370))



	pygame.display.update()