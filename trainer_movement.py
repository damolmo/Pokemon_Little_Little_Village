from home import *
from battle import *


def create_map(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL) :

	now = datetime.now()
	hora = now.strftime("%H")


	if hora <="16" and hora >="10" :
		WIN.blit(ROUTE_IMG, (0,0)) # Place background image

	elif hora >="17" and hora <"20":
		WIN.blit(ROUTE_IMG_2, (0,0)) # Place background image

	elif hora >= "00" and hora <"06" :
		WIN.blit(ROUTE_IMG_4, (0,0))

	elif hora >= "06" and hora <"10" :
		WIN.blit(ROUTE_IMG_5, (0,0))

	else :
		WIN.blit(ROUTE_IMG_3, (0,0)) # Place background image

	

	#pygame.draw.rect(WIN, BLUE, HOUSE_1) # House 1 building
	#WIN.blit(LAB, (HOUSE_1.x  - 100, HOUSE_1.y + 30 ))
	#pygame.draw.rect(WIN, BLUE, HOUSE_1_DOOR) # House 1 Door

	#pygame.draw.rect(WIN, BLUE, HOUSE_2) # House 2 building
	#pygame.draw.rect(WIN, BLUE, HOUSE_2_DOOR) # House 2 Door

	#pygame.draw.rect(WIN, GREEN, TREE_1) # Tree 1 building
	#pygame.draw.rect(WIN, GREEN, TREE_2) # Tree 2 building

	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH) # Grass zone south
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH_2) # Grass zone south 2
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_WEST) # Grass zone west
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_EAST) # Grass zone west

	pokeball = POKEBALL_ITEM.get_rect()
	pokeball = pygame.Rect(
		pokemon_trainer.x, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 10, 5)


	for pokeball in trainer_pokeballs :
		WIN.blit(POKEBALL_ITEM, (pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 1, 1))

	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

	if variables["TRAINER"]["INITIAL_POKEMON"] =="NONE":
		WIN.blit(OAK_IMG, (395, -10))

		if oakMessage :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("Hey! Don't go away yet!", 1, WHITE)
			WIN.blit(oak_phrase, (280, 400))
			clock.tick(2)

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

	#pygame.draw.rect(WIN, GREEN, OAK_RECTANGLE_MAP)

	pygame.display.update()




def trainer_movement (keys_pressed, pokemon_trainer, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_b] :
		if isAsh :
			TRAINER_IMG = ASH_BICICLE_IMG
		else :
			TRAINER_IMG = MISTY_BICICLE_IMG


	if keys_pressed[pygame.K_a]  and pokemon_trainer.x >0:
		if isAsh :
			TRAINER_IMG = ASH_BICICLE_IMG
		else :
			TRAINER_IMG = MISTY_BICICLE_IMG

		fps = 0
		while fps < 5 :
			bicicle_movement_left(pokemon_trainer,pikachu_trainer, isAsh, isMisty, pause, VEL)
			fps +=1
				
	if keys_pressed[pygame.K_d] and pokemon_trainer.x < WIDTH - 80  :
		if isAsh :
			TRAINER_IMG = ASH_BICICLE_RIGHT_IMG
		else :
			TRAINER_IMG = MISTY_BICICLE_RIGHT_IMG

		fps = 0
		while fps < 5 :
			bicicle_movement_right(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_w]  and pokemon_trainer.y - VEL > 0:
		if isAsh :
			TRAINER_IMG = ASH_BICICLE_BACK_IMG
		else :
			TRAINER_IMG = MISTY_BICICLE_BACK_IMG

		fps = 0
		while fps < 5 :
			bicicle_movement_up(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_s] and pokemon_trainer.y - VEL < HEIGHT -100:
		if isAsh :
			TRAINER_IMG = ASH_BICICLE_IMG
		else :
			TRAINER_IMG = MISTY_BICICLE_IMG

		fps = 0
		while fps < 5 :
			bicicle_movement_down(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL)
			fps +=1

def movement_left (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y

	if variables["TRAINER"]["INITIAL_POKEMON"] =="NONE"  :

		if pokemon_trainer.colliderect(OAK_RECTANGLE_MAP):
			oakMessage = True
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + 10
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + 10
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)



	if not wild :
		if isAsh :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot


		pokemon_trainer.x -= VEL
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(HOUSE_2):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)


		if pokemon_trainer.colliderect(TREE_2):
			WALL_SOUND.play()
			keys = pygame.key.get_pressed()
				
			if keys[pygame.K_z]:
				pokemon_trainer.x = previous_x + VEL
				pokemon_trainer.y = previous_y - 0
				pikachu_trainer.x = previous_pi_x + VEL
				pikachu_trainer.y = previous_pi_y - 0
				wild_encouter = randint(1, 300)

				if wild_encouter == 95 :
					previous_x = pokemon_trainer.x 
					previous_y = pokemon_trainer.y
					previous_pi_x = pikachu_trainer.x
					previous_pi_y = pikachu_trainer.y
					wild = True
					isTree = True
					start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

			else :
				pokemon_trainer.x = previous_x + VEL
				pokemon_trainer.y = previous_y - 0
				pikachu_trainer.x = previous_pi_x + VEL
				pikachu_trainer.y = previous_pi_y - 0

				pygame.draw.rect(WIN, WHITE, pokemon_trainer)
				pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST):
			wild = False

			wild_encouter = randint(1, 500) # Generate random number 1
			wild_encounter_2 = randint(1,500) # Generate random number 2
			lucky = wild_encouter + wild_encounter_2 # Total

			if lucky == 900 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				previous_pi_x = pikachu_trainer.x
				previous_pi_y = pikachu_trainer.y
				wild = True
				POKEMON_ENCOUNTER_SOUND.play()
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)


def movement_right (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False

	if not wild :
		if isAsh :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(HOUSE_1):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x - VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_1)

		if pokemon_trainer.colliderect(HOUSE_2):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x - VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if variables["TRAINER"]["INITIAL_POKEMON"] =="NONE"  :
			if pokemon_trainer.colliderect(OAK_RECTANGLE_MAP):
				WALL_SOUND.play()
				pokemon_trainer.x = previous_x - VEL
				pokemon_trainer.y = previous_y - 0
				pikachu_trainer.x = previous_pi_x - VEL
				pikachu_trainer.y = previous_pi_y - 0

				pygame.draw.rect(WIN, WHITE, pokemon_trainer)
				pygame.draw.rect(WIN, WHITE, HOUSE_2)


		if pokemon_trainer.colliderect(TREE_2):
				WALL_SOUND.play()
				keys = pygame.key.get_pressed()
				
				if keys[pygame.K_z]:
					pokemon_trainer.x = previous_x - VEL
					pokemon_trainer.y = previous_y - 0
					pikachu_trainer.x = previous_pi_x - VEL
					pikachu_trainer.y = previous_pi_y - 0
					wild_encouter = randint(1, 300)

					if wild_encouter == 95 :
						previous_x = pokemon_trainer.x 
						previous_y = pokemon_trainer.y
						previous_pi_x = pikachu_trainer.x
						previous_pi_y = pikachu_trainer.y
						wild = True
						isTree = True
						start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

				else :

					pokemon_trainer.x = previous_x - VEL
					pokemon_trainer.y = previous_y - 0
					pikachu_trainer.x = previous_pi_x - VEL
					pikachu_trainer.y = previous_pi_y - 0

					pygame.draw.rect(WIN, WHITE, pokemon_trainer)
					pygame.draw.rect(WIN, WHITE, TREE_2)


		if pokemon_trainer.colliderect(TREE_1):
				WALL_SOUND.play()
				keys = pygame.key.get_pressed()
				
				if keys[pygame.K_z]:
					pokemon_trainer.x = previous_x - VEL
					pokemon_trainer.y = previous_y - 0
					pikachu_trainer.x = previous_pi_x - VEL
					pikachu_trainer.y = previous_pi_y - 0
					wild_encouter = randint(1, 300)

					if wild_encouter == 95 :
						previous_x = pokemon_trainer.x 
						previous_y = pokemon_trainer.y
						previous_pi_x = pikachu_trainer.x
						previous_pi_y = pikachu_trainer.y
						wild = True
						isTree = True
						start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

				else :
					pokemon_trainer.x = previous_x - VEL
					pokemon_trainer.y = previous_y - 0
					pikachu_trainer.x = previous_pi_x - VEL
					pikachu_trainer.y = previous_pi_y - 0

					pygame.draw.rect(WIN, WHITE, pokemon_trainer)
					pygame.draw.rect(WIN, WHITE, TREE_1)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :

			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				previous_pi_x = pikachu_trainer.x
				previous_pi_y = pikachu_trainer.y
				wild = True
				POKEMON_ENCOUNTER_SOUND.play()
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)


def movement_up (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	if variables["TRAINER"]["INITIAL_POKEMON"] =="NONE":
		if pokemon_trainer.colliderect(OAK_RECTANGLE_MAP):
			oakMessage = True
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + 10
			pikachu_trainer.x = previous_pi_x - 0
			pikachu_trainer.y = previous_pi_y + 10

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_1)

	
	if not wild: 
		if isAsh :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.y -= VEL
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(HOUSE_1):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + VEL
			pikachu_trainer.x = previous_pi_x - 0
			pikachu_trainer.y = previous_pi_y + VEL

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_1)


		if pokemon_trainer.colliderect(HOUSE_2):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + VEL
			pikachu_trainer.x = previous_pi_x - 0
			pikachu_trainer.y = previous_pi_y + VEL

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(TREE_1):
				WALL_SOUND.play()
				keys = pygame.key.get_pressed()
				
				if keys[pygame.K_z]:
					pokemon_trainer.x = previous_x - 0
					pokemon_trainer.y = previous_y + VEL
					pikachu_trainer.x = previous_pi_x - 0
					pikachu_trainer.y = previous_pi_y + VEL
					wild_encouter = randint(1, 300)

					if wild_encouter == 95 :
						previous_x = pokemon_trainer.x 
						previous_y = pokemon_trainer.y
						previous_pi_x = pikachu_trainer.x
						previous_pi_y = pikachu_trainer.y
						wild = True
						isTree = True
						start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

				else :
					pokemon_trainer.x = previous_x - 0
					pokemon_trainer.y = previous_y + VEL
					pikachu_trainer.x = previous_pi_x - 0
					pikachu_trainer.y = previous_pi_y + VEL

					pygame.draw.rect(WIN, WHITE, pokemon_trainer)
					pygame.draw.rect(WIN, WHITE, TREE_1)
		

		if pokemon_trainer.colliderect(TREE_2):
				WALL_SOUND.play()
				keys = pygame.key.get_pressed()
				
				if keys[pygame.K_z]:
					pokemon_trainer.x = previous_x - 0
					pokemon_trainer.y = previous_y + VEL
					pikachu_trainer.x = previous_pi_x - 0
					pikachu_trainer.y = previous_pi_y + VEL
					wild_encouter = randint(1, 300)

					if wild_encouter == 95 :
						previous_x = pokemon_trainer.x 
						previous_y = pokemon_trainer.y
						previous_pi_x = pikachu_trainer.x
						previous_pi_y = pikachu_trainer.y
						wild = True
						isTree = True
						start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

				else :
					pokemon_trainer.x = previous_x - 0
					pokemon_trainer.y = previous_y + VEL
					pikachu_trainer.x = previous_pi_x - 0
					pikachu_trainer.y = previous_pi_y + VEL

					pygame.draw.rect(WIN, WHITE, pokemon_trainer)
					pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :
			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				previous_pi_x = pikachu_trainer.x
				previous_pi_y = pikachu_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)


def movement_down (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()
	isTree = False
	oakMessage = False

	if not wild :

		if isAsh :

			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # All Foots
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.y += VEL
		pikachu_trainer.y = pokemon_trainer.y - 70
		pikachu_trainer.x = pokemon_trainer.x + 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(TREE_1):
			WALL_SOUND.play()
			keys = pygame.key.get_pressed()
				
			if keys[pygame.K_z]:
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y - VEL
				pikachu_trainer.x = previous_pi_x
				pikachu_trainer.y = previous_pi_y - VEL
				wild_encouter = randint(1, 300)

				if wild_encouter == 95 :
					previous_x = pokemon_trainer.x 
					previous_y = pokemon_trainer.y
					previous_pi_x = pikachu_trainer.x
					previous_pi_y = pikachu_trainer.y
					wild = True
					isTree = True
					start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

			else :
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y - VEL
				pikachu_trainer.x = previous_pi_x
				pikachu_trainer.y = previous_pi_y - VEL

				pygame.draw.rect(WIN, WHITE, pokemon_trainer)
				pygame.draw.rect(WIN, WHITE, TREE_1)


		if pokemon_trainer.colliderect(TREE_2):
			WALL_SOUND.play()
			keys = pygame.key.get_pressed()
				
			if keys[pygame.K_z]:
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y - VEL
				pikachu_trainer.x = previous_pi_x
				pikachu_trainer.y = previous_pi_y - VEL
				wild_encouter = randint(1, 300)

				if wild_encouter == 95 :
					previous_x = pokemon_trainer.x 
					previous_y = pokemon_trainer.y
					previous_pi_x = pikachu_trainer.x
					previous_pi_y = pikachu_trainer.y
					wild = True
					isTree = True
					start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

			else :
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y - VEL
				pikachu_trainer.x = previous_pi_x
				pikachu_trainer.y = previous_pi_y - VEL

				pygame.draw.rect(WIN, WHITE, pokemon_trainer)
				pygame.draw.rect(WIN, WHITE, TREE_2)


		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :

			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				previous_pi_x = pikachu_trainer.x
				previous_pi_y = pikachu_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)


def bicicle_movement_left(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL) :
	VEL = 3
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	if isAsh :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_LEFT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_LEFT_RIGHT_FOOT_IMG , trainer_pokeballs, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

	else :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_LEFT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_LEFT_RIGHT_FOOT_IMG , trainer_pokeballs, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot


	pokemon_trainer.x -= VEL
	pikachu_trainer.x = pokemon_trainer.x + 60
	pikachu_trainer.y = pokemon_trainer.y - VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	if pokemon_trainer.colliderect(HOUSE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x + VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x + VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST):
		wild = False

		wild_encouter = randint(1, 500) # Generate random number 1
		wild_encounter_2 = randint(1,500) # Generate random number 2
		lucky = wild_encouter + wild_encounter_2 # Total

		if lucky == 900 :
			previous_x = pokemon_trainer.x
			previous_y = pokemon_trainer.y
			previous_pi_x = pikachu_trainer.x
			previous_pi_y = pikachu_trainer.y
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

def bicicle_movement_right(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL) :
	VEL = 3
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	if isAsh :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_RIGHT_RIGHT_FOOT_IMG , trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

	else :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_RIGHT_RIGHT_FOOT_IMG , trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot


	pokemon_trainer.x += VEL
	pikachu_trainer.x = pokemon_trainer.x - 60
	pikachu_trainer.y = pokemon_trainer.y + VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_x = pikachu_trainer.y
	previous_pi_y = pikachu_trainer.x

	if pokemon_trainer.colliderect(HOUSE_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x - VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_1)

	if pokemon_trainer.colliderect(HOUSE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x - VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x - VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(TREE_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y - 0
		pikachu_trainer.x = previous_pi_x - VEL
		pikachu_trainer.y = previous_pi_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST):
		wild = False

		wild_encouter = randint(1, 500) # Generate random number 1
		wild_encounter_2 = randint(1,500) # Generate random number 2
		lucky = wild_encouter + wild_encounter_2 # Total

		if lucky == 900 :
			previous_x = pokemon_trainer.x
			previous_y = pokemon_trainer.y
			previous_pi_x = pikachu_trainer.x
			previous_pi_y = pikachu_trainer.y
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)


def bicicle_movement_up (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL) :
	VEL = 3
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	if isAsh :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

	else :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot


	pokemon_trainer.y -= VEL
	pikachu_trainer.y = pokemon_trainer.y + 60
	pikachu_trainer.x = pokemon_trainer.x - 5
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(HOUSE_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + VEL
		pikachu_trainer.x = previous_pi_x - 0
		pikachu_trainer.y = previous_pi_y + VEL

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_1)

	if pokemon_trainer.colliderect(HOUSE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + VEL
		pikachu_trainer.x = previous_pi_x - 0
		pikachu_trainer.y = previous_pi_y + VEL

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + 5
		pikachu_trainer.x = previous_pi_x - 0
		pikachu_trainer.y = previous_pi_y + 5

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_1)

	if pokemon_trainer.colliderect(TREE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + VEL
		pikachu_trainer.x = previous_pi_x - 0
		pikachu_trainer.y = previous_pi_y + VEL

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST):
		wild = False

		wild_encouter = randint(1, 500) # Generate random number 1
		wild_encounter_2 = randint(1,500) # Generate random number 2
		lucky = wild_encouter + wild_encounter_2 # Total

		if lucky == 900 :
			previous_x = pokemon_trainer.x
			previous_y = pokemon_trainer.y
			previous_pi_x = pikachu_trainer.x
			previous_pi_y = pikachu_trainer.y
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)

def bicicle_movement_down (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, VEL) :
	VEL = 3
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	if isAsh :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BICICLE_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

	else :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL  ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BICICLE_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage,pause, VEL ) # Right foot


	pokemon_trainer.y += VEL
	pikachu_trainer.y = pokemon_trainer.y - 70
	pikachu_trainer.x = pokemon_trainer.x + VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	if pokemon_trainer.colliderect(TREE_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL
		pikachu_trainer.x = previous_pi_x
		pikachu_trainer.y = previous_pi_y - VEL

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_1)

	if pokemon_trainer.colliderect(TREE_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL
		pikachu_trainer.x = previous_pi_x
		pikachu_trainer.y = previous_pi_y - VEL

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST):
		wild = False

		wild_encouter = randint(1, 500) # Generate random number 1
		wild_encounter_2 = randint(1,500) # Generate random number 2
		lucky = wild_encouter + wild_encounter_2 # Total

		if lucky == 900:
			previous_x = pokemon_trainer.x
			previous_y = pokemon_trainer.y
			previous_pi_x = pikachu_trainer.x
			previous_pi_y = pikachu_trainer.y
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL)



# ---------------------- Shared Libs --------------------

