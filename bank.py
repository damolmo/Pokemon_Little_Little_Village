from resources import *

def access_bank () :
	bank = True
	cursor_pos.x = 100
	cursor_pos.y = 20

	while bank :
		create_bank()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_BACKSPACE :
					pokemon_trainer.y += 40
					bank = False


				if event.key == pygame.K_RIGHT and cursor_pos.x < 800 :
							cursor_pos.x+=100

				if event.key == pygame.K_LEFT and cursor_pos.x > 100 :
							cursor_pos.x-=100

				if event.key == pygame.K_UP and cursor_pos.y > 20 :
							cursor_pos.y-=125

				if event.key == pygame.K_DOWN and cursor_pos.y < 295 :
							cursor_pos.y+=125


def create_bank () :
	WIN.blit(CENTER_BANK_IMG, (0,0))
	WIN.blit(CURSOR, (cursor_pos.x, cursor_pos.y))
	pygame.display.update()
