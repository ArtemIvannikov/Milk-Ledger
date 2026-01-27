import random
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import config
from data import storage
from models.animal import Animal


class Market():
	def __init__(self):
		self.storage = storage.Storage(config.PATH)


	def _create_animal_for_sale(self, type, gender):
		'''определяет перки, вызывает создание животного '''
		rarity = random.choices(('common', 'rare', 'epic'), weights=[0.6, 0.3, 0.1], k=1)[0]
		perks = self._generate_random_perks(rarity)
		details = {
			'gender': gender,
			'type': type,
			'perks': perks,
			'rarity': rarity,
			'milk_per_day': 0,
			'maturity_hours_left': 0,
			'location_type': 'market',
		}

		match type:
			case 'bull':
				pass

			case 'cow':
				rarity_to_milk = {
				'common': 10,
				'rare'  : 15,
				'epic'  : 20,
				}
				details['milk_per_day'] = rarity_to_milk[rarity]

			case 'calf':
				details['maturity_hours_left'] = config.MATURITY_HOURS_LEFT

		new_animal = Animal.create_new_animal(storage=self.storage, **details)
		self.storage.save_animal(new_animal)

		print(new_animal)

		return new_animal

	def _generate_random_perks(self, rarity):
		'''генерирует из перечня перков рандомный список перков животного '''
		animal_rarity_to_perks = {
			'common': range(2),
			'rare'  : range(1, 3),
			'epic'  : range(2, 4),
		}
		self.quantity_of_perks = random.choice(animal_rarity_to_perks[rarity])
		
		return self.storage.get_list_perks(self.quantity_of_perks)


	def generate_starter_shop(self):
		'''использует генератор животных для продажи для создания Х животных'''
		starter_pack = config.STARTER_PACK

		for bull in range(starter_pack['bull']):
			self._create_animal_for_sale('bull', 'male') 

			# TODO дописать сохранение в базу данных(табл МАГАЗИН)
		for cow in range(starter_pack['cow']):
			self._create_animal_for_sale('cow', 'female')

		print(3333)

	def buy_animal(self, animal):
		pass

	def sell_animal(self, animal):
		pass

	def calculate_animal_price(self, animal):
		'''получает животного, считает его стоимость по правилам'''
		pass
		

animal_rarity_for_perks = {
			'common': range(2),
			'rare'  : range(3),
			'epic'  : range(4),
		}

s = Market()
s._generate_random_perks('rare')
# s._create_animal_for_sale('bull', 'male')
s.generate_starter_shop()