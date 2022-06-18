import os
import json
from resources import *

def save_game () :
	my_save_slot = json.dumps(variables)
	with open('save.json', 'w') as save:
		save.write(my_save_slot)

