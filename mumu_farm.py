from resources import *
from save_game import *

def check_farm_threads () :
	variables["THREADS"]["FARM"] = "NO"
	silent_save_game()

def create_bottle_animation () :

	while variables["THREADS"]["FARM"]  == "NO":

		MILTANK_SOUND.play()

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