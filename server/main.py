from flask import Flask
from flask_restful import Api
from resources import Translate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['KMP_DUPLICATE_LIB_OK']='True'

api = Api(app)

api.add_resource(Translate, "/translate")

if __name__ == '__main__':
    app.run()

