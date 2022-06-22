from resources import *
from save_game import *

def check_farm_threads () :
	variables["THREADS"]["FARM"] = "NO"
	silent_save_game()


def check_farm_inside_thread() :
	variables["THREADS"]["FARM_INSIDE"] = "NO"
	silent_save_game()

def create_bottle_animation () :

	while variables["THREADS"]["FARM"]  == "NO":

		# Bottle middle
		create_mumu_animation(MUMU_FARM_LOGO_IMG, MUMU_FARM_BOTTLE_MIDDLE_IMG)

		# Bottle left
		create_mumu_animation(MUMU_FARM_LOGO_IMG, MUMU_FARM_BOTTLE_LEFT_IMG)

		# Bottle right
		create_mumu_animation(MUMU_FARM_LOGO_IMG, MUMU_FARM_BOTTLE_RIGHT_IMG)

	

def create_mumu_animation (LOGO_MILTANK, MILTANK_BOTTLE) :
	# Sets background color
	WIN.blit(MUMU_FARM_OPENING_IMG, (0,0))

	# Display first title font
	start = TITLE_FONT.render("Welcome to", 1, WHITE)
	WIN.blit(start, (300, 20))
	clock.tick(20)

	# Display second title font
	start = TITLE_FONT.render("Moomoo Farm", 1, WHITE)
	WIN.blit(start, (320, 320))
	clock.tick(20)

	# Display Miltank logo
	WIN.blit(LOGO_MILTANK, (350, 100))

	# Enter message
	start = POKEBALLS_COUNTER_2.render("Press SPACE to enter", 1, WHITE)
	WIN.blit(start, (320, 450))
	clock.tick(20)

	# Show the miltank bottles in movement

	# Bottle left
	WIN.blit(MILTANK_BOTTLE, (50, 250))
	clock.tick(15)

	# Bottle right
	WIN.blit(MILTANK_BOTTLE, (700, 250))
	clock.tick(15)

	pygame.display.update()


def create_farm_background () :

	lucky_x = random.randint(50, 800)
	lucky_y = random.randint(300, 350)
	FARM_SOUND.play()

	while variables["THREADS"]["FARM_INSIDE"] == "NO" :

		create_background(SHOPPING_CLOUD_BOTTOM_IMG ,CLOUDS_ONE,lucky_x, lucky_y, STARS_ONE)
		create_background(SHOPPING_CLOUD_MIDDLE_IMG ,CLOUDS_TWO,lucky_x, lucky_y, STARS_TWO)
		create_background(SHOPPING_CLOUD_TOP_IMG ,CLOUDS_THREE,lucky_x, lucky_y, STARS_THREE)
		create_background(SHOPPING_CLOUD_TOP_IMG,CLOUDS_FOUR,lucky_x, lucky_y, STARS_THREE)


def create_background (CLOUD_DAY, CLOUD_NIGHT, lucky_x, lucky_y, STARS) :

	now = datetime.now()
	hora = now.strftime("%H")

	if hora <="16" and hora >="10" :
		WIN.blit(MUMU_FARM_BACKGROUND, (0,0)) # Place background image
		WIN.blit(CLOUD_DAY, (500, 10))
		clock.tick(1)
		WIN.blit(CLOUD_DAY, (-20, -20))
		clock.tick(1)

	elif hora >="17" and hora <"20":
		WIN.blit(MUMU_FARM_BACKGROUND_AFTERNOON, (0,0)) # Place background image

		WIN.blit(CLOUD_NIGHT, (20, -60))
		clock.tick(1)
		clock.tick(1)
		

	else:
		WIN.blit(MUMU_FARM_BACKGROUND_NIGHT, (0,0)) # Place background image
		WIN.blit(STARS, (0, 10))
		WIN.blit(STARS, (250, 10))
		WIN.blit(STARS, (500, 10))

		WIN.blit(CLOUD_NIGHT, (20, -60))
		clock.tick(1)
		clock.tick(1)

	WIN.blit(MILTANK_ASSET, (lucky_x, lucky_y))
	
	pygame.display.update()


def create_mumu_animation_keyboard () :

	while variables["THREADS"]["FARM"]  == "NO":

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE:
					PRESS_A_SOUND.play()
					variables["THREADS"]["FARM"] = "YES"
					silent_save_game()


def create_farm_control () :

	while variables["THREADS"]["FARM_INSIDE"]  == "NO":

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE:
					PRESS_A_SOUND.play()
					variables["THREADS"]["FARM_INSIDE"] = "YES"
					silent_save_game()