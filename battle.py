import pygame
from resources import *
from save_game import *
from pokemon import *

def pre_area(POKEMON, POKEMON_NAME, ASH) :
	now = datetime.now()
	hora = now.strftime("%H")

	# Create initial background
	if hora <="16" and hora >="10" :
		WIN.blit(BATTLE_ARENA_IMG, (0,0))

	elif hora >="17" and hora <"20":
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0)) # Place background image

	else:
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0))

	# Create Wild Pokemon
	WIN.blit(POKEMON, (640,160))


	# Create Ash opening animation
	WIN.blit(ASH, (0,220))

	# Create Wild Pokemon Dialog 
	WIN.blit(BATTLE_DIALOG, (0, 420))
	dialog = DIALOG_FONT.render("" + str("A Wild Pokémon Appeared!"), 1, BLACK)
	WIN.blit(dialog, (50, 440))
	if variables["TRAINER"]["POKEMON_1"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["TRAINER"]["POKEMON_1"]["NAME"].capitalize())  + "!"), 1, BLACK)

	elif variables["TRAINER"]["POKEMON_1"]["HP"] == 0 and variables["TRAINER"]["POKEMON_2"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["TRAINER"]["POKEMON_2"]["NAME"].capitalize())  + "!"), 1, BLACK)


	elif variables["TRAINER"]["POKEMON_1"]["HP"] == 0 and variables["TRAINER"]["POKEMON_2"]["HP"] == 0 and  variables["TRAINER"]["POKEMON_3"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["TRAINER"]["POKEMON_3"]["NAME"].capitalize())  + "!"), 1, BLACK)

	WIN.blit(dialog, (50, 460))

	# Display Wild Pokemon Name
	date = RULES.render("" + str(POKEMON_NAME), 1, BLACK)
	WIN.blit(date, (5, 35))


	pygame.display.update()

def create_battle_opening (frame) :

	WIN.blit(frame, (0,0)) # Place background image
	pygame.display.update()


def create_opening_anim () :

	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	create_battle_opening(BATTLE_ARENA_IMG_01)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	create_battle_opening(BATTLE_ARENA_IMG_02)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	create_battle_opening(BATTLE_ARENA_IMG_03)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	create_battle_opening(BATTLE_ARENA_IMG_04)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	create_battle_opening(BATTLE_ARENA_IMG_05)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	create_battle_opening(BATTLE_ARENA_IMG_06)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	create_battle_opening(BATTLE_ARENA_IMG_07)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	create_battle_opening(BATTLE_ARENA_IMG_08)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	create_battle_opening(BATTLE_ARENA_IMG_09)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	create_battle_opening(BATTLE_ARENA_IMG_10)
	

	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	create_battle_opening(BATTLE_ARENA_IMG_11)
	clock.tick(15)

	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)
	create_battle_opening(BATTLE_ARENA_IMG_12)




def random_pokemon (isTree) :

	pokemon_route = []
	now = datetime.now()
	hora = now.strftime("%H")

	wild_appeared = 0
	if int(hora) >= 20 and not isTree :
		pokemon_route = ["UMBREON", "GASTLY", "GENGAR", "ARCANINE"]

	if int(hora) >= 00 and  int(hora) <= 9 and not isTree:
		pokemon_route = ["UMBREON", "GASTLY", "GENGAR", "ARCANINE"]


	if int(hora) >=10 and int(hora) < 20 and not isTree :
		pokemon_route = ["PIKACHU", "SQUIRTLE", "CHARMANDER", "BULBASAUR", "PSYDUCK", "MEOWTH", "EEVEE", "GROWLITHE", "MRMIME"]

	if isTree == True :
		pokemon_route = ["BEEDRILL", "SCYTHER"]


	wild_appeared = random.choice(pokemon_route)

	return wild_appeared


def wild_asset (wild_appeared) :

	pokemon = ""

	if wild_appeared == "PIKACHU" :
		pokemon = PIKACHU_IMG_1

	elif wild_appeared == "SQUIRTLE" :
		pokemon = SQUIRTLE_IMG_01

	elif wild_appeared == "CHARMANDER" :
		pokemon = CHARMANDER_IMG_01

	elif wild_appeared == "BULBASAUR" :
		pokemon = BULBASAUR_IMG_01

	elif wild_appeared == "PSYDUCK" :
		pokemon = PSYDUCK_IMG_01

	elif wild_appeared == "MEOWTH" :
		pokemon = MEOWTH_IMG_01

	elif wild_appeared == "UMBREON" :
		pokemon = UMBREON_IMG_02

	elif wild_appeared == "GASTLY" :
		pokemon = GASTLY_IMG_01

	elif wild_appeared == "GENGAR" :
		pokemon = GENGAR_IMG_01

	elif wild_appeared == "BEEDRILL" :
		pokemon = BEEDRILL_IMG_01

	elif wild_appeared == "SCYTHER" :
		pokemon = SCYTHER_IMG_01

	elif wild_appeared == "EEVEE" :
		pokemon = EEVEE_IMG_01

	elif wild_appeared == "ARCANINE" :
		pokemon = ARCANINE_IMG_01

	elif wild_appeared == "GROWLITHE" :
		pokemon = GROWLITHE_IMG_01

	elif wild_appeared == "MRMIME" :
		pokemon = MRMIME_IMG_01

	return pokemon

def wild_pokemon (wild_appeared, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) :

	pokemon = ""

	if wild_appeared == "PIKACHU" :
		create_Pikachu(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "SQUIRTLE" :
		create_Squirtle(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "CHARMANDER" :
		create_Charmander(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "BULBASAUR" :
		create_Bulbasaur(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "PSYDUCK" :
		create_Psyduck(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "MEOWTH":
		create_Meowth(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "UMBREON" :
		create_Umbreon(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "GASTLY" :
		create_Gastly(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "GENGAR" :
		create_Gengar(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "BEEDRILL":
		create_Beedrill(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "SCYTHER":
		create_Scyther(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "EEVEE":
		create_Eevee(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 

	elif wild_appeared == "ARCANINE":
		create_Arcanine(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs)

	elif wild_appeared == "GROWLITHE":
		create_Growlithe(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs)  

	elif wild_appeared == "MRMIME":
		create_MrMime(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs)  

def check_battle_threads () :
	variables["THREADS"]["BATTLE"] = "NO"
	silent_save_game()


def start_battle(wild,x ,y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL) :
	trainer_pokeballs = []
	GRASS_SOUND.stop()
	BACKGROUND_SOUND.stop()
	cursor_pos.x = 620
	cursor_pos.y = 350
	POKEMON_ENCOUNTER_SOUND.play()
	time.sleep(1.2)
	pokemon = random_pokemon(isTree)
	sound = 0
	opening = True
	pause = False
	staticHP = random.randint(10, 20)
	randomLevel = random.randint(2, 12)
	variableHP = staticHP
	pokemonStaticHP = variables["TRAINER"]["POKEMON_1"]["BASE_HP"]
	pokemonVariableHP = variables["TRAINER"]["POKEMON_1"]["HP"]
	
	pokemonStaticHP_2 = variables["TRAINER"]["POKEMON_2"]["BASE_HP"]
	pokemonVariableHP_2 = variables["TRAINER"]["POKEMON_2"]["HP"]

	pokemonStaticHP_3 = variables["TRAINER"]["POKEMON_3"]["BASE_HP"]
	pokemonVariableHP_3 = variables["TRAINER"]["POKEMON_3"]["HP"]

	pokemonLevel = variables["TRAINER"]["POKEMON_1"]["LEVEL"]


	POKEMON = wild_asset(pokemon)

	create_opening_anim()
	if isAsh :
		create_ash_opening_anim(POKEMON, "")

	else :
		create_misty_opening_anim(POKEMON, "")

	time.sleep(1.5)

	check_battle_threads()
 
	t7 = threading.Thread(target = create_battle_pokemon , name="t1", args=([pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs, pokemonStaticHP_2, pokemonStaticHP_3, pokemonVariableHP_2, pokemonVariableHP_3]))
	t8 = threading.Thread(target = create_battle_keyboard , name="t2", args=([pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs, pokemonStaticHP_2, pokemonStaticHP_3, pokemonVariableHP_2, pokemonVariableHP_3]))

	t7.start()
	t8.start()

	start = create_battle_keyboard (pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs, pokemonStaticHP_2, pokemonStaticHP_3, pokemonVariableHP_2, pokemonVariableHP_3)

	while variables["THREADS"]["BATTLE"] == "NO":
		t8.join()
		t7.join()


def create_battle_pokemon (pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs, pokemonStaticHP_2, pokemonStaticHP_3, pokemonVariableHP_2, pokemonVariableHP_3) :

	while variables["THREADS"]["BATTLE"] == "NO":

		if pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_1"]["HP"] and variables["TRAINER"]["POKEMON_2"]["HP"] > 0   :
			pokemonVariableHP = pokemonVariableHP_2 
			pokemonStaticHP = pokemonStaticHP_2

		elif pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_2"]["HP"] and variables["TRAINER"]["POKEMON_2"]["HP"] == 0 and variables["TRAINER"]["POKEMON_3"]["HP"] > 0   :
			pokemonVariableHP = pokemonVariableHP_3
			pokemonStaticHP = pokemonStaticHP_3

		elif pokemonVariableHP == 0 and pokemonVariableHP == variables["TRAINER"]["POKEMON_3"]["HP"] :
			pokemonVariableHP = 0


		wild_pokemon (pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) 
		sound +=1


def create_battle_keyboard (pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs, pokemonStaticHP_2, pokemonStaticHP_3, pokemonVariableHP_2, pokemonVariableHP_3) :

	while variables["THREADS"]["BATTLE"] == "NO":

		for event in pygame.event.get() : 

				if event.type == pygame.KEYDOWN :

					if event.key == pygame.K_SPACE and cursor_pos.x == 800 and cursor_pos.y == 400 :
						PRESS_A_SOUND.play()
						POKEMON_ENCOUNTER_SOUND.stop()
						SCAPE_SOUND.play()
						time.sleep(1)
						variables["TRAINER"]["POKEMON_1"]["HP"] = pokemonVariableHP
						variables["TRAINER"]["POKEMON_2"]["HP"] = pokemonVariableHP_2
						variables["TRAINER"]["POKEMON_3"]["HP"] = pokemonVariableHP_3
						variables["THREADS"]["BATTLE"] = "YES"
						print("HAS HUIDO")
						cursor_pos.x = 620

					if event.key == pygame.K_SPACE and cursor_pos.x == 800 and cursor_pos.y == 350 :
						if isAsh :
							create_ash_opening_anim(POKEMON, "")
						else :
							create_misty_opening_anim(POKEMON, "")
						time.sleep(1.5)

						if  len(trainer_pokeballs) < MAX_POKEBALL:
							pokeball = pygame.Rect(
							pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 10, 5)
							trainer_pokeballs.append(pokeball)

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


					if variableHP == 0 or pokemonVariableHP == 0 and pokemonVariableHP_2 == 0 and pokemonVariableHP_3 == 0 :
						# Backup of current Pokemon HP
						if pokemonStaticHP == variables["TRAINER"]["POKEMON_1"]["BASE_HP"] :
							variables["TRAINER"]["POKEMON_1"]["HP"] = pokemonVariableHP

						if pokemonStaticHP == variables["TRAINER"]["POKEMON_2"]["BASE_HP"] :
							variables["TRAINER"]["POKEMON_2"]["HP"] = pokemonVariableHP

						if pokemonStaticHP == variables["TRAINER"]["POKEMON_3"]["BASE_HP"] :
							variables["TRAINER"]["POKEMON_3"]["HP"] = pokemonVariableHP

						POKEMON_ENCOUNTER_SOUND.stop()
						SCAPE_SOUND.play()
						time.sleep(1)
						VICTORY.play()
						wild = True

						while wild :
							create_victory_windows(variables["TRAINER"]["POKEMON_1"]["NAME"], pokemonVariableHP, pokemon, variableHP)

							for event in pygame.event.get() : 

								if event.type == pygame.KEYDOWN :

									if event.key == pygame.K_RETURN :
										wild = False
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


def throw_pokeball_wild(trainer_pokeballs) :
	for pokeball in trainer_pokeballs:
		pokeball.x += POKEBALL_VEL

		if pokemon_trainer.colliderect(pokeball):
			trainer_pokeballs.remove(pokeball)

		if pokeball.x > WIDTH :
			trainer_pokeballs.remove(pokeball)


def create_victory_windows(trainer_pokemon_name, trainer_pokemon_hp, wild_pokemon_name, wild_pokemon_hp) :

	# Wild Pokemon

	WIN.blit(STARS, (0,0))

	if trainer_pokemon_hp == 0 and wild_pokemon_hp == 0 :
		asset = wild_asset(trainer_pokemon_name)
		WIN.blit(asset, (380,150))
		wild = WINNER_LOOSER_DIALOG.render(trainer_pokemon_name + " WIN!", 1, BLACK)
		WIN.blit(wild, (150, 50))
		trainer = POKEBALLS_COUNTER.render("Press (ENTER) to exit", 1, BLACK)
		WIN.blit(trainer, (300, 400))
		clock.tick(20)
		

	elif trainer_pokemon_hp > 0 and wild_pokemon_hp == 0 :
		asset = wild_asset(trainer_pokemon_name)
		WIN.blit(asset, (380,150))
		wild = WINNER_LOOSER_DIALOG.render(trainer_pokemon_name + " WIN!", 1, BLACK)
		WIN.blit(wild, (150, 50))
		trainer = POKEBALLS_COUNTER.render("Press (ENTER) to exit", 1, BLACK)
		WIN.blit(trainer, (300, 400))
		clock.tick(20)

	# Trainer Pokemon
	if trainer_pokemon_hp == 0 and wild_pokemon_hp > 0 :
		asset = wild_asset(wild_pokemon_name)
		WIN.blit(asset, (380,150))
		wild = WINNER_LOOSER_DIALOG.render("YOU LOOSE!", 1, BLACK)
		WIN.blit(wild, (210, 50))
		trainer = POKEBALLS_COUNTER.render("Press (ENTER) to exit", 1, BLACK)
		WIN.blit(trainer, (300, 400))
		clock.tick(20)

	pygame.display.update()


def create_ash_opening_anim (POKEMON, POKEMON_NAME) :
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_2)
	clock.tick(5)


	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_3)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	pre_area(POKEMON, POKEMON_NAME, ASH_BATTLE_IMG_4)
	clock.tick(5)




def create_misty_opening_anim (POKEMON, POKEMON_NAME) :
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_2)
	clock.tick(5)


	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	clock.tick(5)

	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
	pre_area(POKEMON, POKEMON_NAME, MISTY_BATTLE_IMG_3)
