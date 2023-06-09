from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required = True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required = True)

videos = {}

def isVidNotExists(video_id):
    if video_id not in videos.keys():
        abort(http_status_code=404, message="Video id is not exists...")

class Video(Resource):
    def get(self, video_id):
        isVidNotExists(video_id)
        return videos
        
    def post(self,video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video,'/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
