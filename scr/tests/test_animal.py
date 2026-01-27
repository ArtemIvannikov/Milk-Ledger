import os
import sys
import unittest


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from models.animal import Animal
import config
from data import storage

class Tests(unittest.TestCase):
	
	def test_get_perk_themed_name1(self):
		result = Animal._get_perk_themed_name('male', ['Супер-Удой'])
		print(f"Male with 'Супер-Удой': {result}")
		self.assertEqual(result, ['Породистый', 'Элитный', 'Отборный'])

	def test_get_perk_themed_name2(self):
		result = Animal._get_perk_themed_name('female', ['Супер-Удой'])
		print(f"Female with 'Супер-Удой': {result}")
		self.assertEqual(result, ['Молочница', 'Удойная', 'Продуктивная', 'Щедрая'])

	def test_get_perk_themed_name3(self):
		result = Animal._get_perk_themed_name('female', None)
		print(f"Female with 'Супер-Удой': {result}")
		self.assertEqual(result, ['Обычная'])


	def test_generate_name(self):
		result = Animal._generate_name('male', ['Супер-Удой'])
		print(f"Male with 'Супер-Удой': {result}")
		self.assertIsNotNone(result)

	def test_create_new_animal_cow(self):
		self.storage = storage.Storage(config.PATH)
		details = {
			'gender': 'female',
			'type': 'cow',
			'perks': ['Супер-Удой'],
			'milk_per_day': 10,
			'rarity': 'common',
		}

		result = Animal.create_new_animal(self.storage, **details)
		print(result)


	def test_create_new_animal_bull(self):
		self.storage = storage.Storage(config.PATH)
		details = {
			'gender': 'male',
			'type': 'bull',
			'perks': ['Супер-Удой'],
			'rarity': 'common',
		}

		result = Animal.create_new_animal(self.storage, **details)
		print(getattr(result, 'id'))
		print(result)

	def test_create_new_animal_calf(self):
		self.storage = storage.Storage(config.PATH)
		details = {
			'gender': 'female',
			'type': 'calf',
			'perks': ['Супер-Удой'],
			'milk_per_day': 10,
			'rarity': 'common',
		}

		result = Animal.create_new_animal(self.storage, **details)
		print(result)

if __name__ == '__main__':
    # Запуск всех тестов
    unittest.main(verbosity=2)
    