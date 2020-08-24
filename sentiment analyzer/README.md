# Sentiment Analyzer 

## Overview

I present here a simply text classification Flask app which classifies sentiment of customer’s review on Customer Review Tab whether it is positive or negative which, the trained model predicts. I have trained the model in sci-kit learn (machine learning). An analysis of the submitted reviews can be found under the Review Analysis Tab which is a useful tab for business owners to see analysis of their business performance.
The app can be accessible at : https://sentiment-analyzer-ml.herokuapp.com/home

## Installation:
`pip install -r requirements.txt`

## Run:
You need to set your environment variable for your Database connections with 

`Export DATABASE_URL=dialect+driver://username:password@host:port/database`

Or change the variable `SQLALCHEMY_DATABASE_URI = dialect+driver://username:password@host:port/database` in the `sentiment_app/config.py` file.

## Technologies Used:
-	Scikit-learn
-	Pandas
-	Flask
-	Python
-	Html, CSS, Bootstrap
-	Jupyter Notebook
-	Docker


