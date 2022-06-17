from resources import *
from save_game import *
from pika import *
from bag import *
from trainer_movement_shopping import *
from center import *
from shop import *



def create_shopping_area (pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL) :
	now = datetime.now()
	hora = now.strftime("%H")


	if hora <="16" and hora >="10" :
		WIN.blit(SHOPPING_IMG, (0,0)) # Place background image

	elif hora >="17" and hora <"20":
		WIN.blit(SHOPPING_EVENING_IMG, (0,0)) # Place background image

	else:
		WIN.blit(SHOPPING_NIGHT_IMG, (0,0)) # Place background image
	

	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

	if variables["BATTLE_EVENTS"]["TEAM_ROCKET_EVENT"] == "NOT COMPLETED" :
		# Team Rocket event
		WIN.blit(JESSIE_IMG_01, (700, 300))
		WIN.blit(JAMES_IMG_01, (770, 300))

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



	#pygame.draw.rect(WIN, GREEN, ROCKET_RECT)
	#pygame.draw.rect(WIN, GREEN, POKEMON_CENTER_RECT)
	#pygame.draw.rect(WIN, GREEN, SHOP_RECT)
	#pygame.draw.rect(WIN, BLUE, ESTANQUE_RECT)
	#pygame.draw.rect(WIN, BLUE, TREES_RECT_EAST)
	#pygame.draw.rect(WIN, BLUE, TREES_RECT_WEST)
	#pygame.draw.rect(WIN, BLUE, SHOP_DOOR_RECT)
	#pygame.draw.rect(WIN, BLUE, CENTER_DOOR_RECT)
	
	

	pygame.display.update()

def access_shopping_area (pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty) :
	
	shopping = True
	trainer_pokeballs = []
	oakMessage = False
	pause = -1
	pokemon_trainer.x = before_enter_house_x 
	pokemon_trainer.y = before_enter_house_y + 20
	free_pika = 0
	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
	VEL = 6

	if isAsh :
		TRAINER_IMG = ASH_IMG
	else :
		TRAINER_IMG = MISTY_IMG

	if inside == True :
		pokemon_trainer.x = 100
		pokemon_trainer.y = 400
		BACKGROUND_SOUND.stop()

		if isAsh :
			TRAINER_IMG = ASH_RIGHT_IMG
		else :
			TRAINER_IMG = MISTY_RIGHT_IMG

	while shopping :
		SHOP_SOUND.stop()
		CENTER_SOUND.stop()
		pause = 0
		create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL) # All Foots

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

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				
			if keys[pygame.K_RIGHT] :
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				save_game()
				welcome()

			if keys[pygame.K_x]:
				pause += 1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

				pause_menu(cursor_pause, pause)

			if pokemon_trainer.colliderect(HOME_RECT_MAP):
				TOWN.stop()
				SCAPE_SOUND.play()
				shopping = False
				pokemon_trainer.x = before_enter_house_x
				pokemon_trainer.y = before_enter_house_y + 20

			if pokemon_trainer.colliderect(SHOP_DOOR_RECT):
				previous_y = pokemon_trainer.y + 10
				previous_x = pokemon_trainer.x
				previous_pi_y = pikachu_trainer.y
				previous_pi_x = pikachu_trainer.x
				TOWN.stop()
				inside = True
				access_shop(pokemon_trainer, pikachu_trainer, inside, previous_pi_x, previous_pi_y, isAsh, isMisty)

			if pokemon_trainer.colliderect(CENTER_DOOR_RECT):
				previous_y = pokemon_trainer.y + 10
				previous_x = pokemon_trainer.x
				previous_pi_y = pikachu_trainer.y
				previous_pi_x = pikachu_trainer.x
				inside = True
				TOWN.stop()
				access_center(pokemon_trainer, pikachu_trainer, inside, previous_pi_x, previous_pi_y, isAsh, isMisty)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1

		TOWN.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement_shopping(keys_pressed, pokemon_trainer, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
		create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)


