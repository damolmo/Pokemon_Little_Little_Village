from shopping import *
from mumu_farm import *

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


def trainer_movement_shopping (keys_pressed, pokemon_trainer, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_shopping(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_shopping(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_shopping(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_shopping(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1


def movement_left_shopping (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y


	if not wild :
		if isAsh :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.x -= VEL
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 10
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

def movement_right_shopping (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False
	cursor_pos.x = 620
	cursor_pos.y = 350
	challenge = False

	if not wild :
		if isAsh :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		if pokemon_trainer.colliderect(FARM_RECT):
			count = 0
			not_inside = True
			while (not_inside) :
				TOWN.stop()
				create_bottle_animation(MUMU_FARM_LOGO_IMG)
				# Reproduce sound
				MILTANK_SOUND.play()
				
				if count >=1 :
					MILTANK_SOUND.stop()

				count +=1

				for event in pygame.event.get() : 
						if event.type == pygame.KEYDOWN :
							if event.key == pygame.K_SPACE:
								not_inside = False

		if pokemon_trainer.colliderect(ROCKET_RECT):
			# The event will only happen one time if completed
			if variables["BATTLE_EVENTS"]["TEAM_ROCKET_EVENT"] == "NOT COMPLETED" :
				challenge = True
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				staticHP = random.randint(10, 20)
				randomLevel = random.randint(2, 12)
				variableHP = staticHP
				pokemonVariableHP = variables["TRAINER"]["POKEMON_1"]["HP"]
				pokemonStaticHP = pokemonVariableHP

				pokemonStaticHP_2 = variables["TRAINER"]["POKEMON_2"]["BASE_HP"]
				pokemonVariableHP_2 = variables["TRAINER"]["POKEMON_2"]["HP"]

				pokemonStaticHP_3 = variables["TRAINER"]["POKEMON_3"]["BASE_HP"]
				pokemonVariableHP_3 = variables["TRAINER"]["POKEMON_3"]["HP"]

				pokemonLevel = variables["TRAINER"]["POKEMON_1"]["LEVEL"]


				TOWN.stop()
				ROCKET_SOUND.play()

				if isAsh :
					create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
				else :
					create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
				
				pokemon_trainer.x = previous_x
				pokemon_trainer.y = previous_y
				time.sleep(2)

				# Start of battle opening animation
				create_team_rocket_logo()
				create_team_rocket_intro()
				time.sleep(4)

				if isAsh :
					TRAINER_IMG = ASH_BATTLE_IMG
				else :
					TRAINER_IMG = MISTY_BATTLE_IMG

				# Start of battle opening
				create_npc_transition(TEAM_ROCKET , isAsh, TRAINER_IMG, 1, 600, 100, ["MEOWTH"] )

				# Start of battle
				while (challenge) :
					if pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_1"]["HP"] and variables["TRAINER"]["POKEMON_2"]["HP"] > 0   :
						pokemonVariableHP = pokemonVariableHP_2 
						pokemonStaticHP = pokemonStaticHP_2

					elif pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_2"]["HP"] and variables["TRAINER"]["POKEMON_2"]["HP"] == 0 and variables["TRAINER"]["POKEMON_3"]["HP"] > 0   :
						pokemonVariableHP = pokemonVariableHP_3
						pokemonStaticHP = pokemonStaticHP_3

					elif pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_3"]["HP"] :
						pokemonVariableHP = 0

					create_npc_battle( ["MEOWTH"], staticHP , variableHP, randomLevel, pokemonVariableHP  )

					for event in pygame.event.get() : 

						if event.type == pygame.KEYDOWN :

							if event.key == pygame.K_RETURN :
								movement_down (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
								cursor_pos.x = 620


							if event.key == pygame.K_RIGHT:
								cursor_pos.x = 800

							if event.key == pygame.K_LEFT:
								if cursor_pos.x == 800 :
									cursor_pos.x = 620

							if event.key == pygame.K_DOWN:
								if cursor_pos.x == 800 or cursor_pos.x == 620  :
									cursor_pos.y = 400

							if event.key == pygame.K_UP:
								if cursor_pos.x == 800 or cursor_pos.x == 620 :
									cursor_pos.y = 350

							if event.key == pygame.K_SPACE and cursor_pos.x == 800 and cursor_pos.y == 400 :
								PRESS_A_SOUND.play()
								ROCKET_SOUND.stop()
								SCAPE_SOUND.play()
								time.sleep(1)
								challenge = False
								pokemon_trainer.x = previous_x - 200
								pokemon_trainer.y = previous_y

							if event.key == pygame.K_SPACE and cursor_pos.x == 620 and cursor_pos.y == 350 :
								PRESS_A_SOUND.play()
						
								# Random damage by Trainer Pokemon
								randomDamage = random.randint(2,10)

								if variableHP >= randomDamage: 
									variableHP -= randomDamage

								else :
									variableHP = 0

								# Random damage by wild Pokemon
								randomDamage = random.randint(2,10)

								if pokemonVariableHP >= randomDamage:
									pokemonVariableHP -= randomDamage

								else :
									pokemonVariableHP = 0


							if variableHP == 0 :
								if pokemonVariableHP > 0 or pokemonVariableHP_2 > 0 or pokemonVariableHP_3 > 0 : 
									# Backup of current Pokemon HP
									if pokemonStaticHP == variables["TRAINER"]["POKEMON_1"]["BASE_HP"] :
										variables["TRAINER"]["POKEMON_1"]["HP"] = pokemonVariableHP

									if pokemonStaticHP == variables["TRAINER"]["POKEMON_2"]["BASE_HP"] :
										variables["TRAINER"]["POKEMON_2"]["HP"] = pokemonVariableHP

									if pokemonStaticHP == variables["TRAINER"]["POKEMON_3"]["BASE_HP"] :
										variables["TRAINER"]["POKEMON_3"]["HP"] = pokemonVariableHP

									variables["BATTLE_EVENTS"]["TEAM_ROCKET_EVENT"] = "COMPLETED"

									challenge = False

									ROCKET_SOUND.stop()
									SCAPE_SOUND.play()
									time.sleep(1)
									VICTORY.play()


		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 10
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y


def movement_up_shopping (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	
	if not wild: 
		if isAsh :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.y -= VEL
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 10
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x


		if pokemon_trainer.colliderect(POKEMON_CENTER_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + 60
			pikachu_trainer.x = pokemon_trainer.x - VEL
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(SHOP_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANQUE_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(TREES_RECT_EAST):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(TREES_RECT_WEST):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

def movement_down_shopping (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()
	isTree = False
	oakMessage = False

	if not wild :

		if isAsh :

			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL ) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.y += VEL
		pikachu_trainer.y = pokemon_trainer.y - 70
		pikachu_trainer.x = pokemon_trainer.x + 10
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y


def create_team_rocket_intro() :
	WIN.blit(ROCKET_INTRO, (0, 0 ))
	WIN.blit(BATTLE_DIALOG, (0, 420))
	dialog = DIALOG_FONT.render("" + str("Team Rocket, Jessie and James challenge you"), 1, BLACK)
	WIN.blit(dialog, (50, 440))
	pygame.display.update()

def create_team_rocket_window(ROCKET_LOGO) :
	pygame.draw.rect(WIN, BLACK, ROCKET_LOGO_RECT)
	WIN.blit(ROCKET_LOGO, (350, 150 ))
	pygame.display.update()

def create_team_rocket_logo() :
	create_team_rocket_window(ROCKET_IMG_01) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_02) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_03) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_04) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_05) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_06) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_07) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_08) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_09) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_10) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_11) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_12) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_13) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_14) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_15) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_16) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_17) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_18) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_19) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_20) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_21) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_22) 
	clock.tick(30)
	create_team_rocket_window(ROCKET_IMG_23) 




def create_npc_transition(NPC_IMG, isAsh, TRAINER_IMG, NPC_POKEBALLS, NPC_WIDTH, TRAINER_WIDTH, NPC_POKEMON) : 
	if isAsh :
		create_npc_battle_intro(NPC_IMG, isAsh, ASH_BATTLE_IMG, NPC_POKEBALLS, NPC_WIDTH + 50, TRAINER_WIDTH - 55 , NPC_POKEMON )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, ASH_BATTLE_IMG_2, NPC_POKEBALLS, NPC_WIDTH + 100, TRAINER_WIDTH - 110, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, ASH_BATTLE_IMG_3, NPC_POKEBALLS, NPC_WIDTH + 150, TRAINER_WIDTH - 165, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh,  ASH_BATTLE_IMG_4, NPC_POKEBALLS, NPC_WIDTH + 200, TRAINER_WIDTH - 215, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, ASH_BATTLE_IMG_5, NPC_POKEBALLS, NPC_WIDTH + 250, TRAINER_WIDTH - 265, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, ASH_BATTLE_IMG_5, NPC_POKEBALLS, NPC_WIDTH + 300, TRAINER_WIDTH - 320, NPC_POKEMON  )

	else :
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG, NPC_POKEBALLS, NPC_WIDTH + 50, TRAINER_WIDTH - 55, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG, NPC_POKEBALLS, NPC_WIDTH + 100, TRAINER_WIDTH - 110, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG_2, NPC_POKEBALLS, NPC_WIDTH + 150, TRAINER_WIDTH - 165, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG_2, NPC_POKEBALLS, NPC_WIDTH + 200, TRAINER_WIDTH - 215, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG_3, NPC_POKEBALLS, NPC_WIDTH + 250, TRAINER_WIDTH - 265, NPC_POKEMON  )
		clock.tick(10)
		create_npc_battle_intro(NPC_IMG, isAsh, MISTY_BATTLE_IMG_3, NPC_POKEBALLS, NPC_WIDTH + 300, TRAINER_WIDTH - 320, NPC_POKEMON  )
		

def create_npc_battle_intro(NPC_IMG, isAsh, TRAINER_IMG, NPC_POKEBALLS, NPC_WIDTH, TRAINER_WIDTH, NPC_POKEMON) :
	WIN.blit(BATTLE_INTRO, (0,0))

	# NPCS Transition
	WIN.blit(NPC_IMG, (NPC_WIDTH, 50))
	clock.tick(30)
	
	# Trainer Transition
	WIN.blit(TRAINER_IMG, (TRAINER_WIDTH, 300))
	clock.tick(30)


	# NPC Pokeballs
	if NPC_POKEBALLS == 1 :
		WIN.blit(POKEBALL_ITEM, (75, 44))


	# Trainer Available pokeballs
	if variables["TRAINER"]["POKEMON_1"]["HP"] > 0 :
		WIN.blit(POKEBALL_ITEM, (760, 410))

	if variables["TRAINER"]["POKEMON_2"]["HP"] > 0 :
		WIN.blit(POKEBALL_ITEM, (707, 410))

	if variables["TRAINER"]["POKEMON_3"]["HP"] > 0 :
		WIN.blit(POKEBALL_ITEM, (650, 410))

	pygame.display.update()



def create_npc_battle(NPC_POKEMON, staticHP , variableHP, randomLevel, pokemonVariableHP) :
	WIN.blit(BATTLE_ARENA, (0,0))
	WIN.blit(BATTLE_MENU, (600,410)) # Place background image
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	WIN.blit(LIFE_MENU, (680, 30))
	WIN.blit(LIFE_MENU, (0, 30))

	# NPC Pokemon
	for pokemon in NPC_POKEMON :
		if pokemon == "MEOWTH":
			WIN.blit(MEOWTH_IMG_01, (600, 50))
			wild = RULES.render("" + str(pokemon), 1, BLACK)
			WIN.blit(wild, (685, 35))
			level = RULES.render("Lv " + str(randomLevel), 1, BLACK)
			WIN.blit(level, (840, 35))

			stats = RULES.render("" + str(variableHP), 1, BLACK)
			WIN.blit(stats, (692, 60))

			separator = RULES.render("/", 1, BLACK)
			WIN.blit(separator, (710, 60))

			stats = RULES.render("" + str(staticHP) , 1, BLACK)
			WIN.blit(stats, (720, 60))

	# Trainer Pokemon
	if variables["TRAINER"]["POKEMON_1"]["HP"] > 0 :
		if variables["TRAINER"]["POKEMON_1"]["NAME"] == "PIKACHU"  :
			WIN.blit(PIKACHU_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_1"]["NAME"] == "BULBASAUR"  :
			WIN.blit(BULBASAUR_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_1"]["NAME"] == "CHARMANDER"  :
			WIN.blit(CHARMANDER_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_1"]["NAME"] == "SQUIRTLE"  :
			WIN.blit(SQUIRTLE_BATTLE_IMG, (100, 300))

		friend = RULES.render("" + str(variables["TRAINER"]["POKEMON_1"]["NAME"]), 1, BLACK)
		WIN.blit(friend, (5, 35))

		stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
		WIN.blit(stats, (12, 60))

		separator = RULES.render("/", 1, BLACK)
		WIN.blit(separator, (30, 60))

		stats = RULES.render("" + str(variables["TRAINER"]["POKEMON_1"]["BASE_HP"]), 1, BLACK)
		WIN.blit(stats, (40, 60))


		level = RULES.render("Lv " + str(variables["TRAINER"]["POKEMON_1"]["LEVEL"]), 1, BLACK)
		WIN.blit(level, (160, 35))


	elif variables["TRAINER"]["POKEMON_1"]["HP"] == 0 and variables["TRAINER"]["POKEMON_2"]["HP"] > 0 :
		if variables["TRAINER"]["POKEMON_2"]["NAME"] == "PIKACHU"  :
			WIN.blit(PIKACHU_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_2"]["NAME"] == "BULBASAUR"  :
			WIN.blit(BULBASAUR_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_2"]["NAME"] == "CHARMANDER"  :
			WIN.blit(CHARMANDER_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_2"]["NAME"] == "SQUIRTLE"  :
			WIN.blit(SQUIRTLE_BATTLE_IMG, (100, 300))

		friend = RULES.render("" + str(variables["TRAINER"]["POKEMON_2"]["NAME"]), 1, BLACK)
		WIN.blit(friend, (5, 35))

		stats = RULES.render("" + str(variables["TRAINER"]["POKEMON_2"]["HP"]) , 1, BLACK)
		WIN.blit(stats, (12, 60))

		separator = RULES.render("/", 1, BLACK)
		WIN.blit(separator, (30, 60))

		stats = RULES.render("" + str(variables["TRAINER"]["POKEMON_2"]["BASE_HP"]), 1, BLACK)
		WIN.blit(stats, (40, 60))


		level = RULES.render("Lv " + str(variables["TRAINER"]["POKEMON_2"]["LEVEL"]), 1, BLACK)
		WIN.blit(level, (160, 35))

	elif variables["TRAINER"]["POKEMON_2"]["HP"] == 0 and variables["TRAINER"]["POKEMON_3"]["HP"] > 0 :
		if variables["TRAINER"]["POKEMON_3"]["NAME"] == "PIKACHU"  :
			WIN.blit(PIKACHU_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_3"]["NAME"] == "BULBASAUR"  :
			WIN.blit(BULBASAUR_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_3"]["NAME"] == "CHARMANDER"  :
			WIN.blit(CHARMANDER_BATTLE_IMG, (100, 300))

		elif variables["TRAINER"]["POKEMON_3"]["NAME"] == "SQUIRTLE"  :
			WIN.blit(SQUIRTLE_BATTLE_IMG, (100, 300))

		friend = RULES.render("" + str(variables["TRAINER"]["POKEMON_3"]["NAME"]), 1, BLACK)
		WIN.blit(friend, (5, 35))

		stats = RULES.render("" + str(variables["TRAINER"]["POKEMON_3"]["HP"]) , 1, BLACK)
		WIN.blit(stats, (12, 60))

		separator = RULES.render("/", 1, BLACK)
		WIN.blit(separator, (30, 60))

		stats = RULES.render("" + str(variables["TRAINER"]["POKEMON_3"]["BASE_HP"]), 1, BLACK)
		WIN.blit(stats, (40, 60))


		level = RULES.render("Lv " + str(variables["TRAINER"]["POKEMON_3"]["LEVEL"]), 1, BLACK)
		WIN.blit(level, (160, 35))

	pygame.display.update()