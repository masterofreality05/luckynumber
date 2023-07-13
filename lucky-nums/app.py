from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_cors
from flask_wtf.csrf import CSRFProtect

from forms import LuckyNumberForm
import urllib, json

app = Flask(__name__)
app.config['SECRET_KEY'] = "itsasecret"
app.config['WTF_CSRF_ENABLED'] = False
valid_colors = ['red','green','orange','blue']

def valid_dob(number):
     number = int(number)
     if number >= 1900 and number <= 2000:
          return True
     else:
          return False
     
def get_number_fact():
     """a function used when form submitted to retrieve a lucky number and fact"""
     url = "http://numbersapi.com/random?json"
     response = urllib.request.urlopen(url)
     data = response.read()
     dict = json.loads(data)
     return dict

def get_dob_fact(dob):
       """a function used when form submitted to retrieve a fact  based on the date of birth passed"""
       url = f"http://numbersapi.com/{dob}/year?json"
       response = urllib.request.urlopen(url)
       data = response.read()
       dict = json.loads(data)
       return dict
     
@app.route("/")
def homepage():
    """Show homepage."""
    form = LuckyNumberForm()
    return render_template("index.html", form=form)

@app.route("/numberapi", methods=['GET','POST'])
def get_lucky_number():
    """recieves our AJAX request from the front end,"""
    ## here we will store the data of the users who use our lucky number app. 
    #this is just for reference, and we can use the data at a later point. 
    #when all of the inputted data is correct, we return the client with a lucky number and the fact
    #we can collect data like what type of facts people want to know the most. 
    form = LuckyNumberForm()
    converted = json.loads(bytes.decode(request.data))
    birth_year = converted.get('birth_year')
    color = converted.get('color').lower()


    if form.validate_on_submit():
        print("validated!")
        if  color not in valid_colors:
              print("error of color")
              form.color.errors = "Please pick a valid colour"
              retrieved = jsonify(errors=form.color.errors) 
              #currently returning undefined.
        
        elif valid_dob(birth_year) != True:
             print("error of dob")
             form.color.errors = "Please pick a valid birthyear between 1900 and 2000"
             retrieved = jsonify(errors=form.birth_year.errors)   
             #currently returning undefined
        else:
             
             year_fact = get_dob_fact(birth_year)
             number_fact = get_number_fact()

        print(year_fact) #this is json
        print(number_fact) #this is json
        return [year_fact,number_fact]
    

    return "csrf validation did not pass"

 #we will process user form for information, confirming all valid.. then user can select fact type.
 #if all the information is valid, the user will recieve a randomized lucky number and a fact category of their choice. 
