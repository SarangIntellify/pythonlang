from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__) #Flask class constructor needs the module name
api = Api(app) #initializing the rest api module using Api class.

#resource class must be child of Resource class so we can override the method of parent Resource class.

class HelloWorld(Resource):
    def get(self, name, test): #accessing the variable from request url
        return {"name": name, "test":test}
    
    def post(self):
        return {"data": "Helloworld from post"}
#parsing request json and adding validating
videos = {}    
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required",required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required",required=True)

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="Video_id is not valid, as it doesnt exists...") #it stops the further execution of code and send the message we write in paranthesis.
    
def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(400,message="Video already exists")
            
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id] #, 202 we can send status code.
    
    def put(self, video_id):
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id]
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204
        
      
api.add_resource(Video, "/video/<int:video_id>")    
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>") #parameters in request url

if __name__ == "__main__":
    app.run(debug = True)