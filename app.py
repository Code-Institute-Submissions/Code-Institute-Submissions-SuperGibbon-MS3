import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def array_from_string(string):
    arr = string.split(',')
    return arr


@app.route("/")
def go_home():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if is_authenticated():
        return redirect(url_for("get_recipes"))

    if request.method == "POST":
        username = request.form.get("username").lower()
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": username,
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = username
        flash("Registration Successful!")
        return redirect(url_for("get_recipes"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if is_authenticated():
        return redirect(url_for("get_recipes"))

    if request.method == "POST":
        username = request.form.get("username").lower()
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = username
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for("get_recipes"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    if is_authenticated():
        # remove user from session cookie
        flash("You have been logged out")
        session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipe = {
            "user": request.form.get("user"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_type": request.form.get("recipe_type"),
            "recipe_diff": request.form.get("recipe_diff"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": array_from_string(request.form.get("ingredients")),
            "cook_steps": array_from_string(request.form.get("cook_steps")),
            "tools_needed": array_from_string(
                            request.form.get("tools_needed")),
            "number_served": request.form.get("number_served"),
            "image_source": request.form.get("image_source")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added to cook book")
        return redirect("get_recipes")

    types = mongo.db.recipe_type.find()
    return render_template("addrecipe.html", types=types)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not is_authenticated():
        return redirect(url_for("login"))

    if not is_object_id_valid(recipe_id):
        abort(404)

    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})

    if request.method == "POST":
        editrecipe = {
            "user": request.form.get("user"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_type": request.form.get("recipe_type"),
            "recipe_diff": request.form.get("recipe_diff"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": array_from_string(request.form.get("ingredients")),
            "cook_steps": array_from_string(request.form.get("cook_steps")),
            "tools_needed": array_from_string(
                            request.form.get("tools_needed")),
            "number_served": request.form.get("number_served"),
            "image_source": request.form.get("image_source")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, editrecipe)
        flash("Recipe updated")
        return redirect(url_for("get_recipes"))

    types = mongo.db.recipe_type.find()
    return render_template("editrecipe.html", types=types, recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted")
    return redirect(url_for("get_recipes"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    return render_template("recipes.html", recipes=recipes)


def is_authenticated():
    return "user" in session


def is_object_id_valid(id_value):
    """ Validate if the id_value is a valid ObjectId
    """
    return id_value != "" and ObjectId.is_valid(id_value)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
