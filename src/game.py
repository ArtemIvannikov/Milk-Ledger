import time

class Game():
	'''основной класс игры'''
	def __init__(self):
		pass

	def start_new_game(self):
		pass

	def load_game(self):
		pass

	def save_game(self):
		pass

	def update(self):
		# обновление игры при
		current_time = time.time()
		time_passed = (current_time - self.last_save_time) / 3600

		# обновить всех животных
		# собрать молоко
		# потратить корм
		# изменить возраст телят

		self.last_save_time = current_time

	def collect_milk(self, time_passed):
		pass

	def feed_animal(self, time_passed):
		pass 