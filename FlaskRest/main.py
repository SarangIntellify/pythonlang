from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #Flask class constructor needs the module name
api = Api(app) #initializing the rest api module using Api class.

#resource class must be child of Resource class so we can override the method of parent Resource class.
class HelloWorld(Resource):
    def get(self):
        return {"data": "Helloworld"}
    
api.add_resource(HelloWorld, "/helloworld") 

if __name__ == "__main__":
    app.run(debug = True)