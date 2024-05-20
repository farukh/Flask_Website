from flask import Flask, render_template

app = Flask("Flash Website")

@app.route("/")
def home():
    return render_template("home.html") #html files must be in "templates" folder
@app.route("/about")
def about():
    return render_template("about.html") #html files must be in "templates" folder


app.run(debug=True)

