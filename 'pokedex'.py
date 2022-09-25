print('Welcome to the Pokedex \n \t We are always adding more pokemon.')

#type
none = 'none'
fire = 'fire'
water = 'water'
grass = 'grass'
electric = 'electric'
normal = 'normal'
poison = 'poison'
flying = 'flying'

#pokemon
bulbasaur = 'Bulbasaur'	
ivysaur = 'Ivysaur'
venasaur = 'Venasaur'
squirtle = 'Squirtle'
wartortle = 'Wartortle'
blastoise = 'Blastoise'
charmander = 'Charmander'
charmeleon = 'Charmeleon'
charizard = 'Charizard'					

def pokemonFind(name):

		#pokemon
	if bulbasaur in name:
		type1 = grass	
	elif ivysaur in name:
		type1 = grass
		type2 = poison
	elif venasaur in name:
		type1 = grass
		type2 = poison
		
	if squirtle in name:
		type1 = water
		type2 = none
	elif wartortle in name:
		type1 = water
		type2 = none
	elif blastoise in name:
		type1 = water
		type2 = none
		
	if charmander in name:
		type1 = fire
		type2 = none
	elif charmeleon in name:
		type1 = fire
		type2 = none
	elif charizard in name:
		type1 = fire
		type2 = flying
		
		#first types
	if type1 in fire:
		print(name + ' is a fire type')
	elif type1 in water:
		print(name + ' is a water type')
	elif type1 in grass:
		print(name + ' is a grass type')
	elif type1 in flying:
		print(name + ' is a flying type')
	elif type1 in poison:
		print(name + ' is a poison type')
		
		#second types
	if type2 in fire:
		print(name + ' is also a fire type')
	elif type2 in water:
		print(name + ' is also a water type')
	elif type2 in grass:
		print(name + ' is also a grass type')
	elif type2 in flying:
		print(name + ' is also a flying type')
	elif type2 in poison:
		print(name + ' is also a poison type')



pokemonFind(squirtle)


