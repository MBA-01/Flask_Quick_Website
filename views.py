from flask import Blueprint,render_template,request,jsonify

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",name="Mohamed") # We can pass variable through here as 'name' and displayed on the html page

@views.route("/profile")
def profile():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)


@views.route("/json")
def get_json():
    return jsonify({"name":"Mohamed","coolness":10})