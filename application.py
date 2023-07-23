from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1> Hello World.!, by HasH from my local machine </h1>"

if __name__ == "__main__":
    application.run(port=8000, debug=False)