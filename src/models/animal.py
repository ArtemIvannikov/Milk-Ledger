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

