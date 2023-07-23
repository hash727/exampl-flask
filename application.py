from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1> Hello World.!, by HasH from local machine </h1>"