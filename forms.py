from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username=StringField('Username') #,validators=DataRequired('Username must not be empty'))
    password=PasswordField('Password') #,validators=DataRequired('Password must not be empty'))
    login=SubmitField('Login')

class CityForm(FlaskForm):
    name=StringField('name')
    submit=SubmitField('Add')

class StateForm(FlaskForm):
    name=StringField('name')
    submit=SubmitField('Submit')
   

class PlaceForm(FlaskForm):
    place=StringField('place')
    desc=StringField('desc')
    longitude=FloatField('longitude')
    latitude=FloatField('latitude')
    submit=SubmitField('Submit')

class PlacetagForm(FlaskForm):
    placeid=IntegerField('placeid')
    name=StringField('tag')
    submit=SubmitField('Submit')


class states_detailsForm(FlaskForm):
    newstate=StringField('newstate')
    add=SubmitField('Update')
    name=StringField('name')
    desc=StringField('desc')
    longitude=FloatField('longitude')
    latitude=FloatField('latitude')
    submit=SubmitField('Add')    

class city_detailsForm(FlaskForm):
    name=StringField('name')
    desc=StringField('desc')
    longitude=FloatField('longitude')
    latitude=FloatField('latitude')
    submit=SubmitField('Add')    