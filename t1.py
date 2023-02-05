from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lifestyle.html")
def lifeStyle():
    return render_template("lifeStyle.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/Youtube.html")
def youtube():
    return render_template("Youtube.html")


@app.route("/math.html")
def math():
    return render_template("math.html")


if __name__ == "__main__":
    app.run()
