# Pokemon Pi
# Fan Game powered by Python and Pygame
# Credits to Pygame for the libs

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


class Player :

	def __init__(self, width, height) :
		self.width = width
		self.height = height

trainer_size = Player(64,76)


## Game Values
FPS = 60
VEL = 3
VEL_CURSOR = 50
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,204)
GREY = (25,25,25)
GREEN = (0, 204, 102)
today = date.today()
fecha = today.strftime("%B %d, %Y")
now = datetime.now()
hora = now.strftime("%H")
hora_str = now.strftime("%H:%M")
free_pika = 0

## App icon
icon = pygame.image.load('Assets/items/pokeball.png')
pygame.display.set_icon(icon)

# Player values
my_save_slot = open("save.json")
variables = json.load(my_save_slot)

## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pokémon Little Little Village")

## Map elements
HOUSE_1 = pygame.Rect(650, 20, 220, 250)
input_box = pygame.Rect(100, 50, 700, 100)

# Outside Rect
HOUSE_1_DOOR = pygame.Rect(770, 250, 50, 50)
HOUSE_2 = pygame.Rect(90, 0, 280, 180)
HOUSE_3 = pygame.Rect(500, 200, 280, 180)
HOUSE_2_DOOR = pygame.Rect(260, 135, 50, 50)
TREE_1 = pygame.Rect(500, 140, 120, 120)
TREE_2 = pygame.Rect(230, 280, 120, 120)
GRASS_ZONE_SOUTH = pygame.Rect(320, 400, 500, 120)
GRASS_ZONE_SOUTH_2 = pygame.Rect(0, 274, 250, 250)
GRASS_ZONE_WEST = pygame.Rect(0, 0, 80, 250)
GRASS_ZONE_EAST = pygame.Rect(500, 0, 130, 130)

# Trainer House Rect
TRAINER_HOUSE_DOOR = pygame.Rect(810, 200, 100, 100)
TRAINER_HOUSE_WALL = pygame.Rect(0, 0, 855, 100)
TRAINER_HOUSE_LIMIT_1 = pygame.Rect(865, 0, 30, 300)
TRAINER_HOUSE_LIMIT_2 = pygame.Rect(500, 350, 400, 150)
TRAINER_HOUSE_TV =  pygame.Rect(260, 80, 150, 80)
TRAINER_HOUSE_BOOKS = pygame.Rect(520, 65, 85, 80)
#TRAINER_HOUSE_DESK =
TRAINER_HOUSE_CONSOLE = pygame.Rect(300, 170, 80, 50)
#TRAINER_HOUSE_DESK_CHAIR =
TRAINER_HOUSE_ESTANTERIA = pygame.Rect(5, 90, 120, 80)
TRAINER_HOUSE_BED = pygame.Rect(0, 380, 220, 140)
OAK_RECTANGLE = pygame.Rect(310, 120, 50, 80)
OAK_DOOR = pygame.Rect(400, 480, 78, 36)
OAK_TABLE = pygame.Rect(590, 290, 140, 40)

# Oaks Lab Table
OAK_POKEBALL_1 = pygame.Rect(590, 300, 40, 60)
OAK_POKEBALL_2 = pygame.Rect(640, 300, 40, 60)
OAK_POKEBALL_3 = pygame.Rect(690, 300, 40, 60)

# Shopping area rect
OAK_RECTANGLE_MAP = pygame.Rect(400, -10, 50, 70)
SHOP_RECTANGLE_MAP = pygame.Rect(400, -20, 50, 70)
HOME_RECT_MAP = pygame.Rect(0, 400, 100, 100)

POKEMON_CENTER_RECT = pygame.Rect(100, 100, 300, 220)
SHOP_RECT =  pygame.Rect(520, 100, 250, 220)
ESTANQUE_RECT =  pygame.Rect(430, 200, 100, 100)

TREES_RECT_WEST = pygame.Rect(0, 0, 100, 300)
TREES_RECT_EAST = pygame.Rect(800, 0, 100, 300)

SHOP_DOOR_RECT = pygame.Rect(590, 270, 70, 70)
CENTER_DOOR_RECT =  pygame.Rect(230, 280, 70, 50)

# Shop rect
MACETA_SURESTE_RECT = pygame.Rect(20, 400, 100, 200)
MACETA_SUROESTE_RECT = pygame.Rect(800, 320, 100, 200)
MACETA_NORTE_RECT = pygame.Rect(800, 50, 100, 200)
MOSTRADOR_RECT = pygame.Rect(0, 150, 190, 180)
PUERTA_RECT = pygame.Rect(220, 450, 100, 60)
MESA_RECT = pygame.Rect(450, 350, 230, 50)
ESTANTERIA_CENTRO_1 = pygame.Rect(340, 240, 130, 70)
#ESTANTERIA_CENTRO_2 = pygame.Rect(420, 240, 130, 70)
ESTANTERIA_CENTRO_3 =pygame.Rect(595, 245, 125, 70)
ESTANTERIA_NORTE_1 = pygame.Rect(200, 10, 120, 120)
ESTANTERIA_NORTE_2 = pygame.Rect(350, 10, 120, 120)
ESTANTERIA_NORTE_3 = pygame.Rect(500, 0, 300, 75)

SHOP_DEPENDENT_RECT =  pygame.Rect(150, 120, 60, 100)
DEPENDENT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/shop_dependent', "dependent.png")), (trainer_size.width, trainer_size.height))



## Game Events
THROW_POKEBALL = pygame.USEREVENT +1
clock = pygame.time.Clock()

## Assets

# Pikachu de Ash
## Walking
# --- Down Position ---
ASH_PIKACHU_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/down', "pikachu_friend.png")), (trainer_size.width, trainer_size.height))
ASH_PIKACHU_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/down', "pikachu_friend_2.png")), (trainer_size.width, trainer_size.height))

# --- Left Position ---
ASH_PIKACHU_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/left', "pikachu_friend_left.png")), (trainer_size.width, trainer_size.height))
ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/left', "pikachu_friend_left_2.png")), (trainer_size.width, trainer_size.height))

# --- Right Position ---
ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/right', "pikachu_friend_right.png")), (trainer_size.width, trainer_size.height))
ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/right', "pikachu_friend_right_2.png")), (trainer_size.width, trainer_size.height))

# --- Up Position ---
ASH_PIKACHU_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/up', "pikachu_friend_back.png")), (trainer_size.width, trainer_size.height))
ASH_PIKACHU_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/pikachu/up', "pikachu_friend_back_2.png")), (trainer_size.width, trainer_size.height))


# Trainer
pokemon_trainer = pygame.Rect(450, 253, trainer_size.width, trainer_size.height) # Defines player coords
pikachu_trainer = pygame.Rect(450, 253, trainer_size.width, trainer_size.height) # Defines player coords
previous_x, previous_y = 500, 300
x_change, y_change = 450, 253
previous_pi_x, previous_pi_y= 450, 253

# Ash
## Walking
# --- Down Position ---
ASH_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/down', "ash.png")), (trainer_size.width, trainer_size.height))
ASH_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/down', "ash_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/down', "ash_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Left Position ---
ASH_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/left', "ash_left.png")), (trainer_size.width, trainer_size.height))
ASH_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/left', "ash_left_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/left', "ash_left_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Right Position ---
ASH_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/right', "ash_right.png")), (trainer_size.width, trainer_size.height))
ASH_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/right', "ash_right_right_foot.png")), (trainer_size.width, trainer_size.height))
ASH_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/right', "ash_right_left_foot.png")), (trainer_size.width, trainer_size.height))

# --- Up Position ---
ASH_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/up', "ash_back.png")), (trainer_size.width, trainer_size.height))
ASH_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/up', "ash_back_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/walking/up', "ash_back_right_foot.png")), (trainer_size.width, trainer_size.height))


## Bicicle
# --- Down Position ---
ASH_BICICLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/down', "ash_bicicle.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/down', "ash_bicicle_left.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/down', "ash_bicicle_right.png")), (trainer_size.width, trainer_size.height))

# --- Left Position ---
ASH_BICICLE_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/left', "ash_bicicle_left_foots.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/left', "ash_bicicle_left_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/left', "ash_bicicle_left_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Right Position ---
ASH_BICICLE_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/right', "ash_bicicle_right_foots.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/right', "ash_bicicle_right_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/right', "ash_bicicle_right_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Up Position ---
ASH_BICICLE_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/up', "ash_bicicle_back_foots.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/up', "ash_bicicle_back_left_foot.png")), (trainer_size.width, trainer_size.height))
ASH_BICICLE_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/bicicle/up', "ash_bicicle_back_right_foot.png")), (trainer_size.width, trainer_size.height))



# Misty
## Walking
# --- Down Position ---
MISTY_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/down', "misty_down.png")), (trainer_size.width, trainer_size.height))
MISTY_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/down', "misty_down_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/down', "misty_down_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Left Position ---
MISTY_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/left', "misty_left.png")), (trainer_size.width, trainer_size.height))
MISTY_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/left', "misty_left_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/left', "misty_left_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Right Position ---
MISTY_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/right', "misty_right.png")), (trainer_size.width, trainer_size.height))
MISTY_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/right', "misty_right_right_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/right', "misty_right_left_foot.png")), (trainer_size.width, trainer_size.height))

# --- Up Position ---
MISTY_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/up', "misty_up.png")), (trainer_size.width, trainer_size.height))
MISTY_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/up', "misty_up_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/walking/up', "misty_up_right_foot.png")), (trainer_size.width, trainer_size.height))


## Bicicle
# --- Down Position ---
MISTY_BICICLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/down', "misty_bicicle.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/down', "misty_bicicle_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/down', "misty_bicicle_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Left Position ---
MISTY_BICICLE_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/left', "misty_bicicle_left.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/left', "misty_bicicle_left_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/left', "misty_bicicle_left_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Right Position ---
MISTY_BICICLE_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/right', "misty_bicicle_right.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/right', "misty_bicicle_right_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/right', "misty_bicicle_right_right_foot.png")), (trainer_size.width, trainer_size.height))

# --- Up Position ---
MISTY_BICICLE_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/up', "misty_bicicle_up.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/up', "misty_bicicle_up_left_foot.png")), (trainer_size.width, trainer_size.height))
MISTY_BICICLE_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/bicicle/up', "misty_bicicle_up_right_foot.png")), (trainer_size.width, trainer_size.height))



# NPCS
oak = pygame.Rect(450, 253, 74, 96) # Defines player coords
previous_oak_x, previous_oak_y = 300, 100

## Walking
# --- Down Position ---
OAK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/down', "oak_down.png")), (74, 96))
OAK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/down', "oak_down_left_foot.png")), (74, 96))
OAK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/down', "oak_down_right_foot.png")), (74, 96))

# --- Left Position ---
OAK_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/left', "oak_left.png")), (74, 96))
OAK_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/left', "oak_left_left_foot.png")), (74, 96))
OAK_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/left', "oak_left_right_foot.png")), (74, 96))

# --- Right Position ---
OAK_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/right', "oak_right.png")), (74, 96))
OAK_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/right', "oak_right_right_foot.png")), (74, 96))
OAK_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/right', "oak_right_left_foot.png")), (74, 96))

# --- Up Position ---
OAK_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/up', "oak_up.png")), (74, 96))
OAK_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/up', "oak_up_left_foot.png")), (74, 96))
OAK_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/oak/up', "oak_up_right_foot.png")), (74, 96))



### Pokemon


## Mr Mime

# Sound effect
MRMIME_SOUND = pygame.mixer.Sound("Assets/pokemon/mrmime/sound/mrmime.mp3")

# Sprites
MRMIME_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_00_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_01_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_02_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_03_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_04_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_05_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_06_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_07_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_08_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_09_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_10_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_11_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_12_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_13_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_14_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_15_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_16_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_17_delay-0.05s.gif")), (200, 200))
MRMIME_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/mrmime', "frame_18_delay-0.05s.gif")), (200, 200))


## Growlithe

# Sound effect
GROWLITHE_SOUND = pygame.mixer.Sound("Assets/pokemon/growlithe/sound/growlithe.mp3")

# Sprites
GROWLITHE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_00_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_01_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_02_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_03_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_04_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_05_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_06_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_07_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_08_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_09_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_10_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_11_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_12_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_13_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_14_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_15_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_16_delay-0.05s.gif")), (200, 200))
GROWLITHE_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/growlithe', "frame_17_delay-0.05s.gif")), (200, 200))


## Arcanine

# Sound effect
ARCANINE_SOUND = pygame.mixer.Sound("Assets/pokemon/arcanine/sound/arcanine.mp3")

# Sprites
ARCANINE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_00_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_01_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_02_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_03_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_04_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_05_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_06_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_07_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_08_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_09_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_10_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_11_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_12_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_13_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_14_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_15_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_16_delay-0.05s.gif")), (200, 200))
ARCANINE_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/arcanine', "frame_17_delay-0.05s.gif")), (200, 200))

## Pikachu

# Sound effect
PIKACHU_SOUND = pygame.mixer.Sound("Assets/pokemon/pikachu/sound/pikachu.mp3")

# Sprites
PIKACHU_IMG_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_00_delay-0.65s.gif")), (200, 200))
PIKACHU_IMG_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_01_delay-0.08s.gif")), (200, 200))
PIKACHU_IMG_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_02_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_03_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_04_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_05_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_06_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_07_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_9 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_08_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_09_delay-0.08s.gif")), (200, 200))
PIKACHU_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_10_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_11_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_12_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_13_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_14_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_15_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu', "frame_16_delay-0.05s.gif")), (200, 200))


## Squirtle

# Sound effect
SQUIRTLE_SOUND = pygame.mixer.Sound("Assets/pokemon/squirtle/sound/squirtle.mp3")

# Sprites
SQUIRTLE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_00_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_01_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_02_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_03_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_04_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_05_delay-0.02s.gif")), (200, 200))
SQUIRTLE_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_06_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_07_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_08_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_09_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_10_delay-0.08s.gif")), (200, 200))
SQUIRTLE_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_11_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_12_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_13_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_14_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_15_delay-0.53s.gif")), (200, 200))
SQUIRTLE_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_16_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_17_delay-0.07s.gif")), (200, 200))
SQUIRTLE_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_18_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_19_delay-0.12s.gif")), (200, 200))
SQUIRTLE_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_20_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_21_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_22_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_23_delay-0.12s.gif")), (200, 200))
SQUIRTLE_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_24_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_25_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_26_delay-0.06s.gif")), (200, 200))
SQUIRTLE_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_27_delay-0.09s.gif")), (200, 200))
SQUIRTLE_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_28_delay-0.06s.gif")), (200, 200))
SQUIRTLE_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_29_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_30_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle', "frame_31_delay-0.24s.gif")), (200, 200))


## Beedrill

# Sound effect
BEEDRILL_SOUND = pygame.mixer.Sound("Assets/pokemon/beedrill/sound/beedrill.mp3")

# Sprites
BEEDRILL_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_00_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_01_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_02_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_03_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_04_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_05_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_06_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_07_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_08_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_09_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_10_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_11_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_12_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_13_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_14_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_15_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_16_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_17_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_18_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_19_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_20_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_21_delay-0.1s.gif")), (200, 200))
BEEDRILL_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/beedrill', "frame_22_delay-0.1s.gif")), (200, 200))


# Sycther

# Sound effect
SCYTHER_SOUND = pygame.mixer.Sound("Assets/pokemon/scyther/sound/scyther.mp3")

# Sprites
SCYTHER_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_0_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_1_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_2_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_3_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_4_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_5_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_6_delay-0.08s.gif")), (200, 200))
SCYTHER_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/scyther', "frame_7_delay-0.08s.gif")), (200, 200))


# Charmander

# Sound effect
CHARMANDER_SOUND = pygame.mixer.Sound("Assets/pokemon/charmander/sound/charmander.mp3")

# Sprites
CHARMANDER_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_00_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_01_delay-0.11s.gif")), (200, 200))
CHARMANDER_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_02_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_03_delay-0.03s.gif")), (200, 200))
CHARMANDER_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_04_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_05_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_06_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_07_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_08_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_09_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_10_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_11_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_12_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_13_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_14_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_15_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_16_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_17_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_18_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_19_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_20_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_21_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_22_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_23_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_24_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_25_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_26_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_27_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_28_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_29_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_30_delay-0.03s.gif")), (200, 200))
CHARMANDER_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_31_delay-0.09s.gif")), (200, 200))
CHARMANDER_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_32_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_33_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_35 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_34_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_36 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_35_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_37 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_36_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_38 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_37_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_39 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_38_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_40 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_39_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_41 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_40_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_42 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_41_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_43 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_42_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_44 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_43_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_45 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_44_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_46 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_45_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_47 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_46_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_48 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_47_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_49 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_48_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_50 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_49_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_51 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_50_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_52 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_51_delay-0.09s.gif")), (200, 200))
CHARMANDER_IMG_53 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_52_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_54 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander', "frame_53_delay-0.06s.gif")), (200, 200))

## Bulbasaur

# Sound effect
BULBASAUR_SOUND = pygame.mixer.Sound("Assets/pokemon/bulbasaur/sound/bulbasaur.mp3")

# Sprites
BULBASAUR_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_00_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_01_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_02_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_03_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_04_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_05_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_06_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_07_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_08_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_09_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_10_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_11_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_12_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_13_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_14_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_15_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_16_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_17_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_18_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_19_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_20_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_21_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_22_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_23_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_24_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_25_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_26_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_27_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_28_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_29_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_30_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_31_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_32_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_33_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_35 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_34_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_36 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_35_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_37 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_36_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_38 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_37_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_39 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_38_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_40 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_39_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_41 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_40_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_42 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_41_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_43 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_42_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_44 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_43_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_45 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_44_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_46 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_45_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_47 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_46_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_48 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_47_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_49 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_48_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_50 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_49_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_51 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_50_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_52 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur', "frame_51_delay-0.07S.gif")), (200, 200))


## Psyduck

# Sound
PSYDUCK_SOUND = pygame.mixer.Sound("Assets/pokemon/psyduck/sound/psyduck.mp3")

# Sprites
PSYDUCK_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_00_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_01_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_02_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_03_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_04_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_05_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_06_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_07_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_08_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_09_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_10_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_11_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_12_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_13_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_14_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_15_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_16_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_17_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_18_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_19_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_20_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_21_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_22_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_23_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/psyduck', "frame_24_delay-0.09s.gif")), (200, 200))

## Gastly

# Sound
GASTLY_SOUND = pygame.mixer.Sound("Assets/pokemon/gastly/sound/gastly.mp3")

# Sprites
GASTLY_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_00_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_01_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_02_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_03_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_04_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_05_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_06_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_07_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_08_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_09_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_10_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_11_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_12_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_13_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_14_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_15_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_16_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gastly', "frame_17_delay-0.06s.gif")), (200, 200))

## Eevee

# Sound
EEVEE_SOUND = pygame.mixer.Sound("Assets/pokemon/eevee/sound/eevee.mp3")

# Sprites
EEVEE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_00_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_01_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_02_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_03_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_04_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_05_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_06_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_07_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_08_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_09_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_10_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_11_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_12_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_13_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_14_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_15_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_16_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_17_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_16_delay-0.1s.gif")), (200, 200))
EEVEE_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/eevee', "frame_17_delay-0.1s.gif")), (200, 200))


## Gengar

# Sound
GENGAR_SOUND = pygame.mixer.Sound("Assets/pokemon/gengar/sound/gengar.mp3")

# Sprites
GENGAR_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_00_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_01_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_02_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_03_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_04_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_05_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_06_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_07_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_08_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_09_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_10_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_11_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_12_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_13_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_14_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_15_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_16_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_17_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_18_delay-0.1s.gif")), (200, 200))
GENGAR_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/gengar', "frame_19_delay-0.1s.gif")), (200, 200))


## Meowth

# Sound
MEOWTH_SOUND = pygame.mixer.Sound("Assets/pokemon/meowth/sound/meowth.mp3")

# Sprites
MEOWTH_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_00_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_01_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_02_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_03_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_04_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_05_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_06_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_07_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_08_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_09_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_10_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_11_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_12_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_13_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_14_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_15_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_16_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_17_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_18_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_19_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_20_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_21_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_22_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/meowth', "frame_23_delay-0.08s.gif")), (200, 200))

## Umbreon

# Sound
UMBREON_SOUND = pygame.mixer.Sound("Assets/pokemon/umbreon/sound/umbreon.mp3")

# Sprites
UMBREON_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_02_delay-0.14s.png")), (270, 200))
UMBREON_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_03_delay-0.14s.png")), (270, 200))
UMBREON_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_04_delay-0.14s.png")), (270, 200))
UMBREON_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_05_delay-0.14s.png")), (270, 200))
UMBREON_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_06_delay-0.14s.png")), (270, 200))
UMBREON_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_07_delay-0.14s.png")), (270, 200))
UMBREON_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_08_delay-0.14s.png")), (270, 200))
UMBREON_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_09_delay-0.14s.png")), (270, 200))
UMBREON_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_11_delay-0.14s.png")), (270, 200))
UMBREON_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_12_delay-0.14s.png")), (270, 200))
UMBREON_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_13_delay-0.14s.png")), (270, 200))
UMBREON_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_14_delay-0.14s.png")), (270, 200))
UMBREON_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_15_delay-0.14s.png")), (270, 200))
UMBREON_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_16_delay-0.14s.png")), (270, 200))
UMBREON_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_17_delay-0.14s.png")), (270, 200))
UMBREON_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_18_delay-0.24s.png")), (270, 200))
UMBREON_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_19_delay-0.14s.png")), (270, 200))
UMBREON_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_20_delay-0.14s.png")), (270, 200))
UMBREON_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_21_delay-0.14s.png")), (270, 200))
UMBREON_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_22_delay-0.14s.png")), (270, 200))
UMBREON_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_23_delay-0.14s.png")), (270, 200))
UMBREON_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_24_delay-0.14s.png")), (270, 200))
UMBREON_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_25_delay-0.14s.png")), (270, 200))
UMBREON_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_26_delay-0.24s.png")), (270, 200))
UMBREON_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_27_delay-0.14s.png")), (270, 200))
UMBREON_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_28_delay-0.14s.png")), (270, 200))
UMBREON_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_29_delay-0.14s.png")), (270, 200))
UMBREON_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_30_delay-0.14s.png")), (270, 200))
UMBREON_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_31_delay-0.14s.png")), (270, 200))
UMBREON_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_32_delay-0.14s.png")), (270, 200))
UMBREON_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_33_delay-0.14s.png")), (270, 200))
UMBREON_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/umbreon', "frame_34_delay-0.1s.png")), (270, 200))

# Background
# Title Screen

# Map
TITLE_SCREEN_IMG = pygame.image.load(os.path.join('Assets/background/title_screen', "welcome.png"))
ROUTE_IMG = pygame.image.load(os.path.join('Assets/background/day', "background.png"))
ROUTE_IMG_2 = pygame.image.load(os.path.join('Assets/background/evening', "background_evening.png"))
ROUTE_IMG_3 = pygame.image.load(os.path.join('Assets/background/night', "background_night.png"))
ROUTE_IMG_4 = pygame.image.load(os.path.join('Assets/background/early_morning', "background.png"))
ROUTE_IMG_5 = pygame.image.load(os.path.join('Assets/background/early_day', "background.png"))


# Oask Laboratory
OAK_LABORATORY_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/laboratory', "oak_laboratory.png")), (900, 900))
OAK_LABORATORY_DOOR = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/laboratory', "oak_door.png")), (78, 36))
POKEBALL_CHOOSE = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/laboratory', "pokeball_choose.png")), (WIDTH, HEIGHT))
OAK_THEME = pygame.mixer.Sound("Assets/sounds/oak_theme.mp3")

# TRAINER ROOM
TRAINER_ROOM_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/trainer_house/day', "room_day.png")), (WIDTH, HEIGHT))
TRAINER_ROOM_NIGHT = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/trainer_house/night', "room_night.png")), (WIDTH, HEIGHT))

# Pause Menu
PAUSE_MENU_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/settings', "pause_menu.png")), (450, 200))
CLOCK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/clock', "clock.png")), (200, 100))
BAG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/clock', "bag.png")), (110, 70))
BACK_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/clock', "background.png")), (130, 130))
PIKA_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/clock', "background_down.png")), (130, 130))
SHOES_BG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/clock', "shoes.png")), (130, 130))




# Battle
# Background
BATTLE_ARENA_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/day', "battle_arena.png")), (WIDTH, HEIGHT))
MAIN_MENU_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/choose', "choose.png")), (WIDTH, HEIGHT))
POKEMON_BAG_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/pokemon_bag', "inventory.png")), (583, 361))
BATTLE_ARENA_NIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/night', "battle_arena_night.png")), (WIDTH, HEIGHT))
STARS = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle', "stars_background.jpg")), (WIDTH, HEIGHT))

# Trainer
# ASH
ASH_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/battle/', "ash_battle_1.png")), (300,300))
ASH_BATTLE_IMG_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/battle', "ash_battle_2.png")), (300,300))
ASH_BATTLE_IMG_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/battle', "ash_battle_3.png")), (300,300))
ASH_BATTLE_IMG_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/battle', "ash_battle_4.png")), (300,300))
ASH_BATTLE_IMG_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/ash/battle', "ash_battle_5.png")), (300,300))

# MISTY
MISTY_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/battle/', "misty_battle_1.png")), (300,600))
MISTY_BATTLE_IMG_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/battle', "misty_battle_2.png")), (300,600))
MISTY_BATTLE_IMG_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/trainer/misty/battle', "misty_battle_3.png")), (300,300))

# Pokemon
PIKACHU_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/pikachu/battle', "pikachu.png")), (300,300))
BULBASAUR_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/bulbasaur/battle', "bulbasaur.png")), (300,300))
SQUIRTLE_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/squirtle/battle', "squirtle.png")), (300,300))
CHARMANDER_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pokemon/charmander/battle', "charmander.png")), (300,300))

# Menu
BATTLE_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/battle', "menu.png")), (260,90))
DIALOG_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/dialog', "dialog.png")), (900,300))
RULES_MENU_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/settings', "map_menu.png")), (WIDTH,HEIGHT))
SHOPPING_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone', "shopping.png")), (WIDTH,HEIGHT))
SHOPPING_EVENING_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone', "shopping_evening.png")), (WIDTH,HEIGHT))
SHOPPING_NIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone', "shopping_night.png")), (WIDTH,HEIGHT))
SHOP_INSIDE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/shop', "shop.png")), (WIDTH,HEIGHT))

# Screen Dialog
BATTLE_DIALOG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/battle', "battle_dialog.png")), (WIDTH,130))

# Cursor
CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('Assets/cursor/battle', "cursor.png")), (100,100))
CURSOR_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets/cursor/menu', "main_menu_cursor.png")), (312,317))
CURSOR_PAUSE = pygame.transform.scale(pygame.image.load(os.path.join('Assets/cursor/menu', "pause_menu_cursor.png")), (30,35))
DEFAULT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "pokeball_icon.png")), (40,55))
potions_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "potion.png")), (40,55))
pokeballs_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "pokeball_icon.png")), (40,55))
revives_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "revive.png")), (40,55))

cursor_pos = pygame.Rect(620, 350, 100, 100) # Defines player coords
cursor_pause = pygame.Rect(700, 60, 20, 20) # Defines player coords
cursor_menu = pygame.Rect(120, 20, 300, 317)

# Life menu
LIFE_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/battle', "life_menu.png")), (250,62))
WILD_POKEMON = "unknown"

# Pokemon Bag Values
pokemonPhoto = {
				"PIKACHU": PIKACHU_IMG_1, 
				"SQUIRTLE" : SQUIRTLE_IMG_01, 
				"CHARMANDER" : CHARMANDER_IMG_01, 
				"BULBASAUR" : BULBASAUR_IMG_01, 
				"PSYDUCK" : PSYDUCK_IMG_01, 
				"MEOWTH" : MEOWTH_IMG_01,
				"UMBREON" : UMBREON_IMG_02,
				"GASTLY" : GASTLY_IMG_01,
				"GENGAR" : GENGAR_IMG_01,
				"DEFAULT" : DEFAULT_IMG
				}


# Battle opening
BATTLE_ARENA_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_1.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_2.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_3.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_4.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_5.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_6.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_7.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_8.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_9.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_10.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_11.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/battle/opening', "grass_12.gif")), (WIDTH, HEIGHT))


# Music
BACKGROUND_SOUND = pygame.mixer.Sound("Assets/sounds/music.mp3")
POKEMON_ENCOUNTER_SOUND = pygame.mixer.Sound("Assets/sounds/pokemon_encounter.mp3")
GRASS_SOUND = pygame.mixer.Sound("Assets/sounds/grass.mp3")
SCAPE_SOUND = pygame.mixer.Sound("Assets/sounds/scape.mp3")
WALL_SOUND = pygame.mixer.Sound("Assets/sounds/wall_bump.mp3")
PRESS_A_SOUND = pygame.mixer.Sound("Assets/sounds/press_a.mp3")
VICTORY = pygame.mixer.Sound("Assets/sounds/victory.mp3")
TOWN = pygame.mixer.Sound("Assets/sounds/town.mp3")
SHOP_SOUND =  pygame.mixer.Sound("Assets/sounds/shop_sound.mp3")
CENTER_SOUND = pygame.mixer.Sound("Assets/sounds/center_sound.mp3")



# Pokeball
POKEBALL_IMG = pygame.image.load(os.path.join('Assets/items', "pokeball.png"))
POKEBALL_ITEM = pygame.image.load(os.path.join('Assets/items', "pokeball_item.png"))
POKEBALL_SOUND = pygame.mixer.Sound("Assets/sounds/pokeball_out.mp3")
MAX_POKEBALL = 3
POKEBALL_VEL = 3
POKEBALL_ITEM.convert()

# Displat Fonts
WINNER_LOOSER_DIALOG = pygame.font.SysFont('comicsans', 80)
POKEBALLS_COUNTER = pygame.font.SysFont('comicsans', 30)
DIALOG_FONT = pygame.font.SysFont('comicsans', 26)
DIALOG_MINI_FONT = pygame.font.SysFont('comicsans', 18)
RULES = pygame.font.SysFont('comicsans', 16)


def save_game () :
	my_save_slot = json.dumps(variables)
	with open('save.json', 'w') as save:
		save.write(my_save_slot)


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
	if variables["POKEMON_1"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["POKEMON_1"]["NAME"].capitalize())  + "!"), 1, BLACK)

	elif variables["POKEMON_1"]["HP"] == 0 and variables["POKEMON_2"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["POKEMON_2"]["NAME"].capitalize())  + "!"), 1, BLACK)


	elif variables["POKEMON_1"]["HP"] == 0 and variables["POKEMON_2"]["HP"] == 0 and  variables["POKEMON_3"]["HP"] > 0 :
		dialog = DIALOG_FONT.render("" + str("Let's Go " +  str(variables["POKEMON_3"]["NAME"].capitalize())  + "!"), 1, BLACK)

	WIN.blit(dialog, (50, 460))

	# Display Wild Pokemon Name
	date = RULES.render("" + str(POKEMON_NAME), 1, BLACK)
	WIN.blit(date, (5, 35))


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

	if variables["POKEMON_1"]["HP"] > 0 :

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

	elif variables["POKEMON_1"]["HP"] == 0 :
		if variables["POKEMON_2"]["HP"] > 0 :

			if variables["POKEMON_2"]["NAME"] == "SQUIRTLE":
				WIN.blit(SQUIRTLE_BATTLE_IMG, (0,250))

			elif variables["POKEMON_2"]["NAME"] == "CHARMANDER":
					WIN.blit(CHARMANDER_BATTLE_IMG, (0,250))

			elif variables["POKEMON_2"]["NAME"] == "BULBASAUR":
					WIN.blit(BULBASAUR_BATTLE_IMG, (0,250))


			friend = RULES.render("" + str(variables["POKEMON_2"]["NAME"]), 1, BLACK)
			WIN.blit(friend, (5, 35))

			stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
			WIN.blit(stats, (12, 60))

			separator = RULES.render("/", 1, BLACK)
			WIN.blit(separator, (30, 60))

			stats = RULES.render("" + str(pokemonStaticHP), 1, BLACK)
			WIN.blit(stats, (40, 60))


			level = RULES.render("Lv " + str(variables["POKEMON_2"]["LEVEL"]), 1, BLACK)
			WIN.blit(level, (160, 35))

		elif variables["POKEMON_1"]["HP"] == 0 and variables["POKEMON_2"]["HP"] == 0 :
			if variables["POKEMON_3"]["HP"] > 0 :

				if variables["POKEMON_3"]["NAME"] == "SQUIRTLE":
					WIN.blit(SQUIRTLE_BATTLE_IMG, (0,250))

				elif variables["POKEMON_3"]["NAME"] == "CHARMANDER":
						WIN.blit(CHARMANDER_BATTLE_IMG, (0,250))

				elif variables["POKEMON_3"]["NAME"] == "BULBASAUR":
						WIN.blit(BULBASAUR_BATTLE_IMG, (0,250))


				friend = RULES.render("" + str(variables["POKEMON_3"]["NAME"]), 1, BLACK)
				WIN.blit(friend, (5, 35))

				stats = RULES.render("" + str(pokemonVariableHP) , 1, BLACK)
				WIN.blit(stats, (12, 60))

				separator = RULES.render("/", 1, BLACK)
				WIN.blit(separator, (30, 60))

				stats = RULES.render("" + str(pokemonStaticHP), 1, BLACK)
				WIN.blit(stats, (40, 60))


				level = RULES.render("Lv " + str(variables["POKEMON_3"]["LEVEL"]), 1, BLACK)
				WIN.blit(level, (160, 35))


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


def create_Bulbasaur(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :


	# Pokemon Sound

	if sound == 0:
		BULBASAUR_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(BULBASAUR_IMG_01, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_02, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_03, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_04, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_05, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_06, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_07, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_08, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_09, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_10, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_11, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_12, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_13, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_14, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_15, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_16, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_17, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_18, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_19, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_20, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_21, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_22, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_23, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_24, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_25, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_26, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_27, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_28, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_29, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_30, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_31, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_32, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_33, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_34, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_35, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_36, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_37, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_38, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_39, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_40, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_41, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_42, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_43, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_44, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_45, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_46, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_47, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_48, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_49, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_50, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_51, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BULBASAUR_IMG_52, "BULBASAUR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Charmander(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		CHARMANDER_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(CHARMANDER_IMG_01, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_02, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_03, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_04, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_05, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_06, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_07, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_08, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_09, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_10, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_11, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_12, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_13, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_14, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_15, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_16, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_17, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_18, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_19, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_20, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_21, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_22, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_23, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_24, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_25, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_26, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_27, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_28, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_29, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_30, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_31, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_32, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_33, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_34, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_35, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_36, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_37, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_38, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_39, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_40, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_41, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_42, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_43, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_44, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_45, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_46, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_47, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_48, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_49, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_50, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_51, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_52, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_53, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(CHARMANDER_IMG_54, "CHARMANDER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_MrMime(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		MRMIME_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(MRMIME_IMG_01, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_02, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_03, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_04, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_05, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_06, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_07, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_08, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_09, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_10, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_11, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_12, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_13, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_14, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_15, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_16, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_17, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MRMIME_IMG_18, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)
	clock.tick(30)
	create_area(MRMIME_IMG_19, "MR. MIME", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Arcanine(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		ARCANINE_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(ARCANINE_IMG_01, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_02, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_03, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_04, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_05, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_06, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_07, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_08, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_09, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_10, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_11, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_12, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_13, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_14, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_15, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_16, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_17, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(ARCANINE_IMG_18, "ARCANINE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Growlithe(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		GROWLITHE_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(GROWLITHE_IMG_01, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_02, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_03, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_04, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_05, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_06, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_07, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_08, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_09, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_10, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_11, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_12, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_13, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_14, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_15, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_16, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_17, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GROWLITHE_IMG_18, "GROWLITHE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Gastly(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		GASTLY_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(GASTLY_IMG_01, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_02, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_03, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_04, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_05, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_06, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_07, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_08, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_09, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_10, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_11, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_12, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_13, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_14, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_15, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_16, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GASTLY_IMG_17, "GASTLY", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

def create_Meowth(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		MEOWTH_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(MEOWTH_IMG_01, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_02, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_03, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_04, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_05, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_06, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_07, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_08, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_09, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_10, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_11, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_12, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_13, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_14, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_15, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_16, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_17, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_18, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_19, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_20, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_21, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_22, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_23, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(MEOWTH_IMG_24, "MEOWTH", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Beedrill(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		BEEDRILL_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(BEEDRILL_IMG_01, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_02, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_03, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_04, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_05, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_06, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_07, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_08, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_09, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_10, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_11, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_12, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_13, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_14, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_15, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_16, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_17, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_18, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_19, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_20, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_21, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_22, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(BEEDRILL_IMG_23, "BEEDRILL", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Scyther(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		SCYTHER_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_01, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_02, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_03, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_04, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_05, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_06, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_07, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SCYTHER_IMG_08, "SCYTHER", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	

def create_Gengar(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		GENGAR_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(GENGAR_IMG_01, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_02, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_03, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_04, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_05, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_06, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_07, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_08, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_09, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_10, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_11, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_12, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_13, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_14, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_15, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_16, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_17, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_18, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_19, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(GENGAR_IMG_20, "GENGAR", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Umbreon(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		UMBREON_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(UMBREON_IMG_02, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_03, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_04, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_05, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_06, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_07, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_08, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_09, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_11, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_12, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_13, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_14, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_15, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_16, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_17, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_18, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_19, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_20, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_21, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_22, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_23, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_24, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_25, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_26, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_27, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_28, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_29, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_30, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_31, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_32, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_33, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(UMBREON_IMG_34, "UMBREON", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

#def create_oak(ASH_IMG, previous_oak_x, previous_oak_y) :

	# Oak Sprites

	"""
	# Move down
	if previous_oak_y >= 100  :
		previous_oak_y += 80
		create_laboratory(ASH_IMG, OAK_IMG)
		create_laboratory(ASH_IMG,OAK_LEFT_FOOT_IMG)
		create_laboratory(ASH_IMG,OAK_RIGHT_FOOT_IMG)
		clock.tick(20)
	"""

	"""
	# Move right
	if previous_oak_y >= 150 :
		previous_oak_x += 30
		create_laboratory(ASH_IMG,OAK_RIGHT_IMG)
		create_laboratory(ASH_IMG,OAK_RIGHT_RIGHT_FOOT_IMG)
		create_laboratory(ASH_IMG,OAK_RIGHT_LEFT_FOOT_IMG)
		clock.tick(35)


	# Move up
	if previous_oak_y == 130 and previous_oak_x ==330 :
		previous_oak_y -= 30
		create_laboratory(ASH_IMG,OAK_BACK_IMG)
		create_laboratory(ASH_IMG,OAK_BACK_LEFT_FOOT_IMG)
		create_laboratory(ASH_IMG,OAK_BACK_RIGHT_FOOT_IMG)

	# Move left

	if previous_oak_y == 100 and previous_oak_x == 330 :
		previous_oak_x -= 30
		create_laboratory(ASH_IMG,OAK_LEFT_IMG)
		create_laboratory(ASH_IMG,OAK_LEFT_LEFT_FOOT_IMG)
		create_laboratory(ASH_IMG,OAK_LEFT_RIGHT_FOOT_IMG)

	"""


def create_Psyduck(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		PSYDUCK_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(PSYDUCK_IMG_01, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_02, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_03, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_04, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_05, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_06, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_07, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_08, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_09, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_10, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_11, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_12, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_13, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_14, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_15, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_16, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_17, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_18, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_19, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_20, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_21, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_22, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_23, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_24, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PSYDUCK_IMG_25, "PSYDUCK", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Squirtle(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		SQUIRTLE_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(SQUIRTLE_IMG_01, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_01, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_01, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_01, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_01, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_05, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_05, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_05, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_05, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	clock.tick(30)
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


def create_Pikachu (sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		PIKACHU_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(PIKACHU_IMG_1, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_2, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_3, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_4, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_5, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_6, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_7, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_8, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_9, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_10, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_11, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_12, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_13, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_14, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_15, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_16, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(PIKACHU_IMG_17, "PIKACHU", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	

def create_Eevee(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  :

	# Pokemon Sound

	if sound == 0:
		EEVEE_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(EEVEE_IMG_01, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_02, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_03, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_04, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_05, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_06, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_07, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_08, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_09, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_10, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_11, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_12, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_13, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_14, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_15, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_16, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_17, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_18, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_19, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
	clock.tick(30)
	create_area(EEVEE_IMG_20, "EEVEE", variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 


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

def wild_pokemon (wild_appeared, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) :

	pokemon = ""

	if wild_appeared == "PIKACHU" :
		create_Pikachu(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "SQUIRTLE" :
		create_Squirtle(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "CHARMANDER" :
		create_Charmander(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "BULBASAUR" :
		create_Bulbasaur(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "PSYDUCK" :
		create_Psyduck(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "MEOWTH":
		create_Meowth(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "UMBREON" :
		create_Umbreon(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "GASTLY" :
		create_Gastly(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "GENGAR" :
		create_Gengar(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "BEEDRILL":
		create_Beedrill(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "SCYTHER":
		create_Scyther(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "EEVEE":
		create_Eevee(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 

	elif wild_appeared == "ARCANINE":
		create_Arcanine(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)

	elif wild_appeared == "GROWLITHE":
		create_Growlithe(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  

	elif wild_appeared == "MRMIME":
		create_MrMime(sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel)  


def start_battle(wild,x ,y, pokemon_trainer, cursor_pos, isTree, isAsh, isMisty, VEL) :
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
	pokemonStaticHP = variables["POKEMON_1"]["BASE_HP"]
	pokemonVariableHP = variables["POKEMON_1"]["HP"]
	
	pokemonStaticHP_2 = variables["POKEMON_2"]["BASE_HP"]
	pokemonVariableHP_2 = variables["POKEMON_2"]["HP"]

	pokemonStaticHP_3 = variables["POKEMON_3"]["BASE_HP"]
	pokemonVariableHP_3 = variables["POKEMON_3"]["HP"]

	pokemonLevel = variables["POKEMON_1"]["LEVEL"]


	POKEMON = wild_asset(pokemon)

	create_opening_anim()
	if isAsh :
		create_ash_opening_anim(POKEMON, "")

	else :
		create_misty_opening_anim(POKEMON, "")

	time.sleep(1.5)
 
	keys = pygame.key.get_pressed()

	while wild:
		if pokemonVariableHP == 0 and pokemonVariableHP == variables["POKEMON_1"]["HP"] and variables["POKEMON_2"]["HP"] > 0   :
			pokemonVariableHP = pokemonVariableHP_2 
			pokemonStaticHP = pokemonStaticHP_2

		elif pokemonVariableHP == 0 and pokemonVariableHP == variables["POKEMON_2"]["HP"] and variables["POKEMON_2"]["HP"] == 0 and variables["POKEMON_3"]["HP"] > 0   :
			pokemonVariableHP = pokemonVariableHP_3
			pokemonStaticHP = pokemonStaticHP_3

		elif pokemonVariableHP == 0 and pokemonVariableHP == variables["POKEMON_3"]["HP"] :
			pokemonVariableHP = 0




		wild_pokemon (pokemon, sound, variableHP, staticHP, pokemonStaticHP, pokemonVariableHP, randomLevel, pokemonLevel) 
		sound +=1

		for event in pygame.event.get() : 

			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_SPACE and cursor_pos.x == 800 and cursor_pos.y == 400 :
					PRESS_A_SOUND.play()
					POKEMON_ENCOUNTER_SOUND.stop()
					SCAPE_SOUND.play()
					time.sleep(1)
					variables["POKEMON_1"]["HP"] = pokemonVariableHP
					variables["POKEMON_2"]["HP"] = pokemonVariableHP_2
					variables["POKEMON_3"]["HP"] = pokemonVariableHP_3
					save_game()
					wild = False
					print("HAS HUIDO")
					movement_down (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
					cursor_pos.x = 620

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
					if pokemonStaticHP == variables["POKEMON_1"]["BASE_HP"] :
						variables["POKEMON_1"]["HP"] = pokemonVariableHP

					if pokemonStaticHP == variables["POKEMON_2"]["BASE_HP"] :
						variables["POKEMON_2"]["HP"] = pokemonVariableHP

					if pokemonStaticHP == variables["POKEMON_3"]["BASE_HP"] :
						variables["POKEMON_3"]["HP"] = pokemonVariableHP

					save_game()
					POKEMON_ENCOUNTER_SOUND.stop()
					SCAPE_SOUND.play()
					time.sleep(1)
					VICTORY.play()

					while wild :
						create_victory_windows(variables["POKEMON_1"]["NAME"], pokemonVariableHP, pokemon, variableHP)

						for event in pygame.event.get() : 

							if event.type == pygame.KEYDOWN :

								if event.key == pygame.K_RETURN :
									wild = False
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

def movement_left_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isCharmander = False
	isBulbasaur = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.x += 1
		
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.type == pygame.K_SPACE:
					isTalking = False

	else :
		pokemon_trainer.x -= VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10

	if pokemon_trainer.colliderect(OAK_POKEBALL_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10

	if isAsh :

		create_laboratory( ASH_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( ASH_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( ASH_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory( MISTY_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( MISTY_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( MISTY_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot


def movement_left_house_trainer (pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL) :

	if isAsh :
		create_room(ASH_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL) # All Foots
		create_room(ASH_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(ASH_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, VEL ) # Right foot

	else :
		create_room(MISTY_LEFT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL) # All Foots
		create_room(MISTY_LEFT_LEFT_FOOT_IMG, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(MISTY_LEFT_RIGHT_FOOT_IMG, ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, VEL ) # Right foot

	pokemon_trainer.x -= VEL
	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BED):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_ESTANTERIA):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y


	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(OAK_RECTANGLE_MAP):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

			
	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x + VEL
		pokemon_trainer.y = previous_y

def movement_left_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y


	if not wild :
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,ASH_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_LEFT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG,MISTY_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs,ASH_PIKACHU_LEFT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.x -= VEL
		pikachu_trainer.x = pokemon_trainer.x + 60
		pikachu_trainer.y = pokemon_trainer.y - 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(MOSTRADOR_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(MESA_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(MACETA_SURESTE_RECT):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_2):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			WALL_SOUND.play()
			pokemon_trainer.x = previous_x + VEL
			pokemon_trainer.y = previous_y - 0
			pikachu_trainer.x = previous_pi_x + VEL
			pikachu_trainer.y = previous_pi_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)



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



def movement_left (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y

	if variables["INITIAL_POKEMON"] =="NONE"  :

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


def movement_right_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isBulbasaur = False
	isCharmander = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.x -= 1
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		
		for event in pygame.event.get() :
			if event.type == pygame.KEYDOWN :
				if event.type == pygame.K_SPACE:
					isTalking = False

	else :
		pokemon_trainer.x += VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 10

	if pokemon_trainer.colliderect(OAK_POKEBALL_3):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 10

	if isAsh :

		create_laboratory( ASH_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG,  OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( ASH_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory( MISTY_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # All Foots
		create_laboratory( MISTY_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, OAK_LEFT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( MISTY_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, OAK_LEFT_IMG, isTalking , isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

def movement_right_house_trainer (pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL) :

	if isAsh :
		create_room(ASH_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL ) # All Foots
		create_room(ASH_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(ASH_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL ) # Right foot

	else :
		create_room(MISTY_RIGHT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL ) # All Foots
		create_room(MISTY_RIGHT_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(MISTY_RIGHT_RIGHT_FOOT_IMG, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, VEL ) # Right foot

	pokemon_trainer.x += VEL
	previous_x = pokemon_trainer.x
	previous_y = pokemon_trainer.y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y


	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - 10
		pokemon_trainer.y = previous_y


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

		if variables["INITIAL_POKEMON"] =="NONE"  :
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


def movement_right_shopping (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False

	if not wild :
		if isAsh :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shopping_area(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 10
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

def movement_right_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	oakMessage = False
	isTree = False

	if not wild :
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG , free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.x += VEL
		pikachu_trainer.x = pokemon_trainer.x - 60
		pikachu_trainer.y = pokemon_trainer.y + 5
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(MESA_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(MACETA_SUROESTE_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y 

	if pokemon_trainer.colliderect(MACETA_NORTE_RECT):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y

	if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x - VEL
		pokemon_trainer.y = previous_y



def start_pokeball_starter_view (cursor_pos) :
	choosing = True
	cursor_pos.x = 100
	cursor_pos.y = 50
	isBulbasaur = True
	isCharmander = False
	isSquirtle = False
	isSelected = False

	while variables["INITIAL_POKEMON"] == "NONE" :
		create_pokeball_starter_view(cursor_pos.x, cursor_pos.y, isSquirtle, isBulbasaur, isCharmander, isSelected)

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_b :
					choosing = False

				if isSelected :
					if isSquirtle :
						variables["INITIAL_POKEMON"] = "Squirtle"
						# Generate initial Pokemon Stats
						variables["POKEMON_2"]["NAME"] = "SQUIRTLE"
						variables["POKEMON_2"]["LEVEL"] = 5
						variables["POKEMON_2"]["HP"] = 20
						variables["POKEMON_2"]["BASE_HP"] = 20
						variables["POKEMON_2"]["MOVE"] = "Tail Whip"
						variables["POKEMON_2"]["ATTACK"] = 13
						variables["POKEMON_2"]["DEFENSE"] = 15
						variables["POKEMON_2"]["SPECIAL_ATTACK"] = 11
						variables["POKEMON_2"]["SPECIAL_DEFENSE"] = 14
						variables["POKEMON_2"]["SPEED"] = 11
						save_game()

					if isBulbasaur :
						variables["INITIAL_POKEMON"] = "Bulbasaur"
						# Generate initial Pokemon Stats
						variables["POKEMON_2"]["NAME"] = "BULBASAUR"
						variables["POKEMON_2"]["LEVEL"] = 5
						variables["POKEMON_2"]["HP"] = 20
						variables["POKEMON_2"]["BASE_HP"] = 20
						variables["POKEMON_2"]["MOVE"] = "Tackle"
						variables["POKEMON_2"]["ATTACK"] = 13
						variables["POKEMON_2"]["DEFENSE"] = 11
						variables["POKEMON_2"]["SPECIAL_ATTACK"] = 13
						variables["POKEMON_2"]["SPECIAL_DEFENSE"] = 13
						variables["POKEMON_2"]["SPEED"] = 13
						save_game()

					if isCharmander :
						variables["INITIAL_POKEMON"] = "Charmander"
						# Generate initial Pokemon Stats
						variables["POKEMON_2"]["NAME"] = "CHARMANDER"
						variables["POKEMON_2"]["LEVEL"] = 5
						variables["POKEMON_2"]["HP"] = 20
						variables["POKEMON_2"]["BASE_HP"] = 20
						variables["POKEMON_2"]["MOVE"] = "Scratch"
						variables["POKEMON_2"]["ATTACK"] = 13
						variables["POKEMON_2"]["DEFENSE"] = 11
						variables["POKEMON_2"]["SPECIAL_ATTACK"] = 13
						variables["POKEMON_2"]["SPECIAL_DEFENSE"] = 11
						variables["POKEMON_2"]["SPEED"] = 15
						save_game()

				if cursor_pos.x == 100 and event.key == pygame.K_RIGHT :
					isBulbasaur = False
					isCharmander = True
					isSquirtle = False	

				if isCharmander and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 400 and event.key == pygame.K_LEFT :
					isCharmander = False
					isSquirtle = False
					isBulbasaur = True

				if isBulbasaur and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 400 and  event.key == pygame.K_RIGHT :
					isSquirtle = True
					isBulbasaur = False
					isCharmander = False

				if isSquirtle and event.key == pygame.K_SPACE :
					isSelected = True

				if cursor_pos.x == 700 and  event.key == pygame.K_LEFT :
					isSquirtle = False
					isBulbasaur = False
					isCharmander = True

				if cursor_pos.x < 700 and event.key == pygame.K_RIGHT :
					cursor_pos.x += 300

				if cursor_pos.x > 100 and event.key == pygame.K_LEFT :
					cursor_pos.x -= 300


def create_pokeball_starter_view (x, y, isSquirtle, isBulbasaur, isCharmander, isSelected) :
	WIN.blit(POKEBALL_CHOOSE, (0,0))
	WIN.blit(CURSOR, (x, y))


	if isSquirtle :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Squirtle, a water type Pokémon" , 1, WHITE)
		WIN.blit(oak_phrase, (55, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)


	if isBulbasaur :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Bulbasaur, a grash type Pokémon", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)

	if isCharmander :
		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Charmander, a fire type Pokémon", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press (SPACE) to choose", 1, WHITE)
		WIN.blit(oak_phrase_2, (280, 450))
		clock.tick(20)

	if isSelected :
		choosed = ""

		if isSquirtle :
			choosed = "Squirtle"
		elif isBulbasaur :
			choosed = "Bulbasaur"
		else :
			choosed = "Charmander"

		WIN.blit(DIALOG_MENU, (0, 300))
		oak_phrase = POKEBALLS_COUNTER.render("I choose you, %s" % choosed + "!", 1, WHITE)
		WIN.blit(oak_phrase, (50, 350))
		oak_phrase_2 = POKEBALLS_COUNTER.render("Press any key to exit", 1, WHITE)
		WIN.blit(oak_phrase_2, (50, 450))
		clock.tick(20)
		save_game()


	pygame.display.update()

def movement_up_house (pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isBulbasaur = False
	isCharmander = False
	isSquirtle = False

	if pokemon_trainer.colliderect(OAK_RECTANGLE):
		pokemon_trainer.y -= 1
		isTalking = True

	else :

		pokemon_trainer.y -= VEL
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		pikachu_trainer.y = pokemon_trainer.y + 60
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

	if pokemon_trainer.colliderect(OAK_TABLE):
		start_pokeball_starter_view(cursor_pos)
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + 20

	if pokemon_trainer.colliderect(OAK_POKEBALL_1):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if pokemon_trainer.colliderect(OAK_POKEBALL_2):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if pokemon_trainer.colliderect(OAK_POKEBALL_3):
		start_pokeball_starter_view(cursor_pos)
		pokemon_trainer.y = previous_y + 20


	if isAsh :

		create_laboratory( ASH_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( ASH_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Right foot

	else :
		create_laboratory( MISTY_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( MISTY_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, OAK_IMG, isTalking , isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Left foot
		create_laboratory( MISTY_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Right foot

def movement_up_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL) :

	if isAsh :

		create_room(ASH_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL ) # All Foots
		create_room(ASH_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(ASH_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, VEL) # Right foot

	else :
		create_room(MISTY_BACK_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL ) # All Foots
		create_room(MISTY_BACK_LEFT_FOOT_IMG, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL ) # Left foot
		create_room(MISTY_BACK_RIGHT_FOOT_IMG, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, VEL ) # Right foot

	pokemon_trainer.y -= VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(TRAINER_HOUSE_WALL):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_ESTANTERIA):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_TV):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BOOKS):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y + VEL

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
				my_save_slot = json.dumps(variables)
				pokemon_1_level = variables["POKEMON_1"]["LEVEL"] = 55
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
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
				main(isAsh, isMisty)

			if pokemon_trainer.colliderect(SHOP_DOOR_RECT):
				previous_y = pokemon_trainer.y + 10
				previous_x = pokemon_trainer.x
				previous_pi_y = pikachu_trainer.y
				previous_pi_x = pikachu_trainer.x
				inside = True
				TOWN.stop()
				access_shop(pokemon_trainer, pikachu_trainer, inside, previous_pi_x, previous_pi_y, isAsh, isMisty)

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



def movement_up_shop (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	
	if not wild: 
		if isAsh :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_BACK_RIGHT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_BACK_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot


		pokemon_trainer.y -= VEL
		pikachu_trainer.y = pokemon_trainer.y + VEL
		pikachu_trainer.x = pokemon_trainer.x - 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_y = pikachu_trainer.y
		previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(MESA_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_1):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_2):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(ESTANTERIA_NORTE_3):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

		if pokemon_trainer.colliderect(MOSTRADOR_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x


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

		if pokemon_trainer.colliderect(CENTER_DOOR_RECT):
			pokemon_trainer.y += VEL
			pikachu_trainer.y = pokemon_trainer.y + VEL
			pikachu_trainer.x = pokemon_trainer.x - 5
			previous_y = pokemon_trainer.y
			previous_x = pokemon_trainer.x
			previous_pi_y = pikachu_trainer.y
			previous_pi_x = pikachu_trainer.x

def access_shop (pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty) :
	trainer_pokeballs = []
	oakMessage = False
	pause = -1
	free_pika = 0
	VEL = 3

	if isAsh :
		TRAINER_IMG = ASH_BACK_IMG
	else :
		TRAINER_IMG = MISTY_BACK_IMG

	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	pokemon_trainer.x = 200
	pokemon_trainer.y = 330
	BACKGROUND_SOUND.stop()

	while inside :
		pause = 0
		create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

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
				OAK = OAK_RIGHT_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				OAK = OAK_LEFT_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				OAK = OAK_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				OAK = OAK_BACK_IMG
				create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				my_save_slot = json.dumps(variables)
				pokemon_1_level = variables["POKEMON_1"]["LEVEL"] = 55
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
				welcome()

			if pokemon_trainer.colliderect(PUERTA_RECT):
				inside = False
				SHOP_SOUND.stop()
				access_shopping_area(pokemon_trainer, pikachu_trainer, inside, before_enter_house_x, before_enter_house_y, isAsh, isMisty)

			if keys[pygame.K_x]:
				pause += 1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG

				create_shop(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)
				pause_menu(cursor_pause, pause)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1

		keys_pressed = pygame.key.get_pressed()
		trainer_movement_shop(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)

		SHOP_SOUND.play()


def create_shop(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs, PIKACHU, free_pika, oakMessage, pause, VEL)  :
	WIN.blit(SHOP_INSIDE_IMG, (0, 0))

	WIN.blit(DEPENDENT_IMG, (100, 150))

	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

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


	#pygame.draw.rect(WIN, BLUE, MACETA_SURESTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MACETA_SUROESTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MACETA_NORTE_RECT)
	#pygame.draw.rect(WIN, BLUE, MOSTRADOR_RECT)
	#pygame.draw.rect(WIN, BLUE, PUERTA_RECT)
	#pygame.draw.rect(WIN, BLUE, MESA_RECT)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_1)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_2)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_CENTRO_3)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_1)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_2)
	#pygame.draw.rect(WIN, BLUE, ESTANTERIA_NORTE_3)
	#pygame.draw.rect(WIN, BLACK, SHOP_DEPENDENT_RECT)


	pygame.display.update()


def movement_up (pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	isTree = False
	oakMessage = False

	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_y = pikachu_trainer.y
	previous_pi_x = pikachu_trainer.x

	if variables["INITIAL_POKEMON"] =="NONE":
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


def access_house (pokemon_trainer, pikachu_trainer, inside,x ,y, isAsh, isMisty) :

	VEL = 6
	pause = -1

	if isAsh :
		TRAINER_IMG = ASH_IMG
	else :
		TRAINER_IMG = MISTY_IMG

	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	pokemon_trainer.x = 700
	pokemon_trainer.y = 200

	while inside :

		pause = 0

		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			keys = pygame.key.get_pressed()
				
			if keys[pygame.K_LEFT]:
				if isAsh :
					TRAINER_IMG = ASH_LEFT_IMG
				else :
					TRAINER_IMG = MISTY_LEFT_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL )
				
			if keys[pygame.K_RIGHT] :
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL )

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL)

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				create_room(TRAINER_IMG, PIKACHU_IMG, VEL )

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				my_save_slot = json.dumps(variables)
				pokemon_1_level = variables["POKEMON_1"]["LEVEL"] = 55
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
				welcome()

			if keys[pygame.K_x]:
				pause +=1
				pause_menu(cursor_pause, pause)

			if pokemon_trainer.colliderect(TRAINER_HOUSE_DOOR):
				SCAPE_SOUND.play()
				inside = False
				OAK_THEME.stop()
				pokemon_trainer.x = x
				pokemon_trainer.y = y
				main(isAsh, isMisty)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1

		keys_pressed = pygame.key.get_pressed()
		trainer_movement_house_trainer(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL)
		create_room(TRAINER_IMG,ASH_PIKACHU_BACK_LEFT_FOOT_IMG, VEL)



def access_laboratory (pokemon_trainer, pikachu_trainer, inside, x, y, isAsh, isMisty, free_pika) :

	isTalking = False
	isBulbasaur = False
	isSquirtle = False
	isCharmander = False
	pause = -1
	trainer_pokeballs = []
	VEL = 3

	if isAsh :
		TRAINER_IMG = ASH_BACK_IMG

	else :
		TRAINER_IMG = MISTY_IMG

	OAK = OAK_RIGHT_IMG
	PIKACHU_IMG = ASH_PIKACHU_LEFT_LEFT_FOOT_IMG

	pokemon_trainer.x = 400
	pokemon_trainer.y = 360

	while inside :
		pause = 0

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
				OAK = OAK_RIGHT_IMG
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_RIGHT_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)
				
			if keys[pygame.K_RIGHT]:
				if isAsh :
					TRAINER_IMG = ASH_RIGHT_IMG
				else :
					TRAINER_IMG = MISTY_RIGHT_IMG

				PIKACHU_IMG = ASH_PIKACHU_RIGHT_RIGHT_FOOT_IMG
				OAK = OAK_LEFT_IMG
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_LEFT_IMG , isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)

			if keys[pygame.K_UP]:
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				OAK = OAK_IMG
				create_laboratory( TRAINER_IMG, PIKACHU_IMG, OAK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )

			if keys[pygame.K_DOWN]:
				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG
				OAK = OAK_BACK_IMG
				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )

			if keys[pygame.K_e]:
				inside = True
				BACKGROUND_SOUND.stop()
				my_save_slot = json.dumps(variables)
				pokemon_1_level = variables["POKEMON_1"]["LEVEL"] = 55
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
				welcome()

			if keys[pygame.K_x]:
				pause +=1

				if isAsh :
					TRAINER_IMG = ASH_IMG
				else :
					TRAINER_IMG = MISTY_IMG

				PIKACHU_IMG = ASH_PIKACHU_LEFT_FOOT_IMG

				create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL )
				pause_menu(cursor_pause, pause)

			if event.type == pygame.KEYDOWN:
				if event.unicode == "+":
					if VEL <= 12:
						VEL +=1

			if event.type == pygame.KEYDOWN:
				if event.unicode == "-":
					if VEL > 2:
						VEL -=1



			if pokemon_trainer.colliderect(OAK_DOOR):
				inside = False
				OAK_THEME.stop()
				pokemon_trainer.x = x
				pokemon_trainer.y = y
				main(isAsh, isMisty)


		OAK_THEME.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement_house(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
		create_laboratory(TRAINER_IMG, PIKACHU_IMG, OAK, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL)


def movement_down_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :

	isTalking = False
	isSquirtle = False
	isCharmander = False
	isBulbasaur = False

	if isAsh :
		create_laboratory ( ASH_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( ASH_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( ASH_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot

	else :
		create_laboratory ( MISTY_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # All Foots
		create_laboratory( MISTY_LEFT_FOOT_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL ) # Left foot
		create_laboratory( MISTY_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, OAK_BACK_IMG, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) # Right foot


	pokemon_trainer.y += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	pikachu_trainer.y = pokemon_trainer.y - 70
	pikachu_trainer.x = pokemon_trainer.x + 5
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x
	previous_pi_x = pikachu_trainer.x
	previous_pi_y = pikachu_trainer.y

	if pokemon_trainer.colliderect(OAK_TABLE):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 10



def movement_down_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL) :

	if isAsh :
		create_room(ASH_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, VEL) # All Foots
		create_room(ASH_LEFT_FOOT_IMG,  ASH_PIKACHU_RIGHT_FOOT_IMG, VEL ) # Left foot
		create_room(ASH_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, VEL ) # Right foot

	else :
		create_room(MISTY_IMG, ASH_PIKACHU_RIGHT_FOOT_IMG, VEL ) # All Foots
		create_room(MISTY_LEFT_FOOT_IMG,  ASH_PIKACHU_RIGHT_FOOT_IMG, VEL ) # Left foot
		create_room(MISTY_IMG, ASH_PIKACHU_LEFT_FOOT_IMG, VEL ) # Right foot

	pokemon_trainer.y += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(TRAINER_HOUSE_LIMIT_2):
		WALL_SOUND.play()
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL

	if pokemon_trainer.colliderect(TRAINER_HOUSE_BED):
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - VEL

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

def movement_down_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()
	isTree = False
	oakMessage = False

	if not wild :

		if isAsh :

			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG , free_pika, oakMessage, pause, VEL ) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, ASH_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		else :
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL ) # All Foots
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_LEFT_FOOT_IMG, trainer_pokeballs, ASH_PIKACHU_RIGHT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Left foot
			create_shop(pokemon_trainer, fecha,POKEBALL_IMG, MISTY_IMG, trainer_pokeballs, ASH_PIKACHU_LEFT_FOOT_IMG, free_pika, oakMessage, pause, VEL) # Right foot

		pokemon_trainer.y += VEL
		pikachu_trainer.y = pokemon_trainer.y - VEL
		pikachu_trainer.x = pokemon_trainer.x + 5
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x
		previous_pi_x = pikachu_trainer.x
		previous_pi_y = pikachu_trainer.y

		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_1):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL


		if pokemon_trainer.colliderect(ESTANTERIA_CENTRO_3):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL

		if pokemon_trainer.colliderect(MESA_RECT):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - VEL




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


# Defines the movement inside the Shop

def trainer_movement_shop(keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_shop(pokemon_trainer, wild, pikachu_trainer, free_pika, isAsh, isMisty, pause, VEL)
			fps +=1

# Defines the movement inside the Trainer house
def trainer_movement_house_trainer (keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_house_trainer(pokemon_trainer, pikachu_trainer, isAsh, isMisty, VEL)
			fps +=1


def trainer_movement_house (keys_pressed, pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down_house(pokemon_trainer, pikachu_trainer, isAsh, isMisty, pause, free_pika, VEL)
			fps +=1
		

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

	if variables["INITIAL_POKEMON"] =="NONE":
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

def create_laboratory (TRAINER, PIKACHU, OAK, isTalking, isBulbasaur, isSquirtle, isCharmander, pause, free_pika, VEL) :

	WIN.blit(OAK_LABORATORY_IMG, (0,0))

	WIN.blit(OAK, (previous_oak_x, previous_oak_y))

	WIN.blit(OAK_LABORATORY_DOOR, (400, 480))


	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	if variables["INITIAL_POKEMON"] == "Bulbasaur" :
		WIN.blit(POKEBALL_ITEM, (640, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))

	elif variables["INITIAL_POKEMON"] == "Charmander" :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))

	elif variables["INITIAL_POKEMON"] == "Squirtle" :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (640, 300))

	else :
		WIN.blit(POKEBALL_ITEM, (590, 300))
		WIN.blit(POKEBALL_ITEM, (640, 300))
		WIN.blit(POKEBALL_ITEM, (690, 300))

	WIN.blit(SHOES_BG_IMG, (0,377))
	vel_counter = POKEBALLS_COUNTER.render(str(VEL), 1, GREY)
	WIN.blit(vel_counter, (57, 392))

	
	#pygame.draw.rect(WIN, GREEN, OAK_TABLE) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_1) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_2) 
	#pygame.draw.rect(WIN, GREEN, OAK_POKEBALL_3)

	if isTalking :

		if variables["INITIAL_POKEMON"] == "NONE"  :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("" + str("Now, " + variables["NAME"].capitalize() + ", which Pokémon do you want?"), 1, WHITE)
			WIN.blit(oak_phrase, (180, 400))
			clock.tick(5)

		else :

			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("Take care of your " + variables["INITIAL_POKEMON"] + ", " + variables["NAME"].capitalize(), 1, WHITE)
			WIN.blit(oak_phrase, (180, 400))
			clock.tick(5)



	if variables["INITIAL_POKEMON"] == "NONE"  :

		if isSquirtle :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Squirtle, a water type Pokémon" , 1, WHITE)
			WIN.blit(oak_phrase, (55, 400))
			clock.tick(20)

		if isBulbasaur :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Bulbasaur, a grash type Pokémon", 1, WHITE)
			WIN.blit(oak_phrase, (50, 400))
			clock.tick(20)

		if isCharmander :
			WIN.blit(DIALOG_MENU, (0, 300))
			oak_phrase = POKEBALLS_COUNTER.render("This Pokeball contains a Charmander, a fire type Pokémon", 1, WHITE)
			WIN.blit(oak_phrase, (50, 400))
			clock.tick(20)

	if free_pika % 2 == 1 :
		WIN.blit(PIKACHU, (pikachu_trainer.x, pikachu_trainer.y ))

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
	
	WIN.blit(CLOCK_IMG, (700, 0))
	WIN.blit(date, (725, 10))
	WIN.blit(dayofWeek, (830, 20))
	WIN.blit(time, (750, 50))


	#pygame.draw.rect(WIN, GREEN, OAK_RECTANGLE) # Oak rectangle

	pygame.display.update()

def create_room (TRAINER, PIKACHU, VEL) :

	now = datetime.now()
	hora_str = now.strftime("%H")

	if int(hora_str) >= 10 and int(hora_str) < 20 : 
		WIN.blit(TRAINER_ROOM_IMG, (0,0))

	else :
		WIN.blit(TRAINER_ROOM_NIGHT, (0,0))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	#pygame.draw.rect(WIN, GREEN, TRAINER_HOUSE_DOOR) # House door
	#pygame.draw.rect(WIN, WHITE, TRAINER_HOUSE_WALL) # House wall
	#pygame.draw.rect(WIN, BLACK, TRAINER_HOUSE_LIMIT_1) # House limit
	#pygame.draw.rect(WIN, BLACK, TRAINER_HOUSE_LIMIT_2) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_BED) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_ESTANTERIA) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_TV) # House limit
	#pygame.draw.rect(WIN, BLUE, TRAINER_HOUSE_BOOKS) # House limit
	#pygame.draw.rect(WIN, GREEN, TRAINER_HOUSE_CONSOLE) # House limit

	WIN.blit(SHOES_BG_IMG, (0,377))
	vel_counter = POKEBALLS_COUNTER.render(str(VEL), 1, GREY)
	WIN.blit(vel_counter, (57, 392))
	


	pygame.display.update()

def throw_pokeball(trainer_pokeballs, pokemon_trainer, free_pika) :
	for pokeball in trainer_pokeballs:
		pokeball.x += POKEBALL_VEL

		if pokeball.x < WIDTH :
			trainer_pokeballs.remove(pokeball)

	free_pika +=1


def create_title_screen() :

	WIN.blit(TITLE_SCREEN_IMG, (0,0)) # Place background image
	pygame.display.update()


def create_pause_menu () :

	WIN.blit(PAUSE_MENU_IMG, (230,320))
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	pygame.display.update()



def create_bag_objects_screen () :
	potions_a = variables["TRAINER_BAG"]["POTIONS_AVAILABLE"]
	pokeballs_a = variables["TRAINER_BAG"]["POKEBALLS_AVAILABLE"]
	revives_a = variables["TRAINER_BAG"]["REVIVES_AVAILABLE"]

	potions_m = variables["TRAINER_BAG"]["POTIONS_MAX"]
	pokeballs_m = variables["TRAINER_BAG"]["POKEBALLS_MAX"]
	revives_m = variables["TRAINER_BAG"]["REVIVES_MAX"]

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

	if variables["POKEMON_1"]["NAME"] !="NONE" :
		pokemon_1_name = variables["POKEMON_1"]["NAME"]
		pokemon_1_level =  variables["POKEMON_1"]["LEVEL"]
		pokemon_1_hp =  variables["POKEMON_1"]["HP"]
		pokemon_1_hp_base =  variables["POKEMON_1"]["BASE_HP"]
		pokemon_1_photo = pokemonPhoto[pokemon_1_name]

	else :
		pokemon_1_name = ""
		pokemon_1_level = ""
		pokemon_1_hp = 0
		pokemon_1_hp_base = 0
		pokemon_1_photo =  pokemonPhoto["DEFAULT"]

	if variables["POKEMON_2"]["NAME"] !="NONE" :
		pokemon_2_name = variables["POKEMON_2"]["NAME"]
		pokemon_2_level =  variables["POKEMON_2"]["LEVEL"]
		pokemon_2_hp =  variables["POKEMON_2"]["HP"]
		pokemon_2_hp_base =  variables["POKEMON_2"]["BASE_HP"]
		pokemon_2_photo = pokemonPhoto[pokemon_2_name]

	else :
		pokemon_2_name = "unknown"
		pokemon_2_level = ""
		pokemon_2_hp = 0
		pokemon_2_hp_base =  0
		pokemon_2_photo =  pokemonPhoto["DEFAULT"]

	if variables["POKEMON_3"]["NAME"] !="NONE" :
		pokemon_3_name = variables["POKEMON_3"]["NAME"]
		pokemon_3_level =  variables["POKEMON_3"]["LEVEL"]
		pokemon_3_hp =  variables["POKEMON_3"]["HP"]
		pokemon_3_hp_base =  variables["POKEMON_3"]["BASE_HP"]
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
					if variables["CHARACTER"] == "NONE" :
						choose_character()

					elif variables["CHARACTER"] == "ASH" :
						isAsh = True
						isMisty = False
						main (isAsh, isMisty)

					elif variables["CHARACTER"] == "MISTY" :
						isAsh = False
						isMisty = True
						main (isAsh, isMisty)


def choose_character () :
	BACKGROUND_SOUND.stop()
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
					variables["CHARACTER"] = "ASH"
					save_game()
					enter_name(isAsh, isMisty)

				if cursor_menu.x == 470 and event.key == pygame.K_SPACE :
					PRESS_A_SOUND.play()
					isMisty = True
					start = True
					variables["CHARACTER"] = "MISTY"
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
						variables["NAME"] = text
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
				


def pokeball_out(trainer_pokeballs, free_pika) :

	pokeball = pygame.Rect(
	pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 1, 1)
	trainer_pokeballs.append(pokeball)
	BACKGROUND_SOUND.stop()
	POKEBALL_SOUND.play()
	BACKGROUND_SOUND.play()
	throw_pokeball(trainer_pokeballs, pokemon_trainer, free_pika)
	free_pika +=1

	return free_pika


def main (isAsh, isMisty): ## Main function

	BACKGROUND_SOUND.stop()
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
				if isAsh :
					TRAINER_IMG = ASH_BACK_IMG
				else :
					TRAINER_IMG = MISTY_BACK_IMG

				PIKACHU_IMG = ASH_PIKACHU_BACK_LEFT_FOOT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs, PIKACHU_IMG, free_pika, oakMessage, pause, VEL)

			if keys[pygame.K_DOWN]:
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
				my_save_slot = json.dumps(variables)
				with open('save.json', 'w') as save:
					save.write(my_save_slot)
				welcome()

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

	main()

if __name__ == "__main__":

	welcome()

