from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, FloatField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username=StringField('Username') #,validators=DataRequired('Username must not be empty'))
    password=PasswordField('Password') #,validators=DataRequired('Password must not be empty'))
    login=SubmitField('Login')

class UserLoginForm(FlaskForm):
    username=StringField('username') #,validators=DataRequired('Username must not be empty'))
    password=PasswordField('password') #,validators=DataRequired('Password must not be empty'))
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
    update=SubmitField('update')
    name=StringField('name')
    desc=StringField('desc')
    longitude=FloatField('longitude')
    latitude=FloatField('latitude')
    add=SubmitField('add')    

class city_detailsForm(FlaskForm):
    newcity=StringField('newcity')
    name=StringField('name')
    desc=StringField('desc')
    longitude=FloatField('longitude')
    latitude=FloatField('latitude')
    add=SubmitField('add')    
    update=SubmitField('update')


class place_detailsForm(FlaskForm):
    newplace=StringField('newplace')
    placetag=StringField('placetag')
    add=SubmitField('add')    
    update=SubmitField('update')

class InputForm(FlaskForm):
    homecity=StringField('homecity')
    # city=StringField('city')
    # add=SubmitField('btnaddcity') 
    selectedcities=StringField('selectedcities')
    # remove=SubmitField('btnremovecity')  
    location_tag=StringField('loaction_tag')
    minbudget=FloatField('minbudget')
    maxbudget=FloatField('maxbudget')
    # Find_Itineraries=SubmitField('btn-success')

class RegisterForm(FlaskForm):
    username=StringField('username')
    fname=StringField('fname')
    lname=StringField('lname')
    password=PasswordField('password')
    register=SubmitField('register')  