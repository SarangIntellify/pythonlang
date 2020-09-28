from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #Flask class constructor needs the module name
api = Api(app) #initializing the rest api module using Api class.

#resource class must be child of Resource class so we can override the method of parent Resource class.
class HelloWorld(Resource):
    def get(self, name, test): #accessing the variable from request url
        return {"name": name, "test":test}
    
    def post(self):
        return {"data": "Helloworld from post"}
    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>") #parameters in request url

if __name__ == "__main__":
    app.run(debug = True)