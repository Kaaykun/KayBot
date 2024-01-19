import json
import pickle
import nltk
import random
import numpy as np
from nltk.stem import WordNetLemmatizer

from params import INTENTS_PATH, WORDS_PATH, CLASSES_PATH

# Constants
lemmatizer = WordNetLemmatizer()

########################################################################################

def load_intents():
    """
    Load intents from a JSON file.
    """
    return json.loads(open(INTENTS_PATH).read())

########################################################################################

def load_words():
    """
    Load a list of words from a pickled file.
    """
    return pickle.load(open(WORDS_PATH,'rb'))

########################################################################################

def load_classes():
    """
    Load a list of classes from a pickled file.
    """
    return pickle.load(open(CLASSES_PATH,'rb'))

########################################################################################

def load_data_files():
    """
    Load intents, words, and classes from local files.
    """
    intents = load_intents()
    words = load_words()
    classes = load_classes()

    return intents, words, classes

########################################################################################

def lemmatize_files():
    """
    Lemmatize words from intent patterns and save processed data.
    """
    intents = load_intents()
    words = []
    classes = []
    documents = []
    ignore = ['?','!',',',"'s"]

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent['tag']))

            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore]
    words = sorted(list(set(words)))

    classes = sorted(list(set(classes)))

    pickle.dump(words,open(WORDS_PATH,'wb'))
    pickle.dump(classes,open(CLASSES_PATH,'wb'))

    return words, classes, documents

########################################################################################

def prep_training_data():
    """
    Prepare training data for a classifier using lemmatized files.
    """
    training = []
    words, classes, documents = lemmatize_files()
    output_empty = [0]*len(classes)

    for doc in documents:
        bag = []
        pattern = doc[0]
        pattern = [lemmatizer.lemmatize(word.lower()) for word in pattern ]

        for word in words:
            if word in pattern:
                bag.append(1)
            else:
                bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append((bag, output_row))

    random.shuffle(training)

    X_train = np.array([item[0] for item in training])
    y_train = np.array([item[1] for item in training])

    return X_train, y_train

########################################################################################
