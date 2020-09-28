from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) #Flask class constructor needs the module name
api = Api(app) #initializing the rest api module using Api class.

#resource class must be child of Resource class so we can override the method of parent Resource class.

class HelloWorld(Resource):
    def get(self, name, test): #accessing the variable from request url
        return {"name": name, "test":test}
    
    def post(self):
        return {"data": "Helloworld from post"}

videos = {}    
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes of the video")


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]  
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id:args}
      
api.add_resource(Video, "/video/<int:video_id>")    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>") #parameters in request url

if __name__ == "__main__":
    app.run(debug = True)