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
VEL = 3
WHITE = (255,255,255)
BLUE = (0,0,204)
GREEN = (0, 204, 102)
today = date.today()
fecha = today.strftime("%B %d, %Y")
now = datetime.now()
hora = now.strftime("%H:%M")


## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Draws the map with given dimentions
pygame.display.set_caption("Pokémon Pi - Route")

## Map elements
HOUSE_1 = pygame.Rect(650, 20, 220, 250)
HOUSE_2 = pygame.Rect(90, 0, 280, 180)
TREE_1 = pygame.Rect(500, 140, 120, 120)
TREE_2 = pygame.Rect(230, 280, 120, 120)
GRASS_ZONE_SOUTH = pygame.Rect(320, 390, 500, 120)

## Character Values
TRAINER_WIDTH, TRAINER_HEIGHT = 64, 76


## Game Events
THROW_POKEBALL = pygame.USEREVENT +1
clock = pygame.time.Clock()

## Assets

# Trainer
pokemon_trainer = pygame.Rect(100, 300, TRAINER_WIDTH, TRAINER_HEIGHT) # Defines player coords
previous_x, previous_y = 100, 300
x_change, y_change = 0, 0

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


# Pikachu
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

# Background
ROUTE_IMG = pygame.image.load(os.path.join('Assets', "background.png"))
BATTLE_ARENA_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "battle_arena.png")), (WIDTH, HEIGHT))
ASH_BATTLE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash_battle_1.png")), (300,300))

# Music
BACKGROUND_SOUND = pygame.mixer.Sound("Assets/music.mp3")
POKEMON_ENCOUNTER_SOUND = pygame.mixer.Sound("Assets/pokemon_encounter.mp3")
GRASS_SOUND = pygame.mixer.Sound("Assets/grass.mp3")

# Pokeball
POKEBALL_IMG = pygame.image.load(os.path.join('Assets', "pokeball.png"))
POKEBALL_ITEM = pygame.image.load(os.path.join('Assets', "pokeball_item.png"))
POKEBALL_SOUND = pygame.mixer.Sound("Assets/pokeball_out.mp3")
MAX_POKEBALL = 3
POKEBALL_VEL = 3
POKEBALL_ITEM.convert()

# Displat Fonts
POKEBALLS_COUNTER = pygame.font.SysFont('comicsans', 50)
RULES = pygame.font.SysFont('comicsans', 25)

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

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH):
			wild = False
			BACKGROUND_SOUND.stop()
			GRASS_SOUND.play()

			wild_encouter = randint(1, 100)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer)


def create_area (POKEMON) :

	WIN.blit(BATTLE_ARENA_IMG, (0,0)) # Place background image


	#pygame.draw.rect(WIN, BLUE, HOUSE_1) # House 1 building
	#pygame.draw.rect(WIN, BLUE, HOUSE_2) # House 2 building

	#pygame.draw.rect(WIN, GREEN, TREE_1) # Tree 1 building
	#pygame.draw.rect(WIN, GREEN, TREE_2) # Tree 2 building

	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH) # Grass zone south

	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 10, 10))
	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 65, 10))
	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 120, 10))

	WIN.blit(ASH_BATTLE_IMG, (0,250))
	WIN.blit(POKEMON, (640,160))

	warning = POKEBALLS_COUNTER.render("Un Pokemon Salvaje ha aparecido!", 1, WHITE)
	WIN.blit(warning, (0, 0))

	choice = POKEBALLS_COUNTER.render("(B) Run", 1, WHITE)
	WIN.blit(choice, (WIDTH//2 , 150))

	pygame.display.update()

def create_Pikachu () :
	create_area(PIKACHU_IMG_1)
	create_area(PIKACHU_IMG_2)
	create_area(PIKACHU_IMG_3)
	create_area(PIKACHU_IMG_4)
	create_area(PIKACHU_IMG_5)
	create_area(PIKACHU_IMG_6)
	create_area(PIKACHU_IMG_7)
	create_area(PIKACHU_IMG_8)
	create_area(PIKACHU_IMG_9)
	create_area(PIKACHU_IMG_10)
	create_area(PIKACHU_IMG_11)
	create_area(PIKACHU_IMG_12)
	create_area(PIKACHU_IMG_13)
	create_area(PIKACHU_IMG_14)
	create_area(PIKACHU_IMG_15)
	create_area(PIKACHU_IMG_16)
	create_area(PIKACHU_IMG_17)
	create_area(PIKACHU_IMG_18)
	create_area(PIKACHU_IMG_19)
	create_area(PIKACHU_IMG_20)
	create_area(PIKACHU_IMG_21)
	create_area(PIKACHU_IMG_22)
	create_area(PIKACHU_IMG_23)
	create_area(PIKACHU_IMG_24)
	create_area(PIKACHU_IMG_25)
	create_area(PIKACHU_IMG_26)
	create_area(PIKACHU_IMG_27)
	create_area(PIKACHU_IMG_28)
	create_area(PIKACHU_IMG_29)
	create_area(PIKACHU_IMG_30)
	create_area(PIKACHU_IMG_31)
	create_area(PIKACHU_IMG_32)
	create_area(PIKACHU_IMG_33)
	create_area(PIKACHU_IMG_34)
	create_area(PIKACHU_IMG_35)
	create_area(PIKACHU_IMG_36)
	create_area(PIKACHU_IMG_37)
	create_area(PIKACHU_IMG_38)
	create_area(PIKACHU_IMG_39)
	create_area(PIKACHU_IMG_40)
	create_area(PIKACHU_IMG_41)
	create_area(PIKACHU_IMG_42)
	create_area(PIKACHU_IMG_43)
	create_area(PIKACHU_IMG_44)
	create_area(PIKACHU_IMG_45)
	create_area(PIKACHU_IMG_46)
	create_area(PIKACHU_IMG_47)
	create_area(PIKACHU_IMG_48)
	create_area(PIKACHU_IMG_49)
	create_area(PIKACHU_IMG_50)
	create_area(PIKACHU_IMG_51)
	create_area(PIKACHU_IMG_52)
	create_area(PIKACHU_IMG_53)
	create_area(PIKACHU_IMG_54)
	create_area(PIKACHU_IMG_55)
	create_area(PIKACHU_IMG_56)
	create_area(PIKACHU_IMG_57)
	create_area(PIKACHU_IMG_58)
	create_area(PIKACHU_IMG_59)
	create_area(PIKACHU_IMG_60)
	create_area(PIKACHU_IMG_61)
	create_area(PIKACHU_IMG_62)
	create_area(PIKACHU_IMG_63)
	create_area(PIKACHU_IMG_64)
	create_area(PIKACHU_IMG_65)
	create_area(PIKACHU_IMG_66)
	create_area(PIKACHU_IMG_67)
	create_area(PIKACHU_IMG_68)
	create_area(PIKACHU_IMG_69)
	create_area(PIKACHU_IMG_70)
	create_area(PIKACHU_IMG_71)
	create_area(PIKACHU_IMG_72)
	create_area(PIKACHU_IMG_73)
	create_area(PIKACHU_IMG_74)
	create_area(PIKACHU_IMG_75)
	create_area(PIKACHU_IMG_76)
	create_area(PIKACHU_IMG_77)
	create_area(PIKACHU_IMG_78)
	create_area(PIKACHU_IMG_79)
	create_area(PIKACHU_IMG_80)
	create_area(PIKACHU_IMG_81)
	create_area(PIKACHU_IMG_82)
	create_area(PIKACHU_IMG_83)
	create_area(PIKACHU_IMG_84)
	create_area(PIKACHU_IMG_85)
	create_area(PIKACHU_IMG_86)
	create_area(PIKACHU_IMG_87)
	create_area(PIKACHU_IMG_88)
	create_area(PIKACHU_IMG_89)
	create_area(PIKACHU_IMG_90)
	create_area(PIKACHU_IMG_91)
	create_area(PIKACHU_IMG_92)
	create_area(PIKACHU_IMG_93)
	create_area(PIKACHU_IMG_94)
	create_area(PIKACHU_IMG_95)
	create_area(PIKACHU_IMG_96)
	create_area(PIKACHU_IMG_97)
	create_area(PIKACHU_IMG_98)
	create_area(PIKACHU_IMG_99)
	create_area(PIKACHU_IMG_100)
	create_area(PIKACHU_IMG_101)
	create_area(PIKACHU_IMG_102)
	create_area(PIKACHU_IMG_103)
	create_area(PIKACHU_IMG_104)
	create_area(PIKACHU_IMG_105)
	create_area(PIKACHU_IMG_106)
	create_area(PIKACHU_IMG_107)
	create_area(PIKACHU_IMG_108)
	create_area(PIKACHU_IMG_109)
	create_area(PIKACHU_IMG_110)
	create_area(PIKACHU_IMG_111)
	create_area(PIKACHU_IMG_112)

def random_pokemon () :

	wild_appeared = 0
	pokemon_route = [1,1,1,1]
	wild_appeared = random.choice(pokemon_route)

	if wild_appeared == 1 :
		create_Pikachu()


def start_battle(wild,x ,y, pokemon_trainer) :
	GRASS_SOUND.stop()
	BACKGROUND_SOUND.stop()
	POKEMON_ENCOUNTER_SOUND.play()

	
	keys = pygame.key.get_pressed()

	while wild:
		random_pokemon()

		for event in pygame.event.get() :

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_b :
					wild = False
					print("HAS HUIDO")
					movement_down (pokemon_trainer, wild)

	
			



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

		if pokemon_trainer.colliderect(GRASS_ZONE_SOUTH):
			BACKGROUND_SOUND.stop()
			GRASS_SOUND.play()

			wild_encouter = randint(1, 100)

			if wild_encouter == 95 :
				previous_x = pokemon_trainer.x
				previous_y = pokemon_trainer.y
				wild = True
				start_battle(wild,previous_x ,previous_y, pokemon_trainer)


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

def bicicle_movement_left(pokemon_trainer) :
	VEL = 4
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

def bicicle_movement_right(pokemon_trainer) :
	VEL = 4
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

def bicicle_movement_up (pokemon_trainer) :
	VEL = 4
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

def bicicle_movement_down (pokemon_trainer) :
	VEL = 4
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

	WIN.blit(ROUTE_IMG, (0,0)) # Place background image


	#pygame.draw.rect(WIN, BLUE, HOUSE_1) # House 1 building
	#pygame.draw.rect(WIN, BLUE, HOUSE_2) # House 2 building

	#pygame.draw.rect(WIN, GREEN, TREE_1) # Tree 1 building
	#pygame.draw.rect(WIN, GREEN, TREE_2) # Tree 2 building

	#pygame.draw.rect(WIN, GREEN, GRASS_ZONE_SOUTH) # Grass zone south

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



def main (): ## Main function

	# Download Game Resources


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


		BACKGROUND_SOUND.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement(keys_pressed, pokemon_trainer)
		throw_pokeball(trainer_pokeballs, pokemon_trainer )
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs)

	main()

if __name__ == "__main__":
	main()