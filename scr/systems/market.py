import random
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import config
from data import storage
from models import animal


class Market():
	def __init__(self):
		pass


	def create_animal_for_sale(self):
		'''определяет перки, вызывает создание животного '''
		pass

	def generate_random_perks(self):
		'''генерирует из перечня перков рандомный список перков животного '''
		pass


	def generate_starter_shop(self):
		'''использует генератор животных для продажи для создания Х животных'''
		pass

	def buy_animal(self, animal):
		pass

	def sell_animal(self, animal):
		pass

	def calculate_animal_price(self, animal):
		'''получает животного, считает его стоимость по правилам'''
		pass
		