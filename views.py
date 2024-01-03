from flask import Blueprint

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return "First home page"


@views.route("/home")
def home2():
    return "Second home page"