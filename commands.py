from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
from nltk import tokenize
from operator import itemgetter
import math
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from multi_rake import Rake


# SENTIMENT
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.44, 0.48)

def sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def predict(text, include_neutral=True):
    print('it is party time')
    model = load_model('model.h5')
    with open('tokenizer.pkl', 'rb') as handle:
        tokenizer = pickle.load(handle)
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = sentiment(score, include_neutral=include_neutral)
    word_list = text.split()
    number_of_words = len(word_list)
    keyword = extract_keywords(text)
    print(text)
    if (text == 'no'):
        return('All good! Thank you for sharing.')
    if (label == NEGATIVE):
        if (number_of_words <=12):
            output = sad_short()
            return output
        else:
            return("I'm sorry you've been feeling negatively about your " + keyword + ". I'm glad you're taking the time to reflect on this.")
    elif (label == POSITIVE):
        if (number_of_words <=12):
            output = happy_short()
            return output
        else:
            return("I'm glad you're feeling good about your " + keyword + "! Thank you for sharing :)")
    else:
        if (number_of_words <=12):
            output = neutral_short
            return output
        else:
            return("Thanks for sharing :)")

def neutral_short():
    return("Interesting...tell me more? If you don't want to, just say say 'No'")

def sad_short():
    print('sad time')
    """ Takes an argument, user_input, in form of a string ..."""

    apology_list = ['I empathize!', "I'm so sorry to hear!", "Oh no!"]
    follow_up = "Would you like to talk more about it? If you don't want to, just say say 'No'"

    final_string = (np.random.choice(apology_list, size=1)[0]) + follow_up
    print(final_string)
    return final_string

def happy_short():
    print('happy time')
    """ Takes an argument, user_input, in form of a string ..."""

    apology_list = ["That's so great!", "I'm so happy for you!", "Yay!"]
    follow_up = "Tell me more! If you don't want to, just say say 'No'"

    final_string = (np.random.choice(apology_list, size=1)[0]) + follow_up
    print(final_string)
    return final_string


#doc = 'I am a graduate. I want to learn Python. I like learning Python. Python is easy. Python is interesting. Learning increases thinking. Everyone should invest time in learning'

def extract_keywords(text):
    nlkt_text = word_tokenize(text)
    val = nltk.pos_tag(nlkt_text)
    rake = Rake()
    keywords = rake.apply(text)
    new_val = []
    keyword= 'nothing'
    for i in range(len(val)):
        if ((val[i][1] == 'NN')):
            new_val.append(val[i][0])
    for i in range(len(keywords)):
        for j in range(len(new_val)):
            if (keywords[i][0] == new_val[j]):
                keyword = new_val[j]
    return(keyword)
    #print(keywords[:10])
    
