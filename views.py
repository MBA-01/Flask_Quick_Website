from flask import Blueprint,render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    
    return render_template("index.html",name="Mohamed", age=24) # We can pass variable through here as 'name' and displayed on the html page