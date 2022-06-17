from save_game import *
from bag import *
from pika import *
from resources import *
from main import *
from trainer_movement import *


def access_laboratory (pokemon_trainer, pikachu_trainer, inside, x, y, isAsh, isMisty, free_pika) :

	isTalking = False
	isBulbasaur = False
	isSquirtle = False
	isCharmander = False
	pause = -1
	trainer_pokeballs = []
	VEL = 3

	if isAsh :
		TRAINER_IMG = ASH_BACK_IMG

	else :
		TRAINER_IMG = MISTY_IMG

	OAK = OAK_RIGHT_IMG
	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	pokemon_trainer.x = 400
	pokemon_trainer.y = 360

	while inside :
		pause = 0

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
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)
				
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				OAK = OAK_LEFT_IMG
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				OAK = OAK_IMG
				create_laboratory( TRAINER_IMG, PIKACHU_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				OAK = OAK_BACK_IMG
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				my_save_slot = json.dumps(variables["TRAINER"])
				pokemon_1_level = variables["TRAINER"]["POKEMON_1"]["LEVEL"] = 55
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
				welcome()

			if keys[pygame.K_x]:
				pause +=1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG

				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )
				pause_menu(cursor_pause, pause)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1



			if pokemon_trainer.colliderect(OAK_DOOR):
				inside = False
				OAK_THEME.stop()
				pokemon_trainer.x = x
				pokemon_trainer.y = y
			


		OAK_THEME.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement_house(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
		create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)


def create_laboratory (TRAINER, PIKACHU, OAK, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) :

	WIN.blit(OAK_LABORATORY_IMG, (0,0))

	WIN.blit(OAK, (previous_oak_x, previous_oak_y))

	WIN.blit(OAK_LABORATORY_DOOR, (400, 480))


	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	if variables["TRAINER"]["INITIAL_POKEMON"] == "Bulbasaur" :
		WIN.blit(POKEBALL_ITEM, (640, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))

	elif variables["TRAINER"]["INITIAL_POKEMON"] == "Charmander" :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))

	elif variables["TRAINER"]["INITIAL_POKEMON"] == "Squirtle" :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (640, 300))

	else :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (640, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))


	
	#pygame.draw.rect(WIN, GREEN, OAK_TABLE) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_1) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_2) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_3)

	if isTalking :

		if variables["TRAINER"]["INITIAL_POKEMON"] == "NONE"  :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("" + str("Now, " + variables["TRAINER"]["NAME"].capitalize() + ", which Pokémon do you want?"), 1, WHITE)
			WIN.blit(oak_phrase, (180, 400))
			clock.tick(5)

		else :

			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("Take care of your " + variables["TRAINER"]["INITIAL_POKEMON"] + ", " + variables["TRAINER"]["NAME"].capitalize(), 1, WHITE)
			WIN.blit(oak_phrase, (180, 400))
			clock.tick(5)



	if variables["TRAINER"]["INITIAL_POKEMON"] == "NONE"  :

		if isSquirtle :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Squirtle, a water type Pokémon" , 1, WHITE)
			WIN.blit(oak_phrase, (55, 400))
			clock.tick(20)

		if isBulbasaur :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Bulbasaur, a grash type Pokémon", 1, WHITE)
			WIN.blit(oak_phrase, (50, 400))
			clock.tick(20)

		if isCharmander :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Charmander, a fire type Pokémon", 1, WHITE)
			WIN.blit(oak_phrase, (50, 400))
			clock.tick(20)

	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

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


	#pygame.draw.rect(WIN, GREEN, OAK_RECTANGLE) # Oak rectangle

	pygame.display.update()


def trainer_movement_house (keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1


def movement_left_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isCharmander = False
	isBulbasaur = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.x += 1
		
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.type == pygame.K_SPACE:
					isTalking = False

	else :
		pokemon_trainer.x -= VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10

	if pokemon_trainer.colliderect(OAK_POKEBALL_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10

	if isAsh :

		create_laboratory( ASH_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( ASH_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( ASH_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory( MISTY_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( MISTY_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( MISTY_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

def movement_right_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isBulbasaur = False
	isCharmander = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.x -= 1
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.type == pygame.K_SPACE:
					isTalking = False

	else :
		pokemon_trainer.x += VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 10

	if pokemon_trainer.colliderect(OAK_POKEBALL_3):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 10

	if isAsh :

		create_laboratory( ASH_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG,  OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( ASH_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory( MISTY_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( MISTY_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( MISTY_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking , isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot


def movement_up_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isBulbasaur = False
	isCharmander = False
	isSquirtle = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.y -= 1
		isTalking = True

	else :

		pokemon_trainer.y -= VEL
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

	if pokemon_trainer.colliderect(OAK_TABLE):
		start_pokeball_starter_view(cursor_pos)
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 20

	if pokemon_trainer.colliderect(OAK_POKEBALL_1):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if pokemon_trainer.colliderect(OAK_POKEBALL_2):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if pokemon_trainer.colliderect(OAK_POKEBALL_3):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if isAsh :

		create_laboratory( ASH_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( ASH_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Right foot

	else :
		create_laboratory( MISTY_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( MISTY_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking , isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( MISTY_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Right foot


def movement_down_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isCharmander = False
	isBulbasaur = False

	if isAsh :
		create_laboratory ( ASH_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( ASH_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory ( MISTY_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( MISTY_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( MISTY_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot


	pokemon_trainer.y += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	pikachu_trainer.y = pokemon_trainer.y - 70
	pikachu_trainer.x = pokemon_trainer.x + 5
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10

def start_pokeball_starter_view (cursor_pos) :
	choosing = True
	cursor_pos.x = 100
	cursor_pos.y = 50
	isBulbasaur = True
	isCharmander = False
	isSquirtle = False
	isSelected = False

	while variables["TRAINER"]["INITIAL_POKEMON"] == "NONE" :
		create_pokeball_starter_view(cursor_pos.x, cursor_pos.y, isSquirtle, isBulbasaur, isCharmander, isSelected)

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_b :
					choosing = False

				if isSelected :
					if isSquirtle :
						variables["TRAINER"]["INITIAL_POKEMON"] = "Squirtle"
						# Generate initial Pokemon Stats
						variables["TRAINER"]["POKEMON_2"]["NAME"] = "SQUIRTLE"
						variables["TRAINER"]["POKEMON_2"]["LEVEL"] = 5
						variables["TRAINER"]["POKEMON_2"]["HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["BASE_HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["MOVE"] = "Tail Whip"
						variables["TRAINER"]["POKEMON_2"]["ATTACK"] = 13
						variables["TRAINER"]["POKEMON_2"]["DEFENSE"] = 15
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_ATTACK"] = 11
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_DEFENSE"] = 14
						variables["TRAINER"]["POKEMON_2"]["SPEED"] = 11
						save_game()

					if isBulbasaur :
						variables["TRAINER"]["INITIAL_POKEMON"] = "Bulbasaur"
						# Generate initial Pokemon Stats
						variables["TRAINER"]["POKEMON_2"]["NAME"] = "BULBASAUR"
						variables["TRAINER"]["POKEMON_2"]["LEVEL"] = 5
						variables["TRAINER"]["POKEMON_2"]["HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["BASE_HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["MOVE"] = "Tackle"
						variables["TRAINER"]["POKEMON_2"]["ATTACK"] = 13
						variables["TRAINER"]["POKEMON_2"]["DEFENSE"] = 11
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_ATTACK"] = 13
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_DEFENSE"] = 13
						variables["TRAINER"]["POKEMON_2"]["SPEED"] = 13
						save_game()

					if isCharmander :
						variables["TRAINER"]["INITIAL_POKEMON"] = "Charmander"
						# Generate initial Pokemon Stats
						variables["TRAINER"]["POKEMON_2"]["NAME"] = "CHARMANDER"
						variables["TRAINER"]["POKEMON_2"]["LEVEL"] = 5
						variables["TRAINER"]["POKEMON_2"]["HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["BASE_HP"] = 20
						variables["TRAINER"]["POKEMON_2"]["MOVE"] = "Scratch"
						variables["TRAINER"]["POKEMON_2"]["ATTACK"] = 13
						variables["TRAINER"]["POKEMON_2"]["DEFENSE"] = 11
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_ATTACK"] = 13
						variables["TRAINER"]["POKEMON_2"]["SPECIAL_DEFENSE"] = 11
						variables["TRAINER"]["POKEMON_2"]["SPEED"] = 15
						save_game()

				if cursor_pos.x == 100 and event.key == pygame.K_RIGHT :
					isBulbasaur = False
					isCharmander = True
					isSquirtle = False	

				if isCharmander and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 400 and event.key == pygame.K_LEFT :
					isCharmander = False
					isSquirtle = False
					isBulbasaur = True

				if isBulbasaur and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 400 and  event.key == pygame.K_RIGHT :
					isSquirtle = True
					isBulbasaur = False
					isCharmander = False

				if isSquirtle and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 700 and  event.key == pygame.K_LEFT :
					isSquirtle = False
					isBulbasaur = False
					isCharmander = True

				if cursor_pos.x < 700 and event.key == pygame.K_RIGHT :
					cursor_pos.x += 300

				if cursor_pos.x > 100 and event.key == pygame.K_LEFT :
					cursor_pos.x -= 300


def create_pokeball_starter_view (x, y, isSquirtle, isBulbasaur, isCharmander, isSelected) :
	WIN.blit(POKEBALL_CHOOSE, (0,0))
	WIN.blit(CURSOR, (x, y))


	if isSquirtle :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Squirtle, a water type Pokémon" , 1, WHITE)
		WIN.blit(oak_phrase, (55, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)


	if isBulbasaur :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Bulbasaur, a grash type Pokémon", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)

	if isCharmander :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Charmander, a fire type Pokémon", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)

	if isSelected :
		choosed = ""

		if isSquirtle :
			choosed = "Squirtle"
		elif isBulbasaur :
			choosed = "Bulbasaur"
		else :
			choosed = "Charmander"

		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("I choose you, %s" % choosed + "!", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press any key to exit", 1, WHITE)
		WIN.blit(oak_phrase_2, (50, 450))
		clock.tick(20)
		save_game()


	pygame.display.update()