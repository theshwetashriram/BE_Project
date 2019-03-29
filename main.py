from flask import Flask, render_template, redirect, request
from forms import LoginForm
from database import Database
from forms import PlaceForm
from forms import CityForm
from forms import StateForm
from forms import PlacetagForm
from forms import states_detailsForm
from forms import city_detailsForm
                  


app = Flask(__name__,
            static_url_path='',
            static_folder='static')
app.config['SECRET_KEY'] = 'you-will-never-guess'

#from app import route


@app.route('/hello')
def hello():
    return "Hello universe"

#loops
# making list of pokemons 
Pokemons =["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  
           "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"] 
  
@app.route('/sample1') 
def sample1(): 
    return render_template("sample1.html", len = len(Pokemons), Pokemons = Pokemons) 
    app.run(use_reloader = True, debug = True) 


@app.route('/sample')
def sample():
    return render_template('sample.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('login')
    message = ''
    form = LoginForm()
    if form.validate_on_submit():
        # print('Login requested for username {}, password {}'.format(form.username.data, form.password.data))
        # return redirect('/index')
        db = Database()
        id = db.checkLogin(form.username.data, form.password.data)
        db.close()
        print('id', id)
        if id != -1:
            return redirect('/index')
        else:
            message = 'Invalid username or password'
    return render_template('login.html', form=form, message=message)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/states',methods=['GET', 'POST'])
def states():
    message = ''
    form = StateForm()
    db = Database()
    if form.validate_on_submit():
        # print('Input requested for state{}, ' .format(form.state.data))
        # return redirect('/index')
        db.addState(form.name.data)
        db.commit()
        #print('id', id)
        #if id != -1:
        return redirect('/states')
        # else:
        #     message = 'Invalid state'

    States=db.getStates()
    db.close()
    return render_template('states.html',form=form, message=message,States=States,len=len(States))


@app.route('/city', methods=['GET', 'POST'])
def city():
    message = ''
    form = CityForm()
    placeid=request.args.get('placeid')
    form = states_detailsForm()
    db = Database()
    if form.validate_on_submit():
        # print('Input requested for state{}, city{}, ' .format(form.state.data, form.city.data))
        # return redirect('/index')
        
        id = db.addCity(form.name.data)
        db.commit()
        # print('id', id)
        # if id != -1:
        return redirect('/place?placeid='+placeid)
        # else:
        #    message = 'Invalid state or city'
    
    Cities=db.getCities()
    db.close()
    return render_template('city.html', form=form, message=message,city=Cities,len=len(Cities))

@app.route('/place', methods=['GET', 'POST'])
def place():
    message = ''
    form = states_detailsForm()
    form = PlaceForm()
    if form.is_submitted():
        # return redirect('/index')
        db = Database()
        cityid=request.args.get('cityid')
        print('cityid',cityid)
        id = db.addPlace(form.place.data, form.desc.data,form.longitude.data,form.latitude.data,cityid)
        db.close()
        print('id', id)
        if id != -1:
            return redirect('/index')
        else:
            message = 'Invalid place'
    return render_template('place.html', form=form, message=message)

@app.route('/placetag', methods=['GET', 'POST'])
def placetag():
    message = ''
    form = PlacetagForm()
    if form.is_submitted():
        # return redirect('/index')
        db = Database()
        cityid=request.args.get('cityid')
        print('cityid',cityid)
        id = db.addPlacetag(form.placetag.data, form.tag.data)
        db.close()
        
        print('id', id)
        if id != -1:
            return redirect('/index')
        else:
            message = 'Invalid place'
    return render_template('placetag.html', form=form, message=message)


@app.route('/states_details', methods=['GET', 'POST'])
def states_details():
    message = ''
    stateid=request.args.get('stateid')
    form = states_detailsForm()
    db = Database()
    if form.is_submitted():
        db.addCity(form.name.data,stateid,form.desc.data, form.longitude.data, form.latitude.data)
        db.close()
        print('id', id)
        return redirect('/states_details?stateid='+stateid)
    cities=db.getCities(stateid)
    state=db.getStateById(stateid)
    return render_template('states_details.html', form=form, message=message, len=len(cities),cities=cities,state=state)

@app.route('/citydetails', methods=['GET', 'POST'])
def citydetails():
    message = ''
    id=request.args.get('id')    
    form = city_detailsForm()
    db=Database()
    if form.is_submitted():
        # return redirect('/index')
        #cityid=request.args.get('cityid')
        #print('cityid',cityid)
        db.addPlace(form.name.data,form.desc.data, form.longitude.data, form.latitude.data,id)
        db.close()
        print('id', id)
        if id != -1:4
        return redirect('/citydetails?id='+id)
    places=db.getplaces(id)
    return render_template('citydetails.html', form=form, message=message,len=len(places),places=places)

