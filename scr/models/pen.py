class Pen():
	'''загон для коров'''
	def __init__(self, width, height, storage):
		self.width = width
		self.height = height
		self.grid = [[None for _ in range(width)] for _ in range(height)]

	def add_animal(self, animal, x, y, location_type):
		'''размещает животное в загон'''
		#проверка логики
		if not self._is_valid_position(x, y):
			raise ValueError("Invalid Position")
		if self.grid[y][x] is not None:
			raise ValueError("Cell is not empty")

		self.grid[y][x] = animal

		self.storage.update_animal_position(animal.id, x, y, location_type)

	def remove_animal(self, x, y):
		'''удаляет животное из загона'''
		animal = self.grid[y][x]

		if animal:
			self.grid[y][x] = None
			self.storage.update_animal_position(animal.id, None, None, location_type)
		return animal

	def find_empty_cells(self):
		# находит свободные загоны
		pass

	def is_adjecent(self, pos1, pos2):
		# проверяет, соседние ли клетки к текущей
		pass

	def get_adjecent_cells(self, pos1, pos2):
		# возвращает соседние к текущей клетки
		pass


class CowPen(Pen):
	def __init__(self, width, height, storage):
		super().__init__(self, width, height, storage):

	def add_animal(self, animal, x, y, location_type):
		super().add_animal(self, animal, x, y, location_type='pen')

class BullPen(Pen):
	def __init__(self, width, height, storage):
		super().__init__(self, width, height, storage):

	def add_animal(self, animal, x, y, location_type):
		super().add_animal(self, animal, x, y, location_type='bull_pen')


