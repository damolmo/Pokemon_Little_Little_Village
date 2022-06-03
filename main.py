# Pokemon Pi
# Fan Game powered by Python and Pygame
# Credits to Pygame for the libs

import os
from random import randint
import random

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
		download_assets()

check_Assets_Exist()

## Game Values
FPS = 60
VEL = 2
VEL_CURSOR = 50
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,204)
GREEN = (0, 204, 102)
today = date.today()
fecha = today.strftime("%B %d, %Y")
now = datetime.now()
hora = now.strftime("%H")


## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Draws the map with given dimentions
pygame.display.set_caption("Pokémon Pi - Route")

## Map elements
HOUSE_1 = pygame.Rect(650, 20, 220, 250)
HOUSE_2 = pygame.Rect(90, 0, 280, 180)
TREE_1 = pygame.Rect(500, 140, 120, 120)
TREE_2 = pygame.Rect(230, 280, 120, 120)
GRASS_ZONE_SOUTH = pygame.Rect(320, 400, 500, 120)
GRASS_ZONE_SOUTH_2 = pygame.Rect(0, 274, 250, 250)
GRASS_ZONE_WEST = pygame.Rect(0, 0, 80, 250)
GRASS_ZONE_EAST = pygame.Rect(500, 0, 130, 130)

## Character Values
TRAINER_WIDTH, TRAINER_HEIGHT = 64, 76


## Game Events
THROW_POKEBALL = pygame.USEREVENT +1
clock = pygame.time.Clock()

## Assets

# Trainer
pokemon_trainer = pygame.Rect(450, 253, TRAINER_WIDTH, TRAINER_HEIGHT) # Defines player coords
previous_x, previous_y = 450, 253
x_change, y_change = 450, 2531

## Walking
# --- Down Position ---
TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Left Position ---
TRAINER_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_left.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_left_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_left_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Right Position ---
TRAINER_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_right.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_right_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_right_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Up Position ---
TRAINER_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_back.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_back_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_back_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

## Running

## Bicicle
# --- Down Position ---
TRAINER_BICICLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_left.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_right.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Left Position ---
TRAINER_BICICLE_LEFT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_left_foots.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_LEFT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_left_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_LEFT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_left_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Right Position ---
TRAINER_BICICLE_RIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_right_foots.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_RIGHT_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_right_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_RIGHT_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_right_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# --- Up Position ---
TRAINER_BICICLE_BACK_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_back_foots.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_BACK_LEFT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_back_left_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
TRAINER_BICICLE_BACK_RIGHT_FOOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_bicicle_back_right_foot.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))

### Pokemon

## Pikachu

# Sound effect
PIKACHU_SOUND = pygame.mixer.Sound("Assets/pikachu/sound/pikachu.mp3")

# Sprites
PIKACHU_IMG_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_000_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_001_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_002_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_4 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_003_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_5 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_004_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_6 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_005_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_7 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_006_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_8 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_007_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_9 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_008_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_009_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_010_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_011_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_012_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_013_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_014_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_015_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_016_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_017_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_018_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_019_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_020_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_021_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_022_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_023_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_024_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_025_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_026_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_027_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_028_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_029_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_030_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_031_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_032_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_033_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_35 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_034_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_36 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_035_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_37 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_036_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_38 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_037_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_39 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_038_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_40 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_039_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_41 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_040_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_42 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_041_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_43 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_042_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_44 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_043_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_45 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_044_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_46 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_045_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_47 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_046_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_48 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_047_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_49 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_048_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_50 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_049_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_51 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_050_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_52 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_051_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_53 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_052_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_54 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_053_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_55 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_054_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_56 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_055_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_57 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_056_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_58 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_057_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_59 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_058_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_60 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_059_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_61 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_060_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_62 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_061_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_63 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_062_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_64 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_063_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_65 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_064_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_66 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_065_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_67 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_066_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_68 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_067_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_69 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_068_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_70 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_069_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_71 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_070_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_72 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_071_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_73 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_072_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_74 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_073_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_75 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_074_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_76 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_075_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_77 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_076_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_78 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_077_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_79 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_078_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_80 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_079_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_81 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_080_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_82 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_081_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_83 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_082_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_84 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_083_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_85 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_084_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_86 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_085_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_87 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_086_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_88 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_087_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_89 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_088_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_90 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_089_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_91 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_090_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_92 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_091_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_93 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_092_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_94 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_093_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_95 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_094_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_96 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_095_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_97 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_096_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_98 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_097_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_99 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_098_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_100 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_099_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_101 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_100_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_102 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_101_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_103 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_102_delay-0.15s.gif")), (200, 200))
PIKACHU_IMG_104 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_103_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_105 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_104_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_106 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_105_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_107 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_106_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_108 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_107_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_109 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_108_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_110 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_109_delay-0.05s.gif")), (200, 200))
PIKACHU_IMG_111 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_110_delay-0.1s.gif")), (200, 200))
PIKACHU_IMG_112 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/pikachu', "frame_111_delay-0.1s.gif")), (200, 200))

## Squirtle

# Sound effect
SQUIRTLE_SOUND = pygame.mixer.Sound("Assets/squirtle/sound/squirtle.mp3")

# Sprites
SQUIRTLE_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_00_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_01_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_02_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_03_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_04_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_05_delay-0.02s.gif")), (200, 200))
SQUIRTLE_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_06_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_07_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_08_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_09_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_10_delay-0.08s.gif")), (200, 200))
SQUIRTLE_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_11_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_12_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_13_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_14_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_15_delay-0.53s.gif")), (200, 200))
SQUIRTLE_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_16_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_17_delay-0.07s.gif")), (200, 200))
SQUIRTLE_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_18_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_19_delay-0.12s.gif")), (200, 200))
SQUIRTLE_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_20_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_21_delay-0.03s.gif")), (200, 200))
SQUIRTLE_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_22_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_23_delay-0.12s.gif")), (200, 200))
SQUIRTLE_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_24_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_25_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_26_delay-0.06s.gif")), (200, 200))
SQUIRTLE_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_27_delay-0.09s.gif")), (200, 200))
SQUIRTLE_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_28_delay-0.06s.gif")), (200, 200))
SQUIRTLE_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_29_delay-0.04s.gif")), (200, 200))
SQUIRTLE_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_30_delay-0.05s.gif")), (200, 200))
SQUIRTLE_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/squirtle', "frame_31_delay-0.24s.gif")), (200, 200))

# Charmander

# Sound effect
CHARMANDER_SOUND = pygame.mixer.Sound("Assets/charmander/sound/charmander.mp3")

# Sprites
CHARMANDER_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_00_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_01_delay-0.11s.gif")), (200, 200))
CHARMANDER_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_02_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_03_delay-0.03s.gif")), (200, 200))
CHARMANDER_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_04_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_05_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_06_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_07_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_08_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_09_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_10_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_11_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_12_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_13_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_14_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_15_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_16_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_17_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_18_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_19_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_20_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_21_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_22_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_23_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_24_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_25_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_26_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_27_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_28_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_29_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_30_delay-0.03s.gif")), (200, 200))
CHARMANDER_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_31_delay-0.09s.gif")), (200, 200))
CHARMANDER_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_32_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_33_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_35 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_34_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_36 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_35_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_37 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_36_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_38 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_37_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_39 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_38_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_40 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_39_delay-0.07s.gif")), (200, 200))
CHARMANDER_IMG_41 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_40_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_42 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_41_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_43 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_42_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_44 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_43_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_45 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_44_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_46 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_45_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_47 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_46_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_48 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_47_delay-0.06s.gif")), (200, 200))
CHARMANDER_IMG_49 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_48_delay-0.08s.gif")), (200, 200))
CHARMANDER_IMG_50 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_49_delay-0.05s.gif")), (200, 200))
CHARMANDER_IMG_51 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_50_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_52 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_51_delay-0.09s.gif")), (200, 200))
CHARMANDER_IMG_53 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_52_delay-0.04s.gif")), (200, 200))
CHARMANDER_IMG_54 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/charmander', "frame_53_delay-0.06s.gif")), (200, 200))

## Bulbasaur

# Sound effect
BULBASAUR_SOUND = pygame.mixer.Sound("Assets/bulbasaur/sound/bulbasaur.mp3")

# Sprites
BULBASAUR_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_00_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_01_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_02_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_03_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_04_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_05_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_06_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_07_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_08_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_09_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_10_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_11_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_12_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_13_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_14_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_15_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_16_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_17_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_18_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_19_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_20_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_21_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_22_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_23_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_24_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_25_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_26_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_27_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_28_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_29_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_30_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_31_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_32_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_33_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_35 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_34_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_36 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_35_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_37 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_36_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_38 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_37_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_39 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_38_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_40 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_39_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_41 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_40_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_42 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_41_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_43 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_42_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_44 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_43_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_45 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_44_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_46 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_45_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_47 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_46_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_48 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_47_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_49 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_48_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_50 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_49_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_51 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_50_delay-0.07S.gif")), (200, 200))
BULBASAUR_IMG_52 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/BULBASAUR', "frame_51_delay-0.07S.gif")), (200, 200))


## Psyduck

# Sound
PSYDUCK_SOUND = pygame.mixer.Sound("Assets/psyduck/sound/psyduck.mp3")

# Sprites
PSYDUCK_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_00_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_01_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_02_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_03_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_04_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_05_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_06_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_07_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_08_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_09_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_10_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_11_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_12_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_13_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_14_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_15_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_16_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_17_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_18_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_19_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_20_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_21_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_22_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_23_delay-0.09s.gif")), (200, 200))
PSYDUCK_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/psyduck', "frame_24_delay-0.09s.gif")), (200, 200))

## Gastly

# Sound
GASTLY_SOUND = pygame.mixer.Sound("Assets/gastly/sound/gastly.mp3")

# Sprites
GASTLY_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_00_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_01_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_02_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_03_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_04_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_05_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_06_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_07_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_08_delay-0.1s.gif")), (200, 200))
GASTLY_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_09_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_10_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_11_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_12_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_13_delay-0.25s.gif")), (200, 200))
GASTLY_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_14_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_15_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_16_delay-0.06s.gif")), (200, 200))
GASTLY_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/gastly', "frame_17_delay-0.06s.gif")), (200, 200))

## Meowth

# Sound
MEOWTH_SOUND = pygame.mixer.Sound("Assets/meowth/sound/meowth.mp3")

# Sprites
MEOWTH_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_00_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_01_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_02_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_03_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_04_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_05_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_06_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_07_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_08_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_09_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_10_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_11_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_12_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_13_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_14_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_15_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_16_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_17_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_18_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_19_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_20_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_21_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_22_delay-0.08s.gif")), (200, 200))
MEOWTH_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/MEOWTH', "frame_23_delay-0.08s.gif")), (200, 200))

## Umbreon

# Sound
UMBREON_SOUND = pygame.mixer.Sound("Assets/umbreon/sound/umbreon.mp3")

# Sprites
UMBREON_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_02_delay-0.14s.png")), (270, 200))
UMBREON_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_03_delay-0.14s.png")), (270, 200))
UMBREON_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_04_delay-0.14s.png")), (270, 200))
UMBREON_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_05_delay-0.14s.png")), (270, 200))
UMBREON_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_06_delay-0.14s.png")), (270, 200))
UMBREON_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_07_delay-0.14s.png")), (270, 200))
UMBREON_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_08_delay-0.14s.png")), (270, 200))
UMBREON_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_09_delay-0.14s.png")), (270, 200))
UMBREON_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_11_delay-0.14s.png")), (270, 200))
UMBREON_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_12_delay-0.14s.png")), (270, 200))
UMBREON_IMG_13 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_13_delay-0.14s.png")), (270, 200))
UMBREON_IMG_14 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_14_delay-0.14s.png")), (270, 200))
UMBREON_IMG_15 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_15_delay-0.14s.png")), (270, 200))
UMBREON_IMG_16 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_16_delay-0.14s.png")), (270, 200))
UMBREON_IMG_17 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_17_delay-0.14s.png")), (270, 200))
UMBREON_IMG_18 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_18_delay-0.24s.png")), (270, 200))
UMBREON_IMG_19 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_19_delay-0.14s.png")), (270, 200))
UMBREON_IMG_20 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_20_delay-0.14s.png")), (270, 200))
UMBREON_IMG_21 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_21_delay-0.14s.png")), (270, 200))
UMBREON_IMG_22 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_22_delay-0.14s.png")), (270, 200))
UMBREON_IMG_23 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_23_delay-0.14s.png")), (270, 200))
UMBREON_IMG_24 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_24_delay-0.14s.png")), (270, 200))
UMBREON_IMG_25 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_25_delay-0.14s.png")), (270, 200))
UMBREON_IMG_26 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_26_delay-0.24s.png")), (270, 200))
UMBREON_IMG_27 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_27_delay-0.14s.png")), (270, 200))
UMBREON_IMG_28 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_28_delay-0.14s.png")), (270, 200))
UMBREON_IMG_29 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_29_delay-0.14s.png")), (270, 200))
UMBREON_IMG_30 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_30_delay-0.14s.png")), (270, 200))
UMBREON_IMG_31 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_31_delay-0.14s.png")), (270, 200))
UMBREON_IMG_32 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_32_delay-0.14s.png")), (270, 200))
UMBREON_IMG_33 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_33_delay-0.14s.png")), (270, 200))
UMBREON_IMG_34 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/UMBREON', "frame_34_delay-0.1s.png")), (270, 200))

# Background
TITLE_SCREEN_IMG = pygame.image.load(os.path.join('Assets', "welcome.png"))
ROUTE_IMG = pygame.image.load(os.path.join('Assets', "background.png"))
ROUTE_IMG_2 = pygame.image.load(os.path.join('Assets', "background_evening.png"))
ROUTE_IMG_3 = pygame.image.load(os.path.join('Assets', "background_night.png"))

BATTLE_ARENA_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "battle_arena.png")), (WIDTH, HEIGHT))
BATTLE_ARENA_NIGHT_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "battle_arena_night.png")), (WIDTH, HEIGHT))
ASH_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_battle_1.png")), (300,300))
BATTLE_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "menu.png")), (260,90))
CURSOR = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "cursor.png")), (100,100))
cursor_pos = pygame.Rect(620, 350, 100, 100) # Defines player coords
LIFE_MENU = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "life_menu.png")), (250,62))
WILD_POKEMON = "unknown"


# Battle opening
BATTLE_ARENA_IMG_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_1.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_2.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_3.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_4.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_5.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_6.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_7.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_8.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_09 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_9.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_10 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_10.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_11 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_11.gif")), (WIDTH, HEIGHT))
BATTLE_ARENA_IMG_12 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/fight', "grass_12.gif")), (WIDTH, HEIGHT))


# Music
BACKGROUND_SOUND = pygame.mixer.Sound("Assets/music.mp3")
POKEMON_ENCOUNTER_SOUND = pygame.mixer.Sound("Assets/pokemon_encounter.mp3")
GRASS_SOUND = pygame.mixer.Sound("Assets/grass.mp3")
SCAPE_SOUND = pygame.mixer.Sound("Assets/scape.mp3")

# Pokeball
POKEBALL_IMG = pygame.image.load(os.path.join('Assets', "pokeball.png"))
POKEBALL_ITEM = pygame.image.load(os.path.join('Assets', "pokeball_item.png"))
POKEBALL_SOUND = pygame.mixer.Sound("Assets/pokeball_out.mp3")
MAX_POKEBALL = 3
POKEBALL_VEL = 3
POKEBALL_ITEM.convert()

# Displat Fonts
POKEBALLS_COUNTER = pygame.font.SysFont('comicsans', 30)
RULES = pygame.font.SysFont('comicsans', 16)


def create_area (POKEMON, POKEMON_NAME) :

	if hora <="16" and hora >="10" :
		WIN.blit(BATTLE_ARENA_IMG, (0,0))

	elif hora >="17" and hora <"20":
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0)) # Place background image

	else:
		WIN.blit(BATTLE_ARENA_NIGHT_IMG, (0,0))


	#pygame.draw.rect(WIN, BLUE, HOUSE_1) # House 1 building
	#pygame.draw.rect(WIN, BLUE, HOUSE_2) # House 2 building

	#pygame.draw.rect(WIN, GREEN, TREE_1) # Tree 1 building
	#pygame.draw.rect(WIN, GREEN, TREE_2) # Tree 2 building

	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH) # Grass zone south


	# Battle Elements
	WIN.blit(ASH_BATTLE_IMG, (0,250))
	WIN.blit(POKEMON, (640,160))
	WIN.blit(BATTLE_MENU, (600,410)) # Place background image
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	WIN.blit(LIFE_MENU, (0, 30))

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


def create_Bulbasaur(sound) :


	# Pokemon Sound

	if sound == 0:
		BULBASAUR_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(BULBASAUR_IMG_01, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_02, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_03, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_04, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_05, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_06, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_07, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_08, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_09, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_10, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_11, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_12, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_13, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_14, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_15, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_16, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_17, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_18, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_19, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_20, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_21, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_22, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_23, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_24, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_25, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_26, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_27, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_28, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_29, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_30, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_31, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_32, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_33, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_34, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_35, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_36, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_37, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_38, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_39, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_40, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_41, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_42, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_43, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_44, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_45, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_46, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_47, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_48, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_49, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_50, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_51, "BULBASAUR")
	clock.tick(30)
	create_area(BULBASAUR_IMG_52, "BULBASAUR")


def create_Charmander(sound) :

	# Pokemon Sound

	if sound == 0:
		CHARMANDER_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(CHARMANDER_IMG_01, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_02, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_03, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_04, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_05, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_06, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_07, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_08, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_09, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_10, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_11, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_12, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_13, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_14, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_15, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_16, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_17, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_18, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_19, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_20, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_21, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_22, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_23, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_24, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_25, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_26, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_27, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_28, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_29, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_30, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_31, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_32, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_33, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_34, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_35, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_36, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_37, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_38, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_39, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_40, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_41, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_42, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_43, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_44, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_45, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_46, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_47, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_48, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_49, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_50, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_51, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_52, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_53, "CHARMANDER")
	clock.tick(30)
	create_area(CHARMANDER_IMG_54, "CHARMANDER")


def create_Gastly(sound) :

	# Pokemon Sound

	if sound == 0:
		GASTLY_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(GASTLY_IMG_01, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_02, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_03, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_04, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_05, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_06, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_07, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_08, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_09, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_10, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_11, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_12, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_13, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_14, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_15, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_16, "GASTLY")
	clock.tick(30)
	create_area(GASTLY_IMG_17, "GASTLY")

def create_Meowth(sound) :

	# Pokemon Sound

	if sound == 0:
		MEOWTH_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(MEOWTH_IMG_01, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_02, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_03, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_04, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_05, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_06, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_07, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_08, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_09, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_10, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_11, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_12, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_13, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_14, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_15, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_16, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_17, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_18, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_19, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_20, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_21, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_22, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_23, "MEOWTH")
	clock.tick(30)
	create_area(MEOWTH_IMG_24, "MEOWTH")

def create_Umbreon(sound) :

	# Pokemon Sound

	if sound == 0:
		UMBREON_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(UMBREON_IMG_02, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_03, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_04, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_05, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_06, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_07, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_08, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_09, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_11, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_12, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_13, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_14, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_15, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_16, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_17, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_18, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_19, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_20, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_21, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_22, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_23, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_24, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_25, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_26, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_27, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_28, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_29, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_30, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_31, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_32, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_33, "UMBREON")
	clock.tick(30)
	create_area(UMBREON_IMG_34, "UMBREON")


def create_Psyduck(sound) :

	# Pokemon Sound

	if sound == 0:
		PSYDUCK_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(PSYDUCK_IMG_01, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_02, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_03, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_04, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_05, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_06, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_07, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_08, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_09, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_10, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_11, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_12, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_13, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_14, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_15, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_16, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_17, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_18, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_19, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_20, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_21, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_22, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_23, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_24, "PSYDUCK")
	clock.tick(30)
	create_area(PSYDUCK_IMG_25, "PSYDUCK")


def create_Squirtle(sound) :

	# Pokemon Sound

	if sound == 0:
		SQUIRTLE_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(SQUIRTLE_IMG_01, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_02, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_03, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_04, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_05, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_06, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_07, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_08, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_09, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_10, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_11, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_12, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_13, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_14, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_15, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_16, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_17, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_18, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_19, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_20, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_21, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_22, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_23, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_24, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_25, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_26, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_27, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_28, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_29, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_30, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_31, "SQUIRTLE")
	clock.tick(30)
	create_area(SQUIRTLE_IMG_32, "SQUIRTLE")

def create_Pikachu (sound) :

	# Pokemon Sound

	if sound == 0:
		PIKACHU_SOUND.play()
		sound +=1

	# Pokemon Sprites

	create_area(PIKACHU_IMG_1, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_2, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_3, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_4, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_5, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_6, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_7, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_8, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_9, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_10, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_11, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_12, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_13, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_14, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_15, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_16, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_17, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_18, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_19, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_20, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_21, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_22, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_23, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_24, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_25, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_26, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_27, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_28, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_29, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_30, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_31, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_32, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_33, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_34, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_35, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_36, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_37, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_38, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_39, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_40, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_41, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_42, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_43, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_44, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_45, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_46, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_47, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_48, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_49, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_50, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_51, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_52, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_53, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_54, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_55, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_56, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_57, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_58, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_59, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_60, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_61, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_62, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_63, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_64, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_65, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_66, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_67, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_68, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_69, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_70, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_71, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_72, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_73, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_74, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_75, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_76, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_77, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_78, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_79, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_80, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_81, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_82, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_83, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_84, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_85, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_86, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_87, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_88, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_89, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_90, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_91, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_92, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_93, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_94, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_95, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_96, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_97, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_98, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_99, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_100, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_101, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_102, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_103, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_104, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_105, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_106, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_107, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_108, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_109, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_110, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_111, "PIKACHU")
	clock.tick(30)
	create_area(PIKACHU_IMG_112, "PIKACHU")
	clock.tick(30)
	pygame.display.flip()


def random_pokemon () :

	pokemon_route = []

	wild_appeared = 0
	if int(hora) < 10 :
		pokemon_route = [8]

	if int(hora) >=10 and int(hora) < 20 :
		pokemon_route = [7,1,2,1,4,3,2,1,4,2,5,6,2,7]

	wild_appeared = random.choice(pokemon_route)

	return wild_appeared

def wild_pokemon (wild_appeared, sound) :

	if wild_appeared == 1 :
		create_Pikachu(sound)

	elif wild_appeared == 2 :
		create_Squirtle(sound)

	elif wild_appeared == 3 :
		create_Charmander(sound)

	elif wild_appeared == 4 :
		create_Bulbasaur(sound)

	elif wild_appeared == 5 :
		create_Psyduck(sound)

	elif wild_appeared == 6 :
		create_Meowth(sound)

	elif wild_appeared == 7 :
		create_Umbreon(sound)

	elif wild_appeared == 8 :
		create_Gastly(sound)


def start_battle(wild,x ,y, pokemon_trainer, cursor_pos) :
	GRASS_SOUND.stop()
	BACKGROUND_SOUND.stop()
	POKEMON_ENCOUNTER_SOUND.play()
	time.sleep(1.2)
	pokemon = random_pokemon()
	sound = 0
	create_opening_anim()
 
	keys = pygame.key.get_pressed()

	while wild:
		wild_pokemon (pokemon, sound)
		sound +=1


		for event in pygame.event.get() : 

			if event.type == pygame.KEYDOWN :

				if event.key == pygame.K_SPACE and cursor_pos.x == 800 and cursor_pos.y == 400 :
					POKEMON_ENCOUNTER_SOUND.stop()
					SCAPE_SOUND.play()
					time.sleep(1)
					wild = False
					print("HAS HUIDO")
					movement_down (pokemon_trainer, wild)
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


def movement_left (pokemon_trainer, wild) :
	trainer_pokeballs = []

	if not wild :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_IMG, trainer_pokeballs) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

		pokemon_trainer.x -= VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y

		if pokemon_trainer.colliderect(HOUSE_2):
			pokemon_trainer.x = previous_x + 5
			pokemon_trainer.y = previous_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(TREE_2):
			pokemon_trainer.x = previous_x + 5
			pokemon_trainer.y = previous_y - 0

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
				wild = True
				POKEMON_ENCOUNTER_SOUND.play()
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)


def movement_right (pokemon_trainer, wild) :
	trainer_pokeballs = []

	if not wild :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_IMG, trainer_pokeballs ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

		pokemon_trainer.x += VEL
		previous_x = pokemon_trainer.x
		previous_y = pokemon_trainer.y

		if pokemon_trainer.colliderect(HOUSE_1):
			pokemon_trainer.x = previous_x - 5
			pokemon_trainer.y = previous_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_1)

		if pokemon_trainer.colliderect(HOUSE_2):
			pokemon_trainer.x = previous_x - 5
			pokemon_trainer.y = previous_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(TREE_2):
			pokemon_trainer.x = previous_x - 5
			pokemon_trainer.y = previous_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(TREE_1):
			pokemon_trainer.x = previous_x - 5
			pokemon_trainer.y = previous_y - 0

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :

			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				wild = True
				POKEMON_ENCOUNTER_SOUND.play()
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)


def movement_up (pokemon_trainer, wild) :
	trainer_pokeballs = []

	if not wild: 
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_IMG, trainer_pokeballs ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

		pokemon_trainer.y -= VEL
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x

		if pokemon_trainer.colliderect(HOUSE_1):
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + 3

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_1)

		if pokemon_trainer.colliderect(HOUSE_2):
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + 5

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, HOUSE_2)

		if pokemon_trainer.colliderect(TREE_1):
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + 5

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_1)

		if pokemon_trainer.colliderect(TREE_2):
			pokemon_trainer.x = previous_x - 0
			pokemon_trainer.y = previous_y + 5

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :
			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)


def movement_down (pokemon_trainer, wild) :
	trainer_pokeballs = []
	POKEMON_ENCOUNTER_SOUND.stop()

	if not wild :

		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs ) # Right foot

		pokemon_trainer.y += VEL
		previous_y = pokemon_trainer.y
		previous_x = pokemon_trainer.x

		if pokemon_trainer.colliderect(TREE_1):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - 5

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_1)

		if pokemon_trainer.colliderect(TREE_2):
			pokemon_trainer.x = previous_x
			pokemon_trainer.y = previous_y - 5

			pygame.draw.rect(WIN, WHITE, pokemon_trainer)
			pygame.draw.rect(WIN, WHITE, TREE_2)

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH) or pokemon_trainer.colliderect(GRASS_ZONE_SOUTH_2) or pokemon_trainer.colliderect(GRASS_ZONE_EAST) or pokemon_trainer.colliderect(GRASS_ZONE_WEST) :

			wild_encouter = randint(1, 300)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)

def bicicle_movement_left(pokemon_trainer) :
	VEL = 3
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_IMG, trainer_pokeballs) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_RIGHT_FOOT_IMG , trainer_pokeballs ) # Right foot

	pokemon_trainer.x -= VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(HOUSE_2):
		pokemon_trainer.x = previous_x + 5
		pokemon_trainer.y = previous_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_2):
		pokemon_trainer.x = previous_x + 5
		pokemon_trainer.y = previous_y - 0

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
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)

def bicicle_movement_right(pokemon_trainer) :
	VEL = 3
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_IMG, trainer_pokeballs) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_RIGHT_FOOT_IMG , trainer_pokeballs ) # Right foot

	pokemon_trainer.x += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(HOUSE_1):
		pokemon_trainer.x = previous_x - 5
		pokemon_trainer.y = previous_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_1)

	if pokemon_trainer.colliderect(HOUSE_2):
		pokemon_trainer.x = previous_x - 5
		pokemon_trainer.y = previous_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_2):
		pokemon_trainer.x = previous_x - 5
		pokemon_trainer.y = previous_y - 0

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_2)

	if pokemon_trainer.colliderect(TREE_1):
		pokemon_trainer.x = previous_x - 5
		pokemon_trainer.y = previous_y - 0

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
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)

def bicicle_movement_up (pokemon_trainer) :
	VEL = 3
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y -= VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(HOUSE_1):
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + 5

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_1)

	if pokemon_trainer.colliderect(HOUSE_2):
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + 5

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, HOUSE_2)

	if pokemon_trainer.colliderect(TREE_1):
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + 5

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_1)

	if pokemon_trainer.colliderect(TREE_2):
		pokemon_trainer.x = previous_x - 0
		pokemon_trainer.y = previous_y + 5

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
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)

def bicicle_movement_down (pokemon_trainer) :
	VEL = 3
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y += VEL
	previous_y = pokemon_trainer.y
	previous_x = pokemon_trainer.x

	if pokemon_trainer.colliderect(TREE_1):
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 5

		pygame.draw.rect(WIN, WHITE, pokemon_trainer)
		pygame.draw.rect(WIN, WHITE, TREE_1)

	if pokemon_trainer.colliderect(TREE_2):
		pokemon_trainer.x = previous_x
		pokemon_trainer.y = previous_y - 5

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
			wild = True
			POKEMON_ENCOUNTER_SOUND.play()
			start_battle(wild,previous_x ,previous_y, pokemon_trainer, cursor_pos)

def trainer_movement (keys_pressed, pokemon_trainer) :## Trainer Movement function
	wild = False
	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0 :
		fps = 0
		while fps < 5 :
			movement_left(pokemon_trainer, wild)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80:
		fps = 0
		while fps < 5 :
			movement_right(pokemon_trainer, wild)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up(pokemon_trainer, wild)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down(pokemon_trainer, wild)
			fps +=1

	if keys_pressed[pygame.K_b] :
		TRAINER_IMG = TRAINER_BICICLE_IMG


	if keys_pressed[pygame.K_a]  and pokemon_trainer.x >0:
		TRAINER_IMG = TRAINER_BICICLE_IMG
		fps = 0
		while fps < 5 :
			bicicle_movement_left(pokemon_trainer)
			fps +=1
				
	if keys_pressed[pygame.K_d] and pokemon_trainer.x < WIDTH - 80  :
		TRAINER_IMG = TRAINER_BICICLE_RIGHT_IMG
		fps = 0
		while fps < 5 :
			bicicle_movement_right(pokemon_trainer)
			fps +=1

	if keys_pressed[pygame.K_w]  and pokemon_trainer.y - VEL > 0:
		TRAINER_IMG = TRAINER_BICICLE_BACK_IMG
		fps = 0
		while fps < 5 :
			bicicle_movement_up(pokemon_trainer)
			fps +=1

	if keys_pressed[pygame.K_s] and pokemon_trainer.y - VEL < HEIGHT -100:
		TRAINER_IMG = TRAINER_BICICLE_IMG
		fps = 0
		while fps < 5 :
			bicicle_movement_down(pokemon_trainer)
			fps +=1

		

def create_map(pokemon_trainer, fecha ,POKEBALL_IMG, TRAINER, trainer_pokeballs) :

	if hora <="16" and hora >="10" :
		WIN.blit(ROUTE_IMG, (0,0)) # Place background image

	elif hora >="17" and hora <"20":
		WIN.blit(ROUTE_IMG_2, (0,0)) # Place background image

	else:
		WIN.blit(ROUTE_IMG_3, (0,0)) # Place background image
	


	#pygame.draw.rect(WIN, BLUE, HOUSE_1) # House 1 building
	#pygame.draw.rect(WIN, BLUE, HOUSE_2) # House 2 building

	#pygame.draw.rect(WIN, GREEN, TREE_1) # Tree 1 building
	#pygame.draw.rect(WIN, GREEN, TREE_2) # Tree 2 building

	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH) # Grass zone south
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH_2) # Grass zone south 2
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_WEST) # Grass zone west
	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_EAST) # Grass zone west

	date = POKEBALLS_COUNTER.render("" + str(fecha), 1, WHITE)
	WIN.blit(date, (10, 10))

	pokeball = POKEBALL_ITEM.get_rect()
	pokeball = pygame.Rect(
		pokemon_trainer.x, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 10, 5)


	for pokeball in trainer_pokeballs :
		WIN.blit(POKEBALL_ITEM, (pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 1, 1))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	pygame.display.update()

def throw_pokeball(trainer_pokeballs, pokemon_trainer) :
	for pokeball in trainer_pokeballs:
		pokeball.x += POKEBALL_VEL

		if pokemon_trainer.collidelist(trainer_pokeballs) :
			trainer_pokeballs.remove(pokeball)

		if pokeball.x > WIDTH :
			trainer_pokeballs.remove(pokeball)


def create_title_screen() :

	WIN.blit(TITLE_SCREEN_IMG, (0,0)) # Place background image
	pygame.display.update()



def welcome() :
	start = False
	BACKGROUND_SOUND.play()

	while not start :
		create_title_screen()

		for event in pygame.event.get() :

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_a:
					start = True
					main()
				

def main (): ## Main function

	BACKGROUND_SOUND.stop()


	trainer_pokeballs = []
	free_monster = []
	pokeballs = 5
	pressed = True

	pokemon_trainer = pygame.Rect(100, 300, TRAINER_WIDTH, TRAINER_HEIGHT) # Defines player coords



	clock = pygame.time.Clock()
	run = True
	TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))


	while run :
		clock.tick(FPS)
		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_SPACE and len(trainer_pokeballs) < MAX_POKEBALL:
					pokeball = pygame.Rect(
						pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 1, 1)
					trainer_pokeballs.append(pokeball)
					BACKGROUND_SOUND.stop()
					POKEBALL_SOUND.play()
					BACKGROUND_SOUND.play()

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				TRAINER_IMG = TRAINER_LEFT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )
			
			if keys[pygame.K_RIGHT]:
				TRAINER_IMG = TRAINER_RIGHT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_UP]:
				TRAINER_IMG = TRAINER_BACK_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_DOWN]:
				TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_b]:
				TRAINER_IMG = TRAINER_BICICLE_IMG

			if keys[pygame.K_a]:
				TRAINER_IMG = TRAINER_BICICLE_LEFT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )
				
			if keys[pygame.K_d]:
				TRAINER_IMG = TRAINER_BICICLE_RIGHT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_w]:
				TRAINER_IMG = TRAINER_BICICLE_BACK_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_s]:
				TRAINER_IMG = TRAINER_BICICLE_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs )

			if keys[pygame.K_e]:
				BACKGROUND_SOUND.stop()
				welcome()


		BACKGROUND_SOUND.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement(keys_pressed, pokemon_trainer)
		throw_pokeball(trainer_pokeballs, pokemon_trainer )
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs)

	main()

if __name__ == "__main__":
	welcome()