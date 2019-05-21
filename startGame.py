## Javier Huertas (2017-18)
## Alejandro Cervantes (2017-18)
'''startGame.py
   Artificial Intelligence Course
   Practice on Space State Search
   Loads the module paths and calls the main graphic interface
   
   Run this script from the extraction folder
   
   Dependencies: pygame, simpleAI (provided in the distribution), student code
   sudo pip install pygame
   
   The tutorial requires additional modules:
   sudo apt-get install graphviz
   pip install pydot flask

'''

import os,sys

sys.path.append(os.path.abspath("./student"))
sys.path.append(os.path.abspath("./game"))
sys.path.append(os.path.abspath("./simpleai-0.8.1"))

import gameAI
