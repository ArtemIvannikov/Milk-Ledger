import random
import config

class Animal():
	'''базовый класс для всех животных'''
	def __init__(self):
		pass

	def age_up(self):
		'''увеличивает возраст животного'''
		pass

	def is_adult(self):
		'''проверяет взрослое ли животное'''
		pass

	def can_breed(self): 
		'''проверяет, может ли животное размножаться'''
		pass

	@staticmethod
	def generate_id_and_name(gender):
		'''
		рождается теленок
		вызывается этот метод
		генерируется уникальный id в формате cow-1234 или bull-1234
		генерируется случайное имя

		'''

	@staticmethod	
	def _generate_name(gender, perks=None):
		'''Генерирует случайное имя'''

	def __get_perk_themed_name(gender, perks=None):
		'''Выбирает случайное прилагательное для перка животного '''
		perk_themed_names = {config.PERK_THEMED_NAMES}

		for perk in perks:
			if perk in perk_themed_names:
				return perk_themed_names[perk][gender]

		

class Cow(Animal):
	def __init__(self):
		pass

	def produce_milk(self):
		'''определение количества произведенного молока'''
		pass


class Bull(Animal):
	def __init__(self):
		pass


class Calf(Animal):
	def __init__(self):
		pass

	def mature_calf(self):
		'''превращает теленка во взрослое животное'''
		pass

