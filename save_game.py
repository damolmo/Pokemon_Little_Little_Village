import os
import json

# Player values
my_save_slot = open("save.json")
variables = json.load(my_save_slot)

def save_game () :
	my_save_slot = json.dumps(variables)
	with open('save.json', 'w') as save:
		save.write(my_save_slot)

