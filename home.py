from save_game import *
from pika import *
from resources import *
from main import *
from trainer_movement import *
from laboratory import *
from house import *
from shopping import *
import time

def check_home_threads() :
	variables["THREADS"]["HOME"] = "NO"
	silent_save_game()

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

		if count < 31 :

			position = str(count)
			variables["DAILY_REWARDS"][position]["OBTAINED"] = "YES"
			item = variables["DAILY_REWARDS"][position]["OBJECT"]
			value = variables["DAILY_REWARDS"][position]["VALUE"]

			your_reward = ("Daily Reward: Day %d: You obtained %d %s") % (count, value, item )

			## Add the gift to trainer bag
			if item == "POKEBALL" :
				variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_AVAILABLE"] += value

			elif item == "POTION" :
				variables["TRAINER"]["TRAINER_BAG"]["POTIONS_AVAILABLE"] += value

			elif item  == "REVIVE" :
				variables["TRAINER"]["TRAINER_BAG"]["REVIVES_AVAILABLE"] += value

		else : 
			your_reward = "RECEIVED"

	else  :
		your_reward = "NONE"
		
	return your_reward

def create_reward_window (reward) :
	# Daily Rewards

	if reward != "NONE" :
		WIN.blit(DIALOG_MENU, (0, 300))
		message = POKEBALLS_COUNTER.render(reward, 1, WHITE)
		WIN.blit(message, (165, 400))

	pygame.display.update()

def access_reward_calendar () :

	calendar = True

	while calendar :
		create_reward_calendar ()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_BACKSPACE :
					calendar = False


def create_reward_calendar () :
	WIN.blit(GIFT_CALENDAR_IMG, (0,0))


	if variables["DAILY_REWARDS"]["1"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (15, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][0]), 1, BLACK)
		WIN.blit(day_1, (30, 90))

	if variables["DAILY_REWARDS"]["2"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (155, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][1]), 1, BLACK)
		WIN.blit(day_1, (170, 90))

	if variables["DAILY_REWARDS"]["3"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (295, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][2]), 1, BLACK)
		WIN.blit(day_1, (310, 90))

	if variables["DAILY_REWARDS"]["4"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (435, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][3]), 1, BLACK)
		WIN.blit(day_1, (450, 90))

	if variables["DAILY_REWARDS"]["5"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (575, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][4]), 1, BLACK)
		WIN.blit(day_1, (590, 90))

	if variables["DAILY_REWARDS"]["6"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (715, 5))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][5]), 1, BLACK)
		WIN.blit(day_1, (730, 90))

	if variables["DAILY_REWARDS"]["7"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (15, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][6]), 1, BLACK)
		WIN.blit(day_1, (30, 190))

	if variables["DAILY_REWARDS"]["8"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (155, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][7]), 1, BLACK)
		WIN.blit(day_1, (170, 190))

	if variables["DAILY_REWARDS"]["9"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (295, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][8]), 1, BLACK)
		WIN.blit(day_1, (310, 190))

	if variables["DAILY_REWARDS"]["10"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (435, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][9]), 1, BLACK)
		WIN.blit(day_1, (450, 190))

	if variables["DAILY_REWARDS"]["11"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (575, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][10]), 1, BLACK)
		WIN.blit(day_1, (590, 190))

	if variables["DAILY_REWARDS"]["12"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (715, 105))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][11]), 1, BLACK)
		WIN.blit(day_1, (730, 190))

	if variables["DAILY_REWARDS"]["13"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (15, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][12]), 1, BLACK)
		WIN.blit(day_1, (30, 290))

	if variables["DAILY_REWARDS"]["14"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (155, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][13]), 1, BLACK)
		WIN.blit(day_1, (170, 290))

	if variables["DAILY_REWARDS"]["15"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (295, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][14]), 1, BLACK)
		WIN.blit(day_1, (310, 290))

	if variables["DAILY_REWARDS"]["16"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (435, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][15]), 1, BLACK)
		WIN.blit(day_1, (450, 290))

	if variables["DAILY_REWARDS"]["17"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (575, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][16]), 1, BLACK)
		WIN.blit(day_1, (590, 290))

	if variables["DAILY_REWARDS"]["18"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (715, 205))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][17]), 1, BLACK)
		WIN.blit(day_1, (730, 290))

	if variables["DAILY_REWARDS"]["19"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (15, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][18]), 1, BLACK)
		WIN.blit(day_1, (30, 390))

	if variables["DAILY_REWARDS"]["20"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (155, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][19]), 1, BLACK)
		WIN.blit(day_1, (170, 390))

	if variables["DAILY_REWARDS"]["21"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (295, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][20]), 1, BLACK)
		WIN.blit(day_1, (310, 390))

	if variables["DAILY_REWARDS"]["22"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (435, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][21]), 1, BLACK)
		WIN.blit(day_1, (450, 390))

	if variables["DAILY_REWARDS"]["23"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (575, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][22]), 1, BLACK)
		WIN.blit(day_1, (590, 390))

	if variables["DAILY_REWARDS"]["24"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (715, 305))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][23]), 1, BLACK)
		WIN.blit(day_1, (730, 390))

	if variables["DAILY_REWARDS"]["25"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (15, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][24]), 1, BLACK)
		WIN.blit(day_1, (30, 490))

	if variables["DAILY_REWARDS"]["26"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (155, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][25]), 1, BLACK)
		WIN.blit(day_1, (170, 490))

	if variables["DAILY_REWARDS"]["27"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (295, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][26]), 1, BLACK)
		WIN.blit(day_1, (310, 490))

	if variables["DAILY_REWARDS"]["28"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (435, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][27]), 1, BLACK)
		WIN.blit(day_1, (450, 490))

	if variables["DAILY_REWARDS"]["29"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (575, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][28]), 1, BLACK)
		WIN.blit(day_1, (590, 490))

	if variables["DAILY_REWARDS"]["30"]["OBTAINED"] == "YES" :
		WIN.blit(GIFT_SIGN_IMG, (715, 405))
		day_1 = GIFS.render(str(variables["TRAINER"]["DAYS_PLAYING"][28]), 1, BLACK)
		WIN.blit(day_1, (730, 490))



	pygame.display.update()



def create_area (POKEMON, POKEMON_NAME, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel, trainer_pokeballs) :

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


	pokeball = POKEBALL_ITEM.get_rect()
	pokeball = pygame.Rect(
		pokemon_trainer.x, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 10, 5)

	for pokeball in trainer_pokeballs :
		WIN.blit(POKEBALL_ITEM, pokeball)

	pygame.display.update()


