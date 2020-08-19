from flask import render_template, url_for, flash, redirect,jsonify,request
from sentiment_app import app, db
from sentiment_app.models import Sentiments,Predictions
from sentiment_app.forms import ReviewForm

import pickle
import numpy as np







@app.route("/")
@app.route("/home", methods = ['GET','POST'])
def home():
    form = ReviewForm()


    with open('sentiment_app/model_svm_amzn_ylp_imdb.pkl', 'rb')as f:
        classifier = pickle.load(f)


    if form.validate_on_submit():
        review = Sentiments(review = form.review.data)
        db.session.add(review)
        db.session.commit()

        flash('We received your Feedback. Thanks, for your review!','success')


        text = [form.review.data]

        my_prediction = classifier.predict(text)

        if my_prediction == 1:
            pred = Predictions(prediction='positive',review_id = review.id)
        else:
            pred = Predictions(prediction='negative',review_id = review.id)
        db.session.add(pred)
        db.session.commit()



        #return jsonify((classifier.predict([form.review.data]).tolist()))

        return redirect(url_for('home'))

    return render_template('home.html',title='home',form=form)


@app.route("/reviews")
def reviews():
    page = request.args.get('page', 1, type=int)
    review = Sentiments.query.order_by(Sentiments.date_posted.desc()).paginate(page=page, per_page=5)
    sentiment = Predictions.query.order_by(Predictions.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('review.html', reviews=review,sentiments=sentiment,title='reviews')

