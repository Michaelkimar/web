from flask import Flask,render_template

app =Flask(__name__)


@app.route("/")
def home_page():
    return "render_template(index.html)"
    
@app.route("/about")
def about():
    return "this is the about page"
    