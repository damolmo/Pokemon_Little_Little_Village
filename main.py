# Pokemon Pi
# Fan Game powered by Python and Pygame
# Credits to Pygame for the libs

# First block of code
# Includes the imports and dependencies that this project use

#-------------------------------------------------------------------------------
import os
from random import randint
import random
import json

os.system("pip3 install wget")
os.system("pip3 install pygame")
os.system("pip install pygame")
os.system("pip3.10 install pygame")

import pygame
import time
from datetime import date
from datetime import datetime
import os.path
import platform
import zipfile
from zipfile import ZipFile
import wget 

pygame.font.init() # Import font
pygame.mixer.init() # Import sounds

#-----------------------------------

# Game Resources Imports
from resources import *
from bag import *
from save_game import *
from resources import *
from home import *
from shopping import access_shopping_area
from center import access_center

# ----------------------------------------

class System_Files_Check :

	def download_assets() :
		package = wget.download("https://github.com/daviiid99/Pokemon-Pi/raw/main/Assets.zip", "Assets.zip") #Download the platform-tools-latest-linux.zip from Google server

		with ZipFile("Assets.zip") as zipObj:
			zipObj.extractall()

		if platform.system() == "Linux" :
			os.system("rm Assets.zip ")

		else :
			os.system("del /f Assets.zip ")

	def check_Assets_Exist() :
		exists = False
		if os.path.exists("Assets") :
			exists = True

		else :
			System_Files_Check.download_assets()

	def download_save() :
		package = wget.download("https://github.com/daviiid99/Pokemon-Pi/raw/main/save.json", "save.json") #Download the platform-tools-latest-linux.zip from Google server


	def check_Save_Exist() :
		exists = False
		if os.path.exists("save.json") :
			exists = True

		else :
			System_Files_Check.download_save()

System_Files_Check.check_Assets_Exist()
System_Files_Check.check_Save_Exist()

#-------------------------------------------------------------------------------

# Main functions
# The following functions loads the title screen, the initial character creation and the main function

# ------------------------------------------------------------------------------


def create_title_screen() :

	now = datetime.now()
	hora = now.strftime("%H")

	if hora <="16" and hora >="10" :
		WIN.blit(TITLE_SCREEN_DAY_IMG, (0,0)) # Place background image
		
	elif hora >="17" and hora <"20":
		WIN.blit(TITLE_SCREEN_AFTERNOON_IMG, (0,0)) # Place background image
	
	elif hora >= "00" and hora <"06" :
		WIN.blit(TITLE_SCREEN_EVENING_IMG, (0,0)) # Place background image

	elif hora >= "06" and hora <"10" :
		WIN.blit(TITLE_SCREEN_DAY_IMG, (0,0)) # Place background image

	else :
		WIN.blit(TITLE_SCREEN_EVENING_IMG, (0,0)) # Place background image
	
	WIN.blit(TITLE_LOGO_IMG, (250,0)) # Place background image

	start = TITLE_FONT.render("Press (A) to Start", 1, WHITE)
	WIN.blit(start, (240, 370))

	version = DIALOG_MINI_FONT.render("v11.0 Alpha", 1, WHITE)
	WIN.blit(version, (10, 10))

	year = DIALOG_MINI_FONT.render("©2022", 1, WHITE)
	WIN.blit(year, (830, 10))


	pygame.display.update()



def welcome() :
	start = False
	BACKGROUND_SOUND.play()

	while not start :
		create_title_screen()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_a:
					PRESS_A_SOUND.play()
					start = True
					if variables["TRAINER"]["CHARACTER"] == "NONE" :
						choose_character()

					elif variables["TRAINER"]["CHARACTER"] == "ASH" :
						isAsh = True
						isMisty = False
						main (isAsh, isMisty)

					elif variables["TRAINER"]["CHARACTER"] == "MISTY" :
						isAsh = False
						isMisty = True
						main (isAsh, isMisty)


def choose_character () :
	BACKGROUND_SOUND.stop()
	OPENING_SOUND.play()
	start = False
	isMisty = False
	isAsh = False

	while not start :
		create_character_choooser (cursor_menu.x, cursor_menu.y)

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :

				if cursor_menu.x == 120 and event.key == pygame.K_SPACE :
					PRESS_A_SOUND.play()
					isAsh = True
					start = True
					variables["TRAINER"]["CHARACTER"] = "ASH"
					save_game()
					enter_name(isAsh, isMisty)

				if cursor_menu.x == 470 and event.key == pygame.K_SPACE :
					PRESS_A_SOUND.play()
					isMisty = True
					start = True
					variables["TRAINER"]["CHARACTER"] = "MISTY"
					save_game()
					enter_name(isAsh, isMisty)

				if event.key == pygame.K_RIGHT and cursor_menu.x == 120 :
					cursor_menu.x += 350

				if event.key == pygame.K_LEFT and cursor_menu.x == 470 :
					cursor_menu.x -= 350


def enter_name (isAsh, isMisty) :
	typing = True
	font = pygame.font.Font(None, 100)
	color_inactive = pygame.Color('grey')
	color_active = pygame.Color('white')
	color = color_inactive
	active = False
	text = 'Type here your name'
	done = False

	while typing :

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_box.collidepoint(event.pos):
					active = not active
				else:
					active = False

			if event.type == pygame.KEYDOWN:
				if active:
					if text == 'Type here your name' :
						text = ''
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1]
					else:
						text += event.unicode

					if event.key == pygame.K_RETURN :
						text = text[:-1]
						variables["TRAINER"]["NAME"] = text
						save_game()
						active = False
						typing = False

						rules = True

						while rules :
							create_rules_menu()
							for event in pygame.event.get() :
								if event.type == pygame.KEYDOWN:
									if event.key == pygame.K_SPACE :
										rules = False

						main(isAsh, isMisty)

		WIN.fill((30, 30, 30))
		# Render the current text.
		txt_surface = font.render(text, True, color)
		# Resize the box if the text is too long.
		width = max(200, txt_surface.get_width()+10)
		input_box.w = width
		# Blit the text.
		WIN.blit(txt_surface, (input_box.x+5, input_box.y+5))
		# Blit the input_box rect.
		pygame.draw.rect(WIN, color, input_box, 2)
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("Enter your name", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		if text !=  'Type here your name' :
			oak_phrase = POKEBALLS_COUNTER.render("Press (ENTER) to continue", 1, WHITE)
			WIN.blit(oak_phrase, (50, 400))

		pygame.display.update()
		clock.tick(30)

def create_character_choooser (x, y) :
	WIN.blit(MAIN_MENU_IMG, (0,0))
	WIN.blit(CURSOR_MENU, (x, y))
	character = POKEBALLS_COUNTER.render("" + str("Choose your character"), 1, WHITE)
	WIN.blit(character, (290, 400))
	pygame.display.update()

def create_rules_menu () :
	WIN.blit(RULES_MENU_IMG, (0,0))
	exit = POKEBALLS_COUNTER.render("" + str("Press SPACE to exit"), 1, WHITE)
	WIN.blit(exit, (330, 450))
	pygame.display.update()
			

## The main function
## Part of the game logic resides on it, including the initial screen and wild pokemon encounter

#-------------------------------------------------------------------------------

def main (isAsh, isMisty): ## Main function
	TOWN.stop()
	OAK_THEME.stop()
	BACKGROUND_SOUND.stop()
	OPENING_SOUND.stop()
	HOUSE_SOUND.stop()
	trainer_pokeballs = []
	free_monster = []
	pokeballs = 5
	free_pika = 0
	pressed = True
	oakMessage = False
	pause = -1
	VEL = 3

	clock = pygame.time.Clock()
	run = True

	if isAsh :
		TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/down', "ash.png")), (trainer_size.width, trainer_size.height))

	else :
		TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/down', "misty_down.png")), (trainer_size.width, trainer_size.height))

	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	while run :
		pause = 0
		clock.tick(FPS)

		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_p and len(trainer_pokeballs) < MAX_POKEBALL:
					free_pika = pokeball_out(trainer_pokeballs, free_pika)
					PIKACHU_SOUND.play()

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				if isAsh :
					TRAINER_IMG = ASH_LEFT_IMG
				else :
					TRAINER_IMG = MISTY_LEFT_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_UP]:
				message = daily_rewards()
				if message != "NONE" :
					create_reward_window(message)
					time.sleep(5)
					access_reward_calendar()

				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
				message = daily_rewards()
				if message != "NONE" :
					create_reward_window(message)
					time.sleep(5)
					access_reward_calendar()

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)


			if keys[pygame.K_a]:
				if isAsh :
					TRAINER_IMG = ASH_BICICLE_LEFT_IMG	
				else :
					TRAINER_IMG = MISTY_BICICLE_LEFT_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG , free_pika, oakMessage, pause, VEL)
				
			if keys[pygame.K_d]:
				if isAsh :
					TRAINER_IMG = ASH_BICICLE_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_BICICLE_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_w]:
				if isAsh :
					TRAINER_IMG = ASH_BICICLE_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BICICLE_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_s]:
				if isAsh :
					TRAINER_IMG = ASH_BICICLE_IMG
				else :
					TRAINER_IMG = MISTY_BICICLE_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs , PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_e]:
				BACKGROUND_SOUND.stop()
				save_game()
				welcome()

			if keys[pygame.K_g]:
				access_reward_calendar()

			if keys[pygame.K_x]:
				pause += 1
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs , PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				pause_menu(cursor_pause, pause)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1
						create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs , PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1
						create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs , PIKACHU_IMG, free_pika, oakMessage, pause, VEL)


		BACKGROUND_SOUND.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement(keys_pressed, pokemon_trainer, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

		keys = pygame.key.get_pressed()

		if pokemon_trainer.colliderect(HOUSE_1_DOOR) :
			if keys[pygame.K_SPACE]:
				BACKGROUND_SOUND.stop()
				SCAPE_SOUND.play()
				run = False
				inside = True
				before_enter_house_x = pokemon_trainer.x
				before_enter_house_y = pokemon_trainer.y
				access_laboratory(pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty, free_pika)

		elif pokemon_trainer.colliderect(HOUSE_2_DOOR) :
			if keys[pygame.K_SPACE]:
				BACKGROUND_SOUND.stop()
				SCAPE_SOUND.play()
				run = False
				inside = True
				before_enter_house_x = pokemon_trainer.x
				before_enter_house_y = pokemon_trainer.y
				access_house(pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty)

		elif pokemon_trainer.colliderect(SHOP_RECTANGLE_MAP):
			BACKGROUND_SOUND.stop()
			SCAPE_SOUND.play()
			run = False
			inside = True
			before_enter_house_x = pokemon_trainer.x
			before_enter_house_y = pokemon_trainer.y
			access_shopping_area(pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty)

	main(isAsh, isMisty)
#-------------------------------------------------------------------------------

if __name__ == "__main__":

	welcome()

