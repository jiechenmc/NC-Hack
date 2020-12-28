from flask import Flask, render_template, redirect
from flask.globals import request
from script import get_map_link

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        zip_code = request.form["zip_code"]
        return render_template("map.jinja", map_link=get_map_link(zip_code))
    return render_template("index.jinja")


@app.route("/forward-home")
def go_home():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)