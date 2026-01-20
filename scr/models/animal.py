import random
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

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
        if gender == 'female':
            prefixes = config.FEMALE_PREFIXES
            suffixes = config.FEMALE_SUFFIXES
            full_names = config.FEMALE_FULLNAMES
        elif gender == 'male':
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
    def _get_perk_themed_name(gender, perks=None):
        '''Выбирает случайное прилагательное для перка животного '''
        perk_themed_names = config.PERK_THEMED_NAMES

        if not perks:
            return ['Обычный'] if gender == 'male' else ['Обычная']
            

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

