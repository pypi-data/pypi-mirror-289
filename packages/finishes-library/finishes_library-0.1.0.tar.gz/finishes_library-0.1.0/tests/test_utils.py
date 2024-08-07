# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:16:23 2024

@author: U435712
"""

import sys
import os

# Get the absolute path of the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now import from your library
from finishes_library.utils import add, subtract 

import unittest

class TestUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

if __name__ == '_main_':
    unittest.main()