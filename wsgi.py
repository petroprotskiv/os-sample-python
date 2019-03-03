from flask import Flask
from db_support import get_workers_json

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World from Petro2!"

@application.route("/workers/get")
def get_workers():
    #TODO check token
    return get_workers_json()

if __name__ == "__main__":
    application.run()
