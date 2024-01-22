from flask import Flask #type: ignore
from nltk.stem import WordNetLemmatizer
from kaybotconfig import Config

app = Flask(__name__)
app.config.from_object(Config)

from backend.model import load_local_model
from backend.preprocess import load_data_files

lemmatizer = WordNetLemmatizer()

model = load_local_model()
intents, words, classes = load_data_files()

from frontend import routes
