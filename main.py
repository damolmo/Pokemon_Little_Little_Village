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
FPS = 30
VEL = 2
WHITE = (255,255,255)
today = date.today()
fecha = today.strftime("%B %d, %Y")
now = datetime.now()
hora = now.strftime("%H:%M")



## Map Values
WIDTH, HEIGHT = 900, 507 # Map dimentions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Draws the map with given dimentions
pygame.display.set_caption("Pokémon Pi - Route")

## Map elements
HOUSE_1 = pygame.Rect(WIDTH//2 -10, 0 ,100 , HEIGHT  )

## Character Values
TRAINER_WIDTH, TRAINER_HEIGHT = 64, 76


## Game Events
THROW_POKEBALL = pygame.USEREVENT +1

## Assets

# Trainer
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
PIKACHU_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "pikachu.gif")), (TRAINER_WIDTH, TRAINER_HEIGHT))

# Background
ROUTE_IMG = pygame.image.load(os.path.join('Assets', "background.png"))

# Music
BACKGROUND_SOUND = pygame.mixer.Sound("Assets/music.mp3")

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

def movement_left (pokemon_trainer) :
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_IMG, trainer_pokeballs) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.x -= VEL

def movement_right (pokemon_trainer) :
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_RIGHT_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.x += VEL

def movement_up (pokemon_trainer) :
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BACK_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y -= VEL

def movement_down (pokemon_trainer) :
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y += VEL

def bicicle_movement_left(pokemon_trainer) :
	VEL = 4
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_IMG, trainer_pokeballs) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_RIGHT_FOOT_IMG , trainer_pokeballs ) # Right foot

	pokemon_trainer.x -= VEL

def bicicle_movement_right(pokemon_trainer) :
	VEL = 4
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_IMG, trainer_pokeballs) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_RIGHT_FOOT_IMG , trainer_pokeballs ) # Right foot

	pokemon_trainer.x += VEL

def bicicle_movement_up (pokemon_trainer) :
	VEL = 4
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_BACK_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y -= VEL

def bicicle_movement_down (pokemon_trainer) :
	VEL = 4
	trainer_pokeballs = []
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_IMG, trainer_pokeballs ) # All Foots
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_LEFT_FOOT_IMG, trainer_pokeballs ) # Left foot
	create_map(pokemon_trainer, fecha,POKEBALL_IMG, TRAINER_BICICLE_RIGHT_FOOT_IMG, trainer_pokeballs ) # Right foot

	pokemon_trainer.y += VEL




def trainer_movement (keys_pressed, pokemon_trainer) :## Trainer Movement function

	trainer_pokeballs = []

	if keys_pressed[pygame.K_LEFT] and pokemon_trainer.x >0:
		fps = 0
		while fps < 5 :
			movement_left(pokemon_trainer)
			fps +=1

	if keys_pressed[pygame.K_RIGHT] and pokemon_trainer.x < WIDTH - 80  :
		fps = 0
		while fps < 5 :
			movement_right(pokemon_trainer)
			fps +=1

	if keys_pressed[pygame.K_UP] and pokemon_trainer.y - VEL > 0 :
		fps = 0
		while fps < 5 :
			movement_up(pokemon_trainer)
			fps +=1
		
	if keys_pressed[pygame.K_DOWN] and pokemon_trainer.y - VEL < HEIGHT -100 :
		fps = 0
		while fps < 5 :
			movement_down(pokemon_trainer)
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
	WIN.blit(ROUTE_IMG, (0,0))

	rules_1 = RULES.render("UP/DOWN/LEFT/RIGHT - Move", 1, WHITE)
	rules_2 = RULES.render("W/S/A/D - Bicicle", 1, WHITE)
	rules_3 = RULES.render("Space - Pokeball", 1, WHITE)

	WIN.blit(rules_1, (WIDTH - rules_1.get_width() - 10, 20))
	WIN.blit(rules_2, (WIDTH - rules_2.get_width() - 171, 40))
	WIN.blit(rules_3, (WIDTH - rules_3.get_width() - 200, 60))

	date = POKEBALLS_COUNTER.render("" + str(fecha), 1, WHITE)
	WIN.blit(date, (10, 10))

	WIN.blit(TRAINER, (pokemon_trainer.x, pokemon_trainer.y))

	pokeball = POKEBALL_ITEM.get_rect()
	pokeball = pygame.Rect(
		pokemon_trainer.x, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 10, 5)

	for pokeball in trainer_pokeballs :
		WIN.blit(POKEBALL_ITEM, (pokemon_trainer.x + pokemon_trainer.width, pokemon_trainer.y + pokemon_trainer.height//2 - 2, 1, 1))

	pygame.display.update()

def throw_pokeball(trainer_pokeballs, pokemon_trainer) :
	for pokeball in trainer_pokeballs:
		pokeball.x += POKEBALL_VEL

		if pokemon_trainer.colliderect(pokeball):
			trainer_pokeballs.remove(pokeball)

		if pokeball.x > WIDTH :
			trainer_pokeballs.remove(pokeball)



def main (): ## Main function

	pokemon_trainer = pygame.Rect(100, 300, TRAINER_WIDTH, TRAINER_HEIGHT) # Defines player rectangle
	trainer_pokeballs = []
	free_monster = []
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