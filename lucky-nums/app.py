
from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from flask_cors import cross_origin, CORS
from forms import LuckyNumberForm
import urllib, json


app = Flask(__name__)

app.config['SECRET_KEY'] = "itsasecret"
app.config['WTF_CSRF_ENABLED'] = False
valid_colors = ['red','green','orange','blue']

CORS(app)
cors = CORS(app, resources={r"/numberapi/*": {"origins": "*"}})

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
@cross_origin()
def get_lucky_number():
    """recieves our AJAX request from the front end,"""
    print("running????????????")
    ## here we will store the data of the users who use our lucky number app. 
    #this is just for reference, and we can use the data at a later point. 
    #when all of the inputted data is correct, we return the client with a lucky number and the fact
    #we can collect data like what type of facts people want to know the most. 
   
   # converted = json.loads(bytes.decode(request.data))
    #birth_year = converted.get('birth_year')
    #color = converted.get('color').lower()
    
    
    form = LuckyNumberForm()

    print(form)
    print(form.color.data)
    print(form.name.data)
    print(form.email.data)
    print(form.birth_year.data)


    if form.validate_on_submit():
        print(form.color.data)
        print(form.name.data)
        print(form.email.data)
        print(form.birth_year.data)
        
       
        if  form.color.data not in valid_colors:
            form.color.errors = "Please pick a valid colour"
            retrieved = jsonify(form.errors)
            print("error is ", retrieved)
              #currently returning undefined.
        
        elif valid_dob(form.birth_year.data) != True:
          form.color.errors = "Please pick a valid birthyear between 1900 and 2000"
          retrieved = jsonify(form.errors)
         
          print("error is ", retrieved)
           #currently returning undefined
        else:
             
           year_fact = get_dob_fact(form.birth_year.data)
           number_fact = get_number_fact()
           retrieved = [year_fact, number_fact]

      #  print(year_fact) #this is json
      #  print(number_fact) #this is json
        return retrieved
    
    
    

    return "csrf validation did not pass"

 #we will process user form for information, confirming all valid.. then user can select fact type.
 #if all the information is valid, the user will recieve a randomized lucky number and a fact category of their choice. 
