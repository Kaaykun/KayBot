import os
# Suppress WARNING, INFO, and DEBUG messages related to tensorflow and pygame
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import time
import nltk
import random
import requests
import billboard #type: ignore
import webbrowser
import pygame.mixer #type: ignore
import numpy as np
from dotenv import load_dotenv
from googlesearch import search #type: ignore
from nltk.stem import WordNetLemmatizer

# Custom Imports
from backend.params import *
from backend.preprocess import load_data_files, prep_training_data
from backend.model import load_local_model, initialize_model, train_model, save_model

########################################################################################
load_dotenv()

try:
    """
    Load a local model
    """
    model = load_local_model()

except FileNotFoundError:
    """
    If the local model does not exist, createa, train and save a new one
    """
    X_train, y_train = prep_training_data()
    model, early_stopping = initialize_model(X_train, y_train)
    history = train_model(model, X_train, y_train, early_stopping)
    save_model(model, history)

intents, words, classes = load_data_files()
lemmatizer = WordNetLemmatizer()

########################################################################################

def clean_up(sentence):
    """
    Tokenize and lemmatize the words in a sentence.
    """
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

    return sentence_words

########################################################################################

def create_bow(sentence, words):
    """
    Create a bag of words (BoW) representation.
    """
    sentence_words = clean_up(sentence)
    bag = list(np.zeros(len(words)))

    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    return np.array(bag)

########################################################################################

def predict_class(sentence, model):
    """
    Predict the class/intent of a sentence using a trained model.
    """
    p = create_bow(sentence, words)
    res = model.predict(np.array([p]), verbose=0)[0]
    threshold = 0.8

    results = [[i, r] for i, r in enumerate(res) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []

    for result in results:
        return_list.append({'intent':classes[result[0]],'prob':str(result[1])})

    return return_list

########################################################################################

def get_response(return_list, intents_json):
    """
    Get a response based on the predicted intents and a set of predefined responses.
    """
    if len(return_list)==0:
        tag = 'noanswer'
    else:
        tag = return_list[0]['intent']

    if tag == 'datetime':
        print(time.strftime("%A"))
        print(time.strftime("%d %B %Y"))
        print(time.strftime("%H:%M:%S"))

    if tag == 'google':
        query = input('Enter query: ')
        search_results = list(search(query, num_results=3))

        for url in search_results:
            webbrowser.open(url)

    if tag == 'weather':
        weather_api_key = os.environ.get('WEATHER_API_KEY')
        city_name = input("Enter city name: ")
        url = f'https://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}&q={city_name}'

        response = requests.get(url).json()

        print('Present temp.: ', round(response['main']['temp']-273,2),'celcius ')
        print('Feels Like:: ', round(response['main']['feels_like']-273,2),'celcius ')

    if tag == 'news':
        news_api_key = os.environ.get('NEWS_API_KEY')
        url = f'http://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}'

        open_news_page = requests.get(url).json()
        articles = open_news_page["articles"]

        results = [[article["title"], article["url"]] for article in articles]

        for i in range(10):
            print(f'{i + 1})', results[i][0])
            print(results[i][1],'\n')

    if tag == 'song':
        chart = billboard.ChartData('hot-100')

        print('The top 10 songs at the moment are:')
        for i in range(10):
            song = chart[i]
            print(f"{i + 1}) {song.title.ljust(30)} by: {song.artist.ljust(50)}")

    if tag == 'timer':
        pygame.mixer.init()
        minutes = float(input('Minutes to timer: '))

        time.sleep(minutes * 60)

        pygame.mixer.music.load('../backend/Handbell-ringing-sound-effect.mp3')
        pygame.mixer.music.play()

    list_of_intents = intents_json['intents']

    for i in list_of_intents:
        if tag == i['tag']:
            result = random.choice(i['responses'])

    return result

########################################################################################

def response(text):
    """
    Generate a response for a given input text.
    """
    return_list = predict_class(text, model)
    response = get_response(return_list, intents)

    return response

########################################################################################
# while(1):
#     user_input = input('User: ')
#     print('Kaybot:', response(user_input))

#     if user_input.lower() in ['bye', 'goodbye', 'good bye', 'get lost', 'see you']:
#         break

########################################################################################
