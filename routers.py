import requests
from flask import jsonify, request
from repostories import get_comments, create_comment
from app import app
import time


@app.route('/posts/<int:post_id>/comments', methods = ['GET', "POST"])
def comments(post_id):
    if request.method == 'POST':
        content = request.json['content']
        new_comment = create_comment(content=content, blog_id=post_id)
        post_data = {
            'type': 'CommentCreated',
            'data': new_comment
        }
        requests.post('https://microservices-eventbus-service.herokuapp.com/events', json=post_data)
        return jsonify(new_comment), 201
    time.sleep(1)    
    comments = get_comments(blog_id=post_id)
    return jsonify(comments), 200