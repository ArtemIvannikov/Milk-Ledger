import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scr')))

from models.animal import Animal
from config import *

class Tests(unittest.TestCase):
	pass