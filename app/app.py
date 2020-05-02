# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    @staticmethod
    def get():
        name = request.args.get('name')
        return {'hello': name}


api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='true')
