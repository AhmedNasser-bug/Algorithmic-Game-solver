
import pip

def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])

# installing required packages if not found
required_packages = ['collections', 'random', 'os', 'math', 'heapq', 'customtkinter', 'tkinter', 'PIL']
install_packages(required_packages)

from heapq import*
from os import*
from collections import*
from Node import*
from random import *
from os import *
from time import*
from math import *
from sys import *

class idx:
   def __init__(self, row, col) -> None:
      self.row = row
      self.col = col
      
def ui_step():
    sleep(0.5)
    print("Press any key to continue...")
    system("pause > 0")
    system("cls")
