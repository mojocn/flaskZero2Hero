from flask import Flask, Response
from flask import request
import json


app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'post-login'
    else:
        return 'view login form'




@app.route('/json')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
