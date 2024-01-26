from flask import render_template, flash, request #type: ignore
from frontend import app
from frontend.forms import kaybotform
from frontend.__init__ import model, words, classes, intents

import os
import time
import pytz
import nltk
import random
import requests
import billboard #type: ignore
import webbrowser
import pygame.mixer #type: ignore
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
from googlesearch import search #type: ignore
from nltk.stem import WordNetLemmatizer

load_dotenv()
lemmatizer = WordNetLemmatizer()

#Predict
def clean_up(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [ lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def create_bow(sentence,words):
    sentence_words = clean_up(sentence)
    bag = list(np.zeros(len(words)))

    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence,model):
    p = create_bow(sentence,words)
    res = model.predict(np.array([p]))[0]
    threshold = 0.8
    results = [[i,r] for i,r in enumerate(res) if r>threshold]
    results.sort(key=lambda x: x[1],reverse=True)
    return_list = []

    for result in results:
        return_list.append({'intent':classes[result[0]],'prob':str(result[1])})
    return return_list

def get_response(return_list,intents_json,text):
    if len(return_list) == 0:
        tag = 'noanswer'
    else:
        tag = return_list[0]['intent']

    if tag == 'datetime':
        x = ''
        tz = pytz.timezone('Asia/Tokyo')
        dt = datetime.now(tz)

        x += str(dt.strftime("%A"))+' '
        x += str(dt.strftime("%d %B %Y"))+' '
        x += str(dt.strftime("%H:%M:%S"))

        return x,'datetime'

    if tag == 'weather':
        x = ''
        weather_api_key = os.environ.get('WEATHER_API_KEY')
        city_name = text.split(':')[1].strip()
        url = f'https://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}&q={city_name}'

        response = requests.get(url).json()

        pres_temp = round(response['main']['temp']-273,2)
        feels_temp = round(response['main']['feels_like']-273,2)
        cond = response['weather'][0]['main']

        x += 'Present temp.:' + str(pres_temp) + 'C. Feels like:' + str(feels_temp)+'C. ' + str(cond)
        print(x)

        return x, 'weather'

    if tag=='news':
        news_api_key = os.environ.get('NEWS_API_KEY')
        url = f'http://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}'

        open_news_page = requests.get(url).json()
        articles = open_news_page["articles"]

        results = [[article["title"], article["url"]] for article in articles]
        x = ''

        for i in range(10):
            x += (str(i + 1))
            x += '. '+str(results[i][0])
            x += (str(results[i][1]))
            if i != 9:
                x += '\n'

        return x, 'news'

    if tag == 'song':
        chart = billboard.ChartData('hot-100')
        x = 'The top 10 songs at the moment are: \n'

        for i in range(10):
            song = chart[i]
            x += str(i+1)+'. ' + str(song.title) + '- ' + str(song.artist)
            if i != 9:
                x += '\n'

        return x, 'songs'

    if tag == 'timer':
        x = text.split(':')[1].strip()
        time.sleep(float(x)*60)
        x = 'Timer ringing...'
        return x, 'timer'

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if tag == i['tag'] :
            result = random.choice(i['responses'])
    return result, tag

def response(text):
    return_list = predict_class(text, model)
    response, _ = get_response(return_list, intents, text)
    return response


@app.route('/', methods = ['GET','POST'])
def yo():
    return render_template('main.html')

@app.route('/chat', methods = ['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/get")
def chatbot():
    userText = request.args.get('msg')
    resp = response(userText)

    return resp
