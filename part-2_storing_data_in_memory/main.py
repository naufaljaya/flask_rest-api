from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos
        
    def post(self,video_id):
        print(request.form)
        return {}

api.add_resource(Video,'/video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
