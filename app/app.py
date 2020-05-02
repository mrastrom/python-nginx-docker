# app.py - a minimal flask api using flask_restful
from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse

app = Flask( __name__, template_folder="templates" )
api = Api(app)


# Method one to add routes
class HelloWorld(Resource):
    @staticmethod
    def get():
        name = request.args.get('name')
        return {'hello': name}


api.add_resource(HelloWorld, '/app/hello')


# Method teo to add routes
@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug='true')
