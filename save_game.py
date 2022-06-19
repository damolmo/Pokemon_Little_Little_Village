import os
import json
from resources import *
from main import *

def save_game () :

	saving = True
	my_save_slot = json.dumps(variables)
	with open('save.json', 'w') as save:
		save.write(my_save_slot)

	while saving :
		create_save_windows()
		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_a :
					saving = False

def create_save_windows () :
	WIN.blit(DIALOG_MENU, (0, 300))
	message = POKEBALLS_COUNTER.render("Saved your data...", 1, WHITE)
	WIN.blit(message, (120, 370))
	message = POKEBALLS_COUNTER.render("Press (A) to continue.", 1, WHITE)
	WIN.blit(message, (120, 450))

	pygame.display.update()

