import random
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import config
from data import storage

class Animal():
    '''базовый класс для всех животных'''
    def __init__(self, id: int, name, type, gender, rarity, perks: list):
        self.db = storage.Storage(config.PATH)
        self.name = name
        self.rarity = rarity
        self.perks = perks
        self.id = id
        self.location_type = None
        self.type = type
        self.gender = gender
        self.milk_per_day = None
        self.maturity_hours_left = None

    def age_up(self):
        '''увеличивает возраст животного'''
        pass

    def is_adult(self):
        '''проверяет взрослое ли животное'''
        pass

    def can_breed(self) -> bool: 
        '''проверяет, может ли животное размножаться'''
        return True 

    @staticmethod
    def create_new_animal(storage, **details): #WARNING NOT WORK
        '''создает взрослое животное для покупки в магазине'''
        new_animal_id = storage.get_next_animal_id()
        gender = details['gender']
        animal_type = details['type']
        perks = details['perks']
        rarity = details['rarity']
        new_animal_name = Animal._generate_name(gender, perks)
      
        match animal_type:
            case 'cow':
                animal = Cow(id=new_animal_id, name=new_animal_name, 
                            type=animal_type, gender=gender, rarity=rarity,
                            perks=perks, 
                            milk_per_day=details['milk_per_day'], is_pregnant=0)
                return animal

            case 'bull':
                animal = Bull(id=new_animal_id, name=new_animal_name, 
                            type=animal_type, gender=gender, rarity=rarity, perks=perks)
                return animal

            case 'calf':
                animal = Calf(id=new_animal_id, name=new_animal_name, 
                            type=animal_type, gender=gender, rarity=rarity, perks=perks,
                            maturity_hours_left=config.MATURITY_HOURS_LEFT) 
                return animal
        


    @staticmethod   
    def _generate_name(gender, perks=None):
        '''Генерирует случайное имя'''

        if gender == 'female':
            prefixes = config.FEMALE_PREFIXES
            suffixes = config.FEMALE_SUFFIXES
            full_names = config.FEMALE_FULLNAMES
        else:
            prefixes = config.MALE_PREFIXES
            suffixes = config.MALE_SUFFIXES
            full_names = config.MALE_FULLNAMES

        if random.random() < 0.3: #Full name choice
            if random.random() < 0.3: #full + themed
                perk_name = random.choice(Animal._get_perk_themed_name(gender, perks))
                return perk_name + ' ' + random.choice(full_names)
            else:
                return random.choice(full_names)
        else: #custom name choice
            random_name = random.choice(prefixes) + random.choice(suffixes)
            if random.random() < 0.3: #custom + themed
                perk_name = random.choice(Animal._get_perk_themed_name(gender, perks))
                return perk_name + ' ' + random_name
            else:
                return random_name

    @staticmethod
    def _get_perk_themed_name(gender, perks):
        '''Выбирает случайное прилагательное для перка животного '''
        perk_themed_names = config.PERK_THEMED_NAMES

        if not perks:
            return ['Обычный'] if gender == 'male' else ['Обычная']
            

        for perk in perks:
            if perk in perk_themed_names:
                return perk_themed_names[perk][gender]



        

class Cow(Animal):
    def __init__(self, id: int, name, type, gender, rarity, perks: list, milk_per_day, is_pregnant):
        super().__init__(id, name, type, gender, rarity, perks)
        self.is_pregnant = is_pregnant
        self.milk_per_day = milk_per_day
    def __repr__(self):
        return f"получилась {self.__class__.__name__} {self.name} {self.rarity}"

    def produce_milk(self):
        '''определение количества произведенного молока'''
        pass

    def can_breed(self):
        if self.is_pregnant == 0:
            return True
        else:
            return False
        


class Bull(Animal):

    def __repr__(self):
        return f"получился {self.__class__.__name__} {self.name} {self.rarity} с перками {self.perks}"


class Calf(Animal):
    def __init__(self, id: int, name, type, gender, rarity, perks: list, maturity_hours_left):
        super().__init__(id, name, type, gender, rarity, perks)
        self.maturity_hours_left = maturity_hours_left
        

    def __repr__(self):
        return f"получился  {self.__class__.__name__} {self.name} {self.rarity}"

    def can_breed(self):
        return False

    def mature_calf(self):
        '''превращает теленка во взрослое животное'''
        pass

