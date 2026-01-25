import os
import sqlite3
from sqlite3 import Error
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import config


class Storage():
    def __init__(self, path):
        self.database_path = path
        self.connection = None
        self.cursor = None
        self.connect_database()
        self.create_tables()
        self.init_or_update_perks_table(config.PERKS)


    def connect_database(self):
        # path(self.database_path).parent.mkdir(parents=True, EXISTS_ok=True)
        try:
            self.connection = sqlite3.connect(self.database_path)
        except Error:
            print(Error)
        # self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.connection.commit()

        


    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS perks (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                effect_type TEXT,
                effect_value REAL,
                rarity TEXT
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animal_perks (
                animal_id INTEGER NOT NULL, 
                perk_id INTEGER NOT NULL,
                PRIMARY KEY (animal_id, perk_id),
                FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE,
                FOREIGN KEY (perk_id) REFERENCES perks(id)
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                type TEXT NOT NULL, 
                gender TEXT NOT NULL,
                age REAL DEFAULT 0, 
                birth_timestamp REAL NOT NULL,

                milk_per_day REAL DEFAULT 0,
                is_pregnant BOOLEAN DEFAULT 0,
                pregnancy_hours_left REAL DEFAULT 0,

                maturity_hours_left REAL DEFAULT 0,

                father_id TEXT,
                mother_id TEXT,

                is_alive BOOLEAN DEFAULT 1,
                location_type TEXT, 
                pen_x INTEGER,
                pen_y INTEGER,

                is_owned BOOLEAN DEFAULT 1,  
                sold_timestamp REAL,         
                sold_price REAL,             
                  

                FOREIGN KEY (mother_id) REFERENCES animals(id),
                FOREIGN KEY (father_id) REFERENCES animals(id)
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_state (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                money REAL NOT NULL,
                total_milk REAL NOT NULL DEFAULT 0,
                last_save_timestamp REAL NOT NULL,
                created_at REAL NOT NULL,
                game_time_hours REAL DEFAULT 0
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL NOT NULL, 
                type TEXT NOT NULL,
                animal_id TEXT,
                amount REAL NOT NULL,
                description TEXT,
                FOREIGN KEY (animal_id) REFERENCES animals(id)
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_offers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                available_until REAL,
                FOREIGN KEY (animal_id) REFERENCES animals(id)
                )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pen_config (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                cow_pen_width INTEGER DEFAULT 5,
                cow_pen_height INTEGER DEFAULT 5,
                bull_pen_width INTEGER DEFAULT 5,
                bull_pen_height INTEGER DEFAULT 1
                )
            ''')

        self.connection.commit()

    def init_or_update_perks_table(self, perks_dict):
        '''заполняет таблицу perks перками из словаря в конфиге'''
        for perk_id, perk_data in perks_dict.items():
            self.cursor.execute('''
                INSERT OR REPLACE INTO perks
                (name, description, effect_type, effect_value, rarity)
                VALUES (?, ?, ?, ?, ?)
                ''', (perk_id, perk_data['description'], perk_data['effect_type'], 
                    perk_data['effect_value'],  perk_data['rarity'],))
        self.connection.commit()    


    def save_animal(self, animal_data):
        # сохраняет даннные животного
        self.cursor.execute('''
            INSERT OR REPLACE INTO animals
            (name, type, gender, age, ...)
            VALUES (?, ?, ?, ?, ...)

            ''', (animal_data, ))

        self._save_animal_perk(self, animal_id, perks)

        self.connection.commit()

    def load_animal(self, animal_id):
        ''' загружает данные о животном '''
        self.cursor.execute('''
            SELECT * FROM animals WHERE id = ?
            ''', (animal_id, ))
        return cursor.fetchone()

    def update_animal_position(self, animal_id, x, y, location_type):
        ''' обновляет позицию животного -- пересадить животное'''
        self.cursor.execute('''
            UPDATE animals
            SET pen_x = ?, pen_y = ?, location_type = ?
            WHERE id = ?

            ''', (x, y, location_type, animal_id))
        self.connection.commit()

    def save_game_state(self, money, total_milk, timestamp):
        ''' сохраняет состояние игры '''
        self.cursor.execute('''
            INSERT OR REPLACE INTO game_state (id, money, total_milk, last_save_timestamp)
            VALUES (1, ?, ?, ?)

            ''', (money, total_milk, timestamp, ))
        self.connection.commit()

    def _save_animal_perk(self, animal_id, perks):
        '''
        корова 34, (умная, выносливая)
        1. удалаю запись о корове 34 в таблице анимал перкс, если она там есть
        2. беру каждый элемент из перков
        3. нахожу его УНИКАЛЬНЫЙ айди в моей базе всех перков
        4. делаю запись для коровы 34 и присваиваю ей данные перки
        '''

        self.cursor.execute('DELETE FROM animal_perks WHERE animal_id = ?', (animal_id, ))

        for perk in perks:
            perk_id = self._get_or_create_perk(perk)
            self.cursor.execute('''
                INSERT INTO animal_perks (animal_id, perk_id)
                VALUES (?, ?)
                ''', (animal_id, perk_id)) 
            self.connection.commit()

    def _get_perk_id(self, perk):
        result = self.cursor.execute('SELECT id FROM perks WHERE name = ?', (perk,)).fetchone()
        print (result[0]) 
        self.cursor.execute("SELECT * FROM perks")
        columns = self.cursor.fetchall()
        print("Структура таблицы perks:")
        for col in columns:
            print(col)
        return result[0]

    def load_all_alive_animals(self):
        self.cursor.execute('SELECT * FROM animals WHERE is_alive = 1')
        return self.cursor.fetchone()

    def get_next_animal_id(self):
        '''выдает следующий доступный id, в том числе нулевой'''
        max_id = self.cursor.execute('SELECT MAX(id) FROM animals').fetchone()
        if max_id[0] is None:
            return 0
        else:
            print(max_id[0])
            return max_id[0] + 1
        




p = Storage(config.PATH)
p._get_perk_id('Быстрый рост')