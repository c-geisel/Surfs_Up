from flask import Flask

#create a new flask instance called app
app = Flask(__name__)

#define our starting point with route, add code we want in route below it.
@app.route('/')
def hello_world():
    return 'Hello world'

