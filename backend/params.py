import os

############# CONSTANTS #############
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'models')
INTENTS_PATH = os.path.join(DATA_PATH, 'intents.json')
WORDS_PATH = os.path.join(DATA_PATH, 'words.pkl')
CLASSES_PATH = os.path.join(DATA_PATH, 'classes.pkl')
