#Import Flask
from flask import Flask

#Create a new Flask instance called "app"
app = Flask(__name__)

#Creat a Flask route
##Define the starting point aka the "root"
@app.route('/')
def hello_world():
   return 'Hello World'

#HOW TO RUN FLASK VIA TERMINAL
# 1. Go to Terminal, and enter 'export FLASK_APP=flask_example.py'
# 2. Then enter, 'set FLASK_APP=app.py'
# 3. Then enter, 'flask run'
# ^^^ prompt IP address --> http://127.0.0.1:5000/ or 'localhost:5000'