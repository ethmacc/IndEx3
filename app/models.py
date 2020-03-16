from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    forecasts = db.relationship('Forecast', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Text)
    forecasts = db.relationship('Forecast', backref='cities')

    def __repr__(self):
        return '<City {}>'.format(self.city_id)


class Forecast(db.Model):
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    forecast_datetime = db.Column(db.Text, nullable=False)
    forecast = db.Column(db.Text)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Forecast {} {}>'.format(self.datetime, self.actualforecast)

 