from save_game import *
from bag import *
from pika import *
from resources import *
from main import *
from trainer_movement import *


def access_house (pokemon_trainer, pikachu_trainer, inside,x ,y, isAsh, isMisty) :

	VEL = 8
	pause = -1
	free_pika = 0
	trainer_pokeballs = []
	isTalking = False

	if isAsh :
		TRAINER_IMG = ASH_IMG
	else :
		TRAINER_IMG = MISTY_IMG

	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
	MOM = MOM_IMG

	pokemon_trainer.x = 700
	pokemon_trainer.y = 200

	while inside :

		pause = 0

		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			keys = pygame.key.get_pressed()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_p and len(trainer_pokeballs) < MAX_POKEBALL:
					free_pika = pokeball_out(trainer_pokeballs, free_pika)
					PIKACHU_SOUND.play()
				
			if keys[pygame.K_LEFT]:
				if isAsh :
					TRAINER_IMG = ASH_LEFT_IMG
				else :
					TRAINER_IMG = MISTY_LEFT_IMG

				MOM = MOM_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL, free_pika, pause, MOM, isTalking )
				
			if keys[pygame.K_RIGHT] :
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				MOM = MOM_LEFT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL, free_pika, pause, MOM, isTalking )

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				MOM = MOM_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL, free_pika, pause, MOM, isTalking)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				MOM = MOM_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL, free_pika, pause, MOM, isTalking )

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
				pause_menu(cursor_pause, pause)

			if pokemon_trainer.colliderect(TRAINER_HOUSE_DOOR):
				SCAPE_SOUND.play()
				HOUSE_SOUND.stop()
				inside = False
				pokemon_trainer.x = x
				pokemon_trainer.y = y

			if pokemon_trainer.colliderect(mom):
				isTalking = True
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y + VEL

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1

		HOUSE_SOUND.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement_house_trainer(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking)
		create_room(TRAINER_IMG,ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM, isTalking)


def create_room (TRAINER, PIKACHU, VEL, free_pika, pause, MOM, isTalking) :

	now = datetime.now()
	hora_str = now.strftime("%H")

	if int(hora_str) >= 10 and int(hora_str) < 20 : 
		WIN.blit(TRAINER_ROOM_IMG, (0,0))

	else :
		WIN.blit(TRAINER_ROOM_NIGHT, (0,0))

	WIN.blit(MOM, (previous_mom_x, previous_mom_y))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	#pygame.draw.rect(WIN, GREEN, TRAINER_HOUSE_DOOR) # House door
	#pygame.draw.rect(WIN, WHITE, TRAINER_HOUSE_WALL) # House wall
	#pygame.draw.rect(WIN, BLACK, TRAINER_HOUSE_LIMIT_1) # House limit
	#pygame.draw.rect(WIN, BLACK, TRAINER_HOUSE_LIMIT_2) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_BED) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_ESTANTERIA) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_TV) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_BOOKS) # House limit
	#pygame.draw.rect(WIN, GREEN, TRAINER_HOUSE_CONSOLE) # House limit
	#pygame.draw.rect(WIN, GREEN, mom) # House limit

	WIN.blit(SHOES_BG_IMG, (0,377))
	vel_counter = POKEBALLS_COUNTER.render(str(VEL), 1, GREY)
	WIN.blit(vel_counter, (57, 392))
	
	if pause == 0 :
		WIN.blit(BACK_BG_IMG, (0,0))
		WIN.blit(BAG_IMG, (5,15))

	if free_pika % 2 == 0 :
		WIN.blit(PIKA_BG_IMG, (770,377))

	if isTalking :

		if variables["TRAINER"]["INITIAL_POKEMON"] == "NONE"  :
				WIN.blit(DIALOG_MENU, (0, 300))
				mom_phrase = POKEBALLS_COUNTER.render("" + str("Did you introduce yourself to Prof. Oak?"), 1, WHITE)
				WIN.blit(mom_phrase, (180, 400))
				clock.tick(5)

		else :

			WIN.blit(DIALOG_MENU, (0, 300))
			mom_phrase = POKEBALLS_COUNTER_2.render("Oh! What an adorable Pokémon! You got it from the professor?", 1, WHITE)
			WIN.blit(mom_phrase, (35, 400))
			clock.tick(5)


	pygame.display.update()

def trainer_movement_house_trainer (keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking)
			fps +=1

def movement_left_house_trainer (pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking) :

	if isAsh :
		create_room(ASH_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_IMG, isTalking) # All Foots
		create_room(ASH_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(ASH_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_RIGHT_FOOT_IMG, isTalking ) # Right foot

	else :
		create_room(MISTY_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_IMG, isTalking) # All Foots
		create_room(MISTY_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(MISTY_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_RIGHT_FOOT_IMG , isTalking) # Right foot

	pokemon_trainer.x -= VEL
	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BED):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_ESTANTERIA):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(mom):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(OAK_RECTANGLE_MAP):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

			
	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

def movement_right_house_trainer (pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking) :

	if isAsh :
		create_room(ASH_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_IMG, isTalking ) # All Foots
		create_room(ASH_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, VEL, free_pika, pause , MOM_LEFT_LEFT_FOOT_IMG, isTalking) # Left foot
		create_room(ASH_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_RIGHT_FOOT_IMG, isTalking ) # Right foot

	else :
		create_room(MISTY_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_IMG, isTalking ) # All Foots
		create_room(MISTY_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(MISTY_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_RIGHT_FOOT_IMG, isTalking ) # Right foot

	pokemon_trainer.x += VEL
	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(mom):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y


	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 10
		pokemon_trainer.y = previous_y

def movement_up_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking) :

	pokemon_trainer.y -= VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(TRAINER_HOUSE_WALL):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_ESTANTERIA):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(mom):
		pokemon_trainer.y = previous_y + VEL
		isTalking = True

	if isAsh :

		create_room(ASH_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_IMG, isTalking ) # All Foots
		create_room(ASH_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(ASH_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_FOOT_IMG, isTalking) # Right foot

	else :
		create_room(MISTY_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_IMG, isTalking ) # All Foots
		create_room(MISTY_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(MISTY_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_RIGHT_FOOT_IMG, isTalking ) # Right foot


def movement_down_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL, free_pika, pause, isTalking) :

	if isAsh :
		create_room(ASH_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_BACK_IMG, isTalking) # All Foots
		create_room(ASH_LEFT_FOOT_IMG,  ASH_PIKACHU_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_BACK_LEFT_FOOT_IMG, isTalking ) # Left foot
		create_room(ASH_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_BACK_RIGHT_FOOT_IMG, isTalking ) # Right foot

	else :
		create_room(MISTY_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, VEL, free_pika, pause, MOM_BACK_IMG, isTalking ) # All Foots
		create_room(MISTY_LEFT_FOOT_IMG,  ASH_PIKACHU_RIGHT_FOOT_IMG, VEL , free_pika, pause, MOM_BACK_LEFT_FOOT_IMG, isTalking) # Left foot
		create_room(MISTY_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, VEL, free_pika, pause, MOM_BACK_RIGHT_FOOT_IMG, isTalking ) # Right foot

	pokemon_trainer.y += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL

	if pokemon_trainer.colliderect(mom):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BED):
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL

