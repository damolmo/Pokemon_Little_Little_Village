from save_game import *
from resources import *

def create_pause_menu () :

	WIN.blit(TRAINER_PAUSE_MENU_IMG, (0,0))

	if variables["TRAINER"]["CHARACTER"] == "ASH" :
		TRAINER_IMG = ASH_IMG

	else :
		TRAINER_IMG = MISTY_IMG

	TRAINER_IMG = pygame.transform.scale(TRAINER_IMG,  (128, 156))

	name = POKEBALLS_COUNTER_2.render(str("Name"), 1, BLACK)
	WIN.blit(name, (500, 75))
	name = POKEBALLS_COUNTER.render(str(variables["TRAINER"]["NAME"]).capitalize(), 1, WHITE)
	WIN.blit(name, (500, 110))

	wallet = POKEBALLS_COUNTER_2.render(str("Wallet"), 1, BLACK)
	WIN.blit(wallet, (500, 160))

	wallet = POKEBALLS_COUNTER.render(str(variables["TRAINER"]["POKECOINS"]) + "¥", 1, WHITE)
	WIN.blit(wallet, (500, 200))

	POKEBALL_ITEM =  pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "pokeball_item.png")), (30,30))

	if variables["TRAINER"]["POKEMON_1"]["NAME"] != "NONE" :
		WIN.blit(POKEBALL_ITEM, (500, 270))

	if variables["TRAINER"]["POKEMON_2"]["NAME"] != "NONE" :
		WIN.blit(POKEBALL_ITEM, (535, 270))

	if variables["TRAINER"]["POKEMON_3"]["NAME"] != "NONE" :
		WIN.blit(POKEBALL_ITEM, (570, 270))



	WIN.blit(TRAINER_IMG, (295, 95))
	WIN.blit(PAUSE_MENU_IMG, (230,320))
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	pygame.display.update()


def create_bag_objects_screen () :
	potions_a = variables["TRAINER"]["TRAINER_BAG"]["POTIONS_AVAILABLE"]
	pokeballs_a = variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_AVAILABLE"]
	revives_a = variables["TRAINER"]["TRAINER_BAG"]["REVIVES_AVAILABLE"]

	potions_m = variables["TRAINER"]["TRAINER_BAG"]["POTIONS_MAX"]
	pokeballs_m = variables["TRAINER"]["TRAINER_BAG"]["POKEBALLS_MAX"]
	revives_m = variables["TRAINER"]["TRAINER_BAG"]["REVIVES_MAX"]

	WIN.blit(POKEMON_BAG_IMG, (175,-10))

	# ---- Potions ----

	potions_photo = pygame.transform.scale(potions_IMG, (55,62))
	WIN.blit(potions_photo, (345, 23))

	potions_str = POKEBALLS_COUNTER.render("Potions", 1, WHITE)
	WIN.blit(potions_str, (440, 15))

	potions_available = POKEBALLS_COUNTER.render("" + str(potions_a), 1, WHITE)
	WIN.blit(potions_available, (450, 60))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 60))

	potions_max = POKEBALLS_COUNTER.render("" + str(potions_m), 1, WHITE)
	WIN.blit(potions_max, (510, 60))


	# ---- Pokeballs ----

	pokeballs_photo = pygame.transform.scale(POKEBALL_IMG, (55,62))
	WIN.blit(pokeballs_photo, (345, 140))

	pokeballs_str = POKEBALLS_COUNTER.render("Pokeballs", 1, WHITE)
	WIN.blit(pokeballs_str, (440, 128))

	pokeballs_available = POKEBALLS_COUNTER.render("" + str(pokeballs_a), 1, WHITE)
	WIN.blit(pokeballs_available, (450, 170))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 170))

	pokeballs_max = POKEBALLS_COUNTER.render("" + str(pokeballs_m), 1, WHITE)
	WIN.blit(pokeballs_max, (510, 170))

	# ---- Revives ----

	revives_photo = pygame.transform.scale(revives_IMG, (55,62))
	WIN.blit(revives_photo, (345, 255))

	revives_str = POKEBALLS_COUNTER.render("Revives", 1, WHITE)
	WIN.blit(revives_str, (440, 240))

	revives_available = POKEBALLS_COUNTER.render("" + str(revives_a), 1, WHITE)
	WIN.blit(revives_available, (450, 280))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 280))

	revives_max = POKEBALLS_COUNTER.render("" + str(revives_m), 1, WHITE)
	WIN.blit(revives_max, (510, 280))

	pygame.display.update()


def create_bag_screen() :

	if variables["TRAINER"]["POKEMON_1"]["NAME"] !="NONE" :
		pokemon_1_name = variables["TRAINER"]["POKEMON_1"]["NAME"]
		pokemon_1_level =  variables["TRAINER"]["POKEMON_1"]["LEVEL"]
		pokemon_1_hp =  variables["TRAINER"]["POKEMON_1"]["HP"]
		pokemon_1_hp_base =  variables["TRAINER"]["POKEMON_1"]["BASE_HP"]
		pokemon_1_photo = pokemonPhoto[pokemon_1_name]

	else :
		pokemon_1_name = ""
		pokemon_1_level = ""
		pokemon_1_hp = 0
		pokemon_1_hp_base = 0
		pokemon_1_photo =  pokemonPhoto["DEFAULT"]

	if variables["TRAINER"]["POKEMON_2"]["NAME"] !="NONE" :
		pokemon_2_name = variables["TRAINER"]["POKEMON_2"]["NAME"]
		pokemon_2_level =  variables["TRAINER"]["POKEMON_2"]["LEVEL"]
		pokemon_2_hp =  variables["TRAINER"]["POKEMON_2"]["HP"]
		pokemon_2_hp_base =  variables["TRAINER"]["POKEMON_2"]["BASE_HP"]
		pokemon_2_photo = pokemonPhoto[pokemon_2_name]

	else :
		pokemon_2_name = "unknown"
		pokemon_2_level = ""
		pokemon_2_hp = 0
		pokemon_2_hp_base =  0
		pokemon_2_photo =  pokemonPhoto["DEFAULT"]

	if variables["TRAINER"]["POKEMON_3"]["NAME"] !="NONE" :
		pokemon_3_name = variables["TRAINER"]["POKEMON_3"]["NAME"]
		pokemon_3_level =  variables["TRAINER"]["POKEMON_3"]["LEVEL"]
		pokemon_3_hp =  variables["TRAINER"]["POKEMON_3"]["HP"]
		pokemon_3_hp_base =  variables["TRAINER"]["POKEMON_3"]["BASE_HP"]
		pokemon_3_photo = pokemonPhoto[pokemon_3_name]

	else :
		pokemon_3_name = "unknown"
		pokemon_3_level = ""
		pokemon_3_hp = 0
		pokemon_3_hp_base = 0
		pokemon_3_photo =  pokemonPhoto["DEFAULT"]

	WIN.blit(POKEMON_BAG_IMG, (175,-10))

	# First Pokemon Slot

	pokemon_1_name = DIALOG_MINI_FONT.render("" + str(pokemon_1_name), 1, WHITE)
	WIN.blit(pokemon_1_name, (440, 20))

	pokemon_1_hp = POKEBALLS_COUNTER.render("" + str(pokemon_1_hp), 1, WHITE)
	WIN.blit(pokemon_1_hp, (450, 60))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 60))

	pokemon_1_hp_base = POKEBALLS_COUNTER.render("" + str(pokemon_1_hp_base), 1, WHITE)
	WIN.blit(pokemon_1_hp_base, (510, 60))

	pokemon_1_photo = pygame.transform.scale(pokemon_1_photo, (70,70))
	WIN.blit(pokemon_1_photo, (345, 20))

	# Second Pokemon Slot

	pokemon_2_name = DIALOG_MINI_FONT.render("" + str(pokemon_2_name), 1, WHITE)
	WIN.blit(pokemon_2_name, (440, 135))

	pokemon_2_hp = POKEBALLS_COUNTER.render("" + str(pokemon_2_hp), 1, WHITE)
	WIN.blit(pokemon_2_hp, (450, 170))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 170))

	pokemon_2_hp_base = POKEBALLS_COUNTER.render("" + str(pokemon_2_hp_base), 1, WHITE)
	WIN.blit(pokemon_2_hp_base, (510, 170))

	pokemon_2_photo = pygame.transform.scale(pokemon_2_photo, (55,62))
	WIN.blit(pokemon_2_photo, (348, 140))

	# Third Pokemon Slot

	pokemon_3_name = DIALOG_MINI_FONT.render("" + str(pokemon_3_name), 1, WHITE)
	WIN.blit(pokemon_3_name, (440, 245))

	pokemon_3_hp = POKEBALLS_COUNTER.render("" + str(pokemon_3_hp), 1, WHITE)
	WIN.blit(pokemon_3_hp, (450, 280))

	separator = POKEBALLS_COUNTER.render("/", 1, WHITE)
	WIN.blit(separator, (490, 280))

	pokemon_3_hp_base = POKEBALLS_COUNTER.render("" + str(pokemon_3_hp_base), 1, WHITE)
	WIN.blit(pokemon_3_hp_base, (510, 280))

	pokemon_3_photo = pygame.transform.scale(pokemon_3_photo, (55,62))
	WIN.blit(pokemon_3_photo, (345, 255))

	pygame.display.update()


def pokemon_bag () :
	exit = False


	while not exit :
		create_bag_screen()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_BACKSPACE:
					exit = True


def pokemon_bag_objects () :
	exit = False


	while not exit :
		create_bag_objects_screen()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_BACKSPACE:
					exit = True


def pause_menu (cursor, pause) :
	exit = False
	cursor_pos.x = 300
	cursor_pos.y = 320


	while not exit :
		create_pause_menu()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_BACKSPACE:
					exit = True

				if cursor_pos.x == 300 and event.key == pygame.K_SPACE:
					pokemon_bag()

				if cursor_pos.x == 600  and event.key == pygame.K_SPACE :
					save_game()

				if cursor_pos.x == 450  and event.key == pygame.K_SPACE :
					pokemon_bag_objects()


				if event.key == pygame.K_RIGHT  and cursor_pos.x < 600 :
					cursor_pos.x += 150

				if cursor_pos.x > 300 and event.key == pygame.K_LEFT:
					cursor_pos.x -=150
