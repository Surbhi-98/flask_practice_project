#A SAMPLE WEB PAGE WITH FLASK
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
#def hello_world():
    #return "<p>Hello, World!, Bye--Bye!!!</p>"
if __name__ == '__main__':
    app.run(debug=True)
