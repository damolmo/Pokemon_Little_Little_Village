import pygame
from resources import *

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

def throw_pokeball(trainer_pokeballs, pokemon_trainer, free_pika) :
	for pokeball in trainer_pokeballs:
		pokeball.x += POKEBALL_VEL

		if pokeball.x < WIDTH :
			trainer_pokeballs.remove(pokeball)

	free_pika +=1