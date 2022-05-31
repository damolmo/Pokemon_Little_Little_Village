# Pokemon Pi
# Fan Game powered by Python and Pygame
# Credits to Pygame for the libs

import os

os.system("pip3 install pygame")
os.system("pip install pygame")
os.system("pip3.10 install pygame")

import pygame
import time
from datetime import date
from datetime import datetime

pygame.font.init() # Import font
pygame.mixer.init() # Import sounds

## Game Values
FPS = 60
VEL = 6
WHITE = (255,255,255)
today = date.today()
fecha = today.strftime("%B %d, %Y")
now = datetime.now()
hora = now.strftime("%H:%M")



## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Draws the map with given dimentions
pygame.display.set_caption("Pokémon Pi - Route")

## Character Values
TRAINER_WIDTH, TRAINER_HEIGHT = 64, 76


## Game Events
THROW_POKEBALL = pygame.USEREVENT +1

## Assets

# Trainer
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

# Background
ROUTE_IMG = pygame.image.load(os.path.join('Assets', "background.png"))

# Music
BACKGROUND_SOUND = pygame.mixer.Sound("Assets/music.mp3")

# Pokeball
POKEBALL_IMG = pygame.image.load(os.path.join('Assets', "pokeball.png"))


# Displat Fonts
POKEBALLS_COUNTER = pygame.font.SysFont('comicsans', 50)

def trainer_movement (keys_pressed, pokemon_trainer) :## Trainer Movement function

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0:
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_RIGHT_FOOT_IMG ) # Right foot

		pokemon_trainer.x -= VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_RIGHT_FOOT_IMG ) # Right foot

		pokemon_trainer.x -= VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_IMG ) # All Foots

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80  :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_RIGHT_FOOT_IMG ) # Right foot

		pokemon_trainer.x += VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_RIGHT_FOOT_IMG ) # Right foot
		
		pokemon_trainer.x += VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_RIGHT_IMG ) # All Foots


	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_RIGHT_FOOT_IMG ) # Right foot

		pokemon_trainer.y -= VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,  TRAINER_BACK_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_RIGHT_FOOT_IMG ) # Right foot

		pokemon_trainer.y -= VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_BACK_IMG ) # All Foots


		

	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG ) # Right foot

		pokemon_trainer.y += VEL

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG ) # All Foots
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_LEFT_FOOT_IMG ) # Left foot
		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG ) # Right foot

		create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG ) # All Foots

		pokemon_trainer.y += VEL
		


def create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER) :
	WIN.blit(ROUTE_IMG, (0,0))

	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 10, 10))
	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 65, 10))
	pokeball = POKEBALL_IMG
	WIN.blit(POKEBALL_IMG, (WIDTH - pokeball.get_width() - 120, 10))

	date = POKEBALLS_COUNTER.render("" + str(fecha), 1, WHITE)
	WIN.blit(date, (10, 10))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	pygame.display.update()


def main (): ## Main function

	pokemon_trainer = pygame.Rect(100, 300, TRAINER_WIDTH, TRAINER_HEIGHT) # Defines player rectangle
	trainer_pokeballs = []
	pokeballs = 5
	pressed = True


	clock = pygame.time.Clock()
	run = True
	TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))


	while run :
		clock.tick(FPS)
		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				TRAINER_IMG = TRAINER_LEFT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG )
			
			if keys[pygame.K_RIGHT]:
				TRAINER_IMG = TRAINER_RIGHT_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG )

			if keys[pygame.K_UP]:
				TRAINER_IMG = TRAINER_BACK_IMG
				create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG )

			if keys[pygame.K_DOWN]:
				TRAINER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "ash.png")), (TRAINER_WIDTH, TRAINER_HEIGHT))
				create_map(pokemon_trainer, fecha,POKEBALL_IMG,   TRAINER_IMG )

			


		BACKGROUND_SOUND.play()
		keys_pressed = pygame.key.get_pressed()
		trainer_movement(keys_pressed, pokemon_trainer)
		create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG)

	main()

if __name__ == "__main__":
	main()