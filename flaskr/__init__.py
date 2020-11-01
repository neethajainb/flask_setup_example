from flask import Flask, jsonify
#from models import setup_db, Plant
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    #setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello_world():
        #return 'Hello, World!'
        return jsonify({'message':'Hello, World!'})

    @app.route('/hi')
    def hi():
        return 'hello'

    @app.route('/hello')
    def hello():
        return 'hi'

    return app
