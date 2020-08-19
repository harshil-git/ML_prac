import pickle
import numpy as np

with open('sentiment_app/model_disaster_200d_glove.h5','rb') as file:
    mp = pickle.load(file)
#clf = pickle.load(open('sentiment_app/model_disaster_200d_glove.h5', 'rb'))
dir(mp.predict())

