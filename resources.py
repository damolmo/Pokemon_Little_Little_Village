# Third block of code
# Includes the definition of all game values

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
#----------------------------------


class Player :

	def __init__(self, width, height) :
		self.width = width
		self.height = height

trainer_size = Player(64,76)


# -------------------------------------------------------------------------------
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

# Player values
my_save_slot = open("save.json")
variables = json.load(my_save_slot)

## App icon
icon = pygame.image.load('Assets/background/title_screen/logo.png')
pygame.display.set_icon(icon)

## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
HOME_RECT_MAP = pygame.Rect(0, 300, 100, 200)

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
ESTANTERIA_CENTRO_3 = pygame.Rect(595, 245, 125, 70)
ESTANTERIA_NORTE_1 = pygame.Rect(200, 10, 120, 120)
ESTANTERIA_NORTE_2 = pygame.Rect(350, 10, 120, 120)
ESTANTERIA_NORTE_3 = pygame.Rect(500, 0, 300, 75)

SHOP_DEPENDENT_RECT =  pygame.Rect(150, 120, 60, 100)
DEPENDENT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/shop_dependent', "dependent.png")), (trainer_size.width, trainer_size.height))


# Pokemon Center rect
JOY_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/joy/down', "joy_down.png")), (trainer_size.width, trainer_size.height))
JOY_UP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/joy/up', "joy_up.png")), (trainer_size.width, trainer_size.height))
JOY_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/joy/left', "joy_left.png")), (trainer_size.width, trainer_size.height))
JOY_RECT = pygame.Rect(420, 190, 60, 40)
CENTER_DOOR = pygame.Rect(410, 460, 90, 40)
CENTER_PLANTS = pygame.Rect(700, 250, 120, 40)
CENTER_STAIRS_RIGHT = pygame.Rect(730, 300, 100, 100)
CENTER_STAIRS_WEST =  pygame.Rect(620, 0, 120, 160)
LIMIT_WEST =  pygame.Rect(740, 160, 120, 160)
CENTER_STAIRS_EAST =  pygame.Rect(100, 0, 120, 300)
LIMIT_EAST =  pygame.Rect(0, 300, 120, HEIGHT - 300)
CENTER_DESK = pygame.Rect(250, 120, 350, 100)
BANK_RECT = pygame.Rect(550, 170, 50, 60)

# Team Rocket Rect
ROCKET_RECT = pygame.Rect(800, 300, 100, 200)
ROCKET_LOGO_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT)

# Mumu Farm Rect
FARM_RECT = pygame.Rect(860, 300, 50, 300)


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

previous_mom_x, previous_mom_y = 400, 100
mom = pygame.Rect(previous_mom_x, previous_mom_y, 74, 96) # Defines player coords

## Walking
# --- Down Position ---
MOM_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/down', "mom_down.png")), (74, 96))
MOM_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/down', "mom_down_left_foot.png")), (74, 96))
MOM_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/down', "mom_down_right_foot.png")), (74, 96))

# --- Left Position ---
MOM_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/left', "mom_left.png")), (74, 96))
MOM_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/left', "mom_left_left_foot.png")), (74, 96))
MOM_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/left', "mom_left_right_foot.png")), (74, 96))

# --- Right Position ---
MOM_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/right', "mom_right.png")), (74, 96))
MOM_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/right', "mom_right_right_foot.png")), (74, 96))
MOM_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/right', "mom_right_left_foot.png")), (74, 96))

# --- Up Position ---
MOM_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/up', "mom_up.png")), (74, 96))
MOM_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/up', "mom_up_left_foot.png")), (74, 96))
MOM_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/mom/up', "mom_up_right_foot.png")), (74, 96))


### Team Rocket Assets

# Sound effect
ROCKET_SOUND = pygame.mixer.Sound("Assets/sounds/team_rocket_sound.mp3")


## Jessie
JESSIE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/jessie/down', "jessie_down.png")), (trainer_size.width, trainer_size.height))
JESSIE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/jessie/down', "jessie_down_left_foot.png")), (trainer_size.width, trainer_size.height))
JESSIE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/jessie/down', "jessie_down_right_foot.png")), (trainer_size.width, trainer_size.height))


## James
JAMES_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/james/down', "james_down.png")), (trainer_size.width, trainer_size.height))
JAMES_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/james/down', "james_down_left_foot.png")), (trainer_size.width, trainer_size.height))
JAMES_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/james/down', "james_down_right_foot.png")), (trainer_size.width, trainer_size.height))

## Meowth
MEOWTH_GIF = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/meowth', "meowth.gif")), (trainer_size.width, trainer_size.height))

## Battle opening

## Asset
ROCKET_INTRO = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/intro', "jessie_james_asset.png")), (WIDTH, HEIGHT))

## OPENING
ROCKET_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_00_delay-0.41s.gif")), (200, 200))
ROCKET_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_01_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_02_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_03_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_04_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_05_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_06_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_07_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_08_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_09_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_10_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_11_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_12_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_13_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_14_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_15_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_16_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_17_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_18_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_19_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_20_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_21_delay-0.01s.gif")), (200, 200))
ROCKET_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/team_rocket/logo', "frame_22_delay-0.01s.gif")), (200, 200))

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
TITLE_SCREEN_DAY_IMG = pygame.image.load(os.path.join('Assets/background/title_screen', "day_title_screen.png"))
TITLE_SCREEN_AFTERNOON_IMG = pygame.image.load(os.path.join('Assets/background/title_screen', "afternoon_title_screen.png"))
TITLE_SCREEN_EVENING_IMG = pygame.image.load(os.path.join('Assets/background/title_screen', "night_title_screen.png"))
TITLE_LOGO_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/title_screen', "title_logo.png")), (400, 400))

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

# Mumu Farm
MUMU_FARM_OPENING_IMG = pygame.image.load(os.path.join('Assets/background/mumu_farm', "background.png"))
MUMU_FARM_LOGO_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/mumu_farm', "logo.png")), (200, 200))
MUMU_FARM_BOTTLE_MIDDLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/mumu_farm', "bottle_middle.png")), (180, 300))
MUMU_FARM_BOTTLE_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/mumu_farm', "bottle_left.png")), (180, 300))
MUMU_FARM_BOTTLE_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/mumu_farm', "bottle_right.png")), (180, 300))

# Shopping Zone
SHOPPING_OPENING_IMG = pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "background.png"))
SHOPPING_LOGO_IMG = pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "logo.png"))
SHOPPING_TREE_MIDDLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "tree_middle.png")), (200, 200))
SHOPPING_TREE_LEFT_IMG =  pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "tree_left.png")), (200, 200))
SHOPPING_TREE_RIGHT_IMG =  pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "tree_right.png")), (200, 200))
SHOPPING_CLOUD_BOTTOM_IMG = pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "cloud_bottom.png"))
SHOPPING_CLOUD_MIDDLE_IMG = pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "cloud_middle.png"))
SHOPPING_CLOUD_TOP_IMG = pygame.image.load(os.path.join('Assets/background/shopping_zone/animation', "cloud_top.png"))

# TRAINER ROOM
TRAINER_ROOM_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/trainer_house/day', "room_day.png")), (WIDTH, HEIGHT))
TRAINER_ROOM_NIGHT = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/trainer_house/night', "room_night.png")), (WIDTH, HEIGHT))

# Pause Menu
TRAINER_PAUSE_MENU_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/menu/settings', "trainer_pause_menu.png")), (900, 507))
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
CENTER_INSIDE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/shop', "center.png")), (WIDTH,HEIGHT))
CENTER_BANK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/pokemon_center', "bank.png")), (WIDTH,HEIGHT))
GIFT_CALENDAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/rewards', "rewards.png")), (WIDTH,HEIGHT))
GIFT_SIGN_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/rewards', "sello.png")), (100,110))

SHOP_ITEMS_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/shopping_zone/shop', "pokemon_shop_items.png")), (WIDTH,HEIGHT))

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


# NPC Battle
BATTLE_INTRO = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/challenge', "battle.png")), (WIDTH, HEIGHT))
BATTLE_ARENA =  pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/challenge', "battle_arena.png")), (WIDTH, HEIGHT))

# Battle Assets
TEAM_ROCKET = pygame.transform.scale(pygame.image.load(os.path.join('Assets/npcs/challenge/jessie_james', "rocket.png")), (200, 200))

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
HEALING_SOUND = pygame.mixer.Sound("Assets/sounds/healing.mp3")
CASH_SOUND = pygame.mixer.Sound("Assets/sounds/cash.mp3")
OPENING_SOUND = pygame.mixer.Sound("Assets/sounds/opening.mp3")
HOUSE_SOUND = pygame.mixer.Sound("Assets/sounds/house.mp3")

## Catching sounds
CATCHING_SOUND = pygame.mixer.Sound("Assets/sounds/catching.mp3")
TRYING_SOUND = pygame.mixer.Sound("Assets/sounds/trying.mp3")
GOTCHA_SOUND = pygame.mixer.Sound("Assets/sounds/gotcha.mp3")

## Mumu Sounds
MILTANK_SOUND = pygame.mixer.Sound("Assets/sounds/miltank.mp3")


# Pokeball
POKEBALL_IMG = pygame.image.load(os.path.join('Assets/items', "pokeball.png"))
POKEBALL_ITEM = pygame.transform.scale(pygame.image.load(os.path.join('Assets/items', "pokeball_item.png")), (40,40))
POKEBALL_SOUND = pygame.mixer.Sound("Assets/sounds/pokeball_out.mp3")
MAX_POKEBALL = 3
POKEBALL_VEL = 3
POKEBALL_ITEM.convert()

# Display Fonts
WINNER_LOOSER_DIALOG = pygame.font.SysFont('comicsans', 80)
SHOP_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)
POKEBALLS_COUNTER = pygame.font.SysFont('comicsans', 30)
POKEBALLS_COUNTER_2 = pygame.font.SysFont('comicsans', 28)
DIALOG_FONT = pygame.font.SysFont('comicsans', 26)
DIALOG_MINI_FONT = pygame.font.SysFont('comicsans', 18)
RULES = pygame.font.SysFont('comicsans', 16)
GIFS = pygame.font.SysFont('comicsans', 10)

# Threads
main_thread = variables["THREADS"]["MAIN"]
shopping_thread = variables["THREADS"]["SHOPPING"]

threads_list = [main_thread, shopping_thread ]

# -------------------------------------------

# Second block of code
# Includes some python class for system integrity and trainer static values

##-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------