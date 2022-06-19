from save_game import *
from pika import *
from resources import *
from main import *
from trainer_movement import *
from laboratory import *
from house import *
from shopping import *
import time

def create_map(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL) :

	now = datetime.now()
	hora = now.strftime("%H")
	import time


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


def daily_rewards () :

	now = fecha = today.strftime("%B %d, %Y")
	days = variables["TRAINER"]["DAYS_PLAYING"]
	count = 0
	your_reward = ""

	if now not in days :
		days.append(now)

		for day in days  :
			count +=1

		position = str(count)

		item = variables["DAILY_REWARDS"][position]["OBJECT"]
		value = variables["DAILY_REWARDS"][position]["VALUE"]
		variables["DAILY_REWARDS"][position]["OBTAINED"] = "YES"

		your_reward = ("Daily Reward: Day %d: You obtained %d %s") % (count, value, item )

		## Add the gift to trainer bag
		if item == "POKEBALL" :
			variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_AVAILABLE"] += value

		elif item == "POTION" :
			variables["TRAINER"]["TRAINER_BAG"]["POTIONS_AVAILABLE"] += value

		elif item  == "REVIVE" :
			variables["TRAINER"]["TRAINER_BAG"]["REVIVES_AVAILABLE"] += value

	else  :
		your_reward = "NONE"
		save_game()
		
	return your_reward

def create_reward_window (reward) :
	# Daily Rewards

	if reward != "NONE" :
		WIN.blit(DIALOG_MENU, (0, 300))
		message = POKEBALLS_COUNTER.render(reward, 1, WHITE)
		WIN.blit(message, (180, 400))

	pygame.display.update()

def create_area (POKEMON, POKEMON_NAME, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) :

	now = datetime.now()
	hora = now.strftime("%H")

	if hora <="16" and hora >="10" :
		WIN.blit(BATTLE_ARENA_IMG, (0,0))

	elif hora >="17" and hora <"20":
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0)) # Place background image

	else:
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0))


	# Battle Elements
	#WIN.blit(PIKACHU_BATTLE_IMG, (0,250))
	WIN.blit(POKEMON, (640,160))
	WIN.blit(BATTLE_MENU, (600,410)) # Place background image
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	WIN.blit(LIFE_MENU, (680, 30))
	WIN.blit(LIFE_MENU, (0, 30))

	wild = RULES.render("" + str(POKEMON_NAME), 1, BLACK)
	WIN.blit(wild, (685, 35))

	level = RULES.render("Lv " + str(randomLevel), 1, BLACK)
	WIN.blit(level, (840, 35))

	stats = RULES.render("" + str(variableHP), 1, BLACK)
	WIN.blit(stats, (692, 60))

	separator = RULES.render("/", 1, BLACK)
	WIN.blit(separator, (710, 60))

	stats = RULES.render("" + str(staticHP) , 1, BLACK)
	WIN.blit(stats, (720, 60))

	if variables["TRAINER"]["POKEMON_1"]["HP"] > 0 :

		WIN.blit(PIKACHU_BATTLE_IMG, (0,250))

		friend = RULES.render("" + str("PIKACHU"), 1, BLACK)
		WIN.blit(friend, (5, 35))

		stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
		WIN.blit(stats, (12, 60))

		separator = RULES.render("/", 1, BLACK)
		WIN.blit(separator, (30, 60))

		stats = RULES.render("" + str(pokemonStaticHP), 1, BLACK)
		WIN.blit(stats, (40, 60))


		level = RULES.render("Lv " + str(pokemonLevel), 1, BLACK)
		WIN.blit(level, (160, 35))

	elif variables["TRAINER"]["POKEMON_1"]["HP"] == 0 :
		if variables["TRAINER"]["POKEMON_2"]["HP"] > 0 :

			if variables["TRAINER"]["POKEMON_2"]["NAME"] == "SQUIRTLE":
				WIN.blit(SQUIRTLE_BATTLE_IMG, (0,250))

			elif variables["TRAINER"]["POKEMON_2"]["NAME"] == "CHARMANDER":
					WIN.blit(CHARMANDER_BATTLE_IMG, (0,250))

			elif variables["TRAINER"]["POKEMON_2"]["NAME"] == "BULBASAUR":
					WIN.blit(BULBASAUR_BATTLE_IMG, (0,250))


			friend = RULES.render("" + str(variables["TRAINER"]["POKEMON_2"]["NAME"]), 1, BLACK)
			WIN.blit(friend, (5, 35))

			stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
			WIN.blit(stats, (12, 60))

			separator = RULES.render("/", 1, BLACK)
			WIN.blit(separator, (30, 60))

			stats = RULES.render("" + str(pokemonStaticHP), 1, BLACK)
			WIN.blit(stats, (40, 60))


			level = RULES.render("Lv " + str(variables["TRAINER"]["POKEMON_2"]["LEVEL"]), 1, BLACK)
			WIN.blit(level, (160, 35))

		elif variables["TRAINER"]["POKEMON_1"]["HP"] == 0 and variables["TRAINER"]["POKEMON_2"]["HP"] == 0 :
			if variables["TRAINER"]["POKEMON_3"]["HP"] > 0 :

				if variables["TRAINER"]["POKEMON_3"]["NAME"] == "SQUIRTLE":
					WIN.blit(SQUIRTLE_BATTLE_IMG, (0,250))

				elif variables["TRAINER"]["POKEMON_3"]["NAME"] == "CHARMANDER":
						WIN.blit(CHARMANDER_BATTLE_IMG, (0,250))

				elif variables["TRAINER"]["POKEMON_3"]["NAME"] == "BULBASAUR":
						WIN.blit(BULBASAUR_BATTLE_IMG, (0,250))


				friend = RULES.render("" + str(variables["TRAINER"]["POKEMON_3"]["NAME"]), 1, BLACK)
				WIN.blit(friend, (5, 35))

				stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
				WIN.blit(stats, (12, 60))

				separator = RULES.render("/", 1, BLACK)
				WIN.blit(separator, (30, 60))

				stats = RULES.render("" + str(pokemonStaticHP), 1, BLACK)
				WIN.blit(stats, (40, 60))


				level = RULES.render("Lv " + str(variables["TRAINER"]["POKEMON_3"]["LEVEL"]), 1, BLACK)
				WIN.blit(level, (160, 35))


	pygame.display.update()

