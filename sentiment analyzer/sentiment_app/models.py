from . import db
from datetime import datetime

class Sentiments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



    def __repr__(self):
        return f"Sentiments('{self.review}')"



class Predictions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    review_id = db.Column(db.Integer, db.ForeignKey('sentiments.id'), nullable=False)

    def __repr__(self):
        return f"Predictions('{self.prediction}')"


