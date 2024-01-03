from flask import Blueprint,render_template,request,jsonify,redirect,url_for

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


# access data from received json file

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)



# page Redirection

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))