from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4F6nB5Qgu%jm@localhost:5432/flask_rest_api'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Video(name={name}, views={views}, likes={likes})'

#db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required = True)
video_put_args.add_argument("likes", type=int, help="Likes on the video is required", required = True)

videos = {}

def isVidNotExists(video_id):
    if video_id not in videos.keys():
        abort(http_status_code=404, message="Video id is not exists...")

def isVidExists(video_id):
    if video_id in videos.keys():
        abort(http_status_code=409, message="Video already exists...")

class Video(Resource):
    def get(self, video_id):
        isVidNotExists(video_id)
        return videos
        
    def post(self,video_id):
        isVidExists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        isVidNotExists(video_id)
        videos.pop(video_id)
        return '',204

api.add_resource(Video,'/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
