import re
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

#use Flask's --> app.route to map to home page. It is a decorator (@)
@app.route("/")

#define a simple function and call it home
def home():
    return render_template("home.html")

#add second route
@app.route('/homealone/<name>')
def hello_again(name):
    #get current date
    now = datetime.now()
    #format it
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
    #filter out irregular characters in name
    match_object = re.match("[a-zA-Z]+",name)
    
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
        
    content = "Hello there, "+ clean_name + "! It's " + formatted_now
    return content

#new function for about us page
@app.route("/about/")
def about():
    return render_template("about.html")

#function for contact us page
@app.route("/contact/")
def contact():
    return render_template("contact.html")

