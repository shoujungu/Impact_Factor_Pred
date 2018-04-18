import pandas as pd
import numpy as np
import flask
from flask import request
import os
import spacy
import data_clean as dc
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import sklearn
from ast import literal_eval

app = flask.Flask(__name__)

with open('logreg_model.pkl', 'rb') as f:
    model=pickle.load(f)

with open('logreg_sc.pkl', 'rb') as f:
    sc=pickle.load(f)

#with open('logreg_tfidf.pkl', 'rb') as f:
#    tfidf=pickle.load(f)

x_train=pd.read_csv('x_train.csv',header=None).iloc[:,0]
tfidf = TfidfVectorizer(analyzer='word', lowercase=False, ngram_range=(1,4), \
                   min_df=10,max_df=0.3, max_features=50000)
tfidf_f=tfidf.fit(x_train)

@app.route('/')
def homepage():
     return flask.render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text=dc.clean_words(text)
    text=[text]
    text_tfidf=tfidf_f.transform(text)
    text_sc=sc.transform(text_tfidf)
    pred=model.predict(text_sc)
    if pred[0]==0:
        impact='above 28.'
    elif pred[0]==1:
        impact='between 10 and 28.'
    else:
        impact='below 10.'
    return 'I think this abstract is from the journal with impact factor '+impact


if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
