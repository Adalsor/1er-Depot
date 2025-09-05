from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Histoire.html")

@app.route('/page1')
def page1():
    return render_template("la-belle-aux-bois-dormant.html")

@app.route('/page2')
def page2():
    return render_template("la-belle-et-la-bete.html")

@app.route('/page3')
def page3():
    return render_template("les-trois-petits-cochons.html")

@app.route('/page4')
def page4():
    return render_template("blanche-neige.html")

@app.route('/page5')
def page5():
    return render_template("le-petit-prince.html")
