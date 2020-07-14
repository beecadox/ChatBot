# ChatBot - train

import nltk
import json
import pickle
import numpy as np
import random
from itertools import chain
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from model import train_model
from bag_of_words import bow

lemmatizer = WordNetLemmatizer()

# uncomment the following only the first time
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only


def lemmanize_sort_and_print(words, classes):
    # lemmatize and lower case each word and remove duplicates
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    # sort classes
    classes = sorted(list(set(classes)))
    # documents = combination between patterns and intents
    print(len(documents), "documents")
    # classes = intents
    print(len(classes), "classes", classes)
    # words = all words, vocabulary
    print(len(words), "unique lemmatized words", words)


def organize_from_json():
    words = []
    classes = []
    documents = []
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # tokenize each word
            w = nltk.word_tokenize(pattern)
            # find synonyms of each word
            for i in range(len(w)):
                synonyms = wordnet.synsets(w[i])
                lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
                for x in lemmas:
                    w.append(x)  # append each synonym to the word list
            words.extend(w)
            # add documents in the corpus
            documents.append((w, intent['tag']))
            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    return words, classes, documents


ignore_words = ['?', '!', ',']
data_file = open('JSONFiles/restaurant.json').read()
word_pickle = 'PickleFiles/words.pkl'
class_pickle = 'PickleFiles/classes.pkl'

intents = json.loads(data_file)
words, classes, documents = organize_from_json()
lemmanize_sort_and_print(words, classes)

pickle.dump(words, open(word_pickle, 'wb'))
pickle.dump(classes, open(class_pickle, 'wb'))

training = bow(documents, words, classes)

# shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])  # patterns
train_y = list(training[:, 1])  # intents
print("Training data created")

train_model(train_x, train_y)
print("model created")
