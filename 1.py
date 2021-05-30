

class Planet(object):
	"""docstring for Planet"""
	def __init__(self, population = []):
		self.population = population

	def add_population(self, new_population):
		self.population += new_population

	def add_animal(self, animal):
		self.population.append(animal)

	def __str__(self):
		s = ""
		for animal in self.population:
			s += 'Type: ' + animal.animal_type + ' Name: ' + animal.name + '\n'
		return s


class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name

class Cat(Animal):
	"""docstring for Cat"""
	animal_type = 'cat'
	hungry = 0
	happiness = 100

	def meow(self):
		print('meow')



class Dog(Animal):
	"""docstring for Dog"""
	animal_type = 'dog'
	hungry = 0
	happiness = 100

	def wof(self):
		print('wof')



class Tiger(Animal):
	"""docstring for Tiger"""
	animal_type = 'tiger'
	hungry = 0
	happiness = 100

	def rrr(self):
		print('rrr')


earth = Planet()

earth.add_population([Cat('Max'), Dog('Shiba'), Tiger('Tiger')])

print(earth)
		
		
		