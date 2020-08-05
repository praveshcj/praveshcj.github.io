# app.py
from flask import Flask, request, jsonify, send_file, render_template
app = Flask(__name__, static_folder='./build', static_url_path='/')
# app= Flask(__name__)


@app.route('/')
def index():
    template = open('./build/index.html', 'r');
    print(template);
    return app.send_static_file('index.html')



@app.route('/profilepic', methods=['GET'])
def respond():
    pic = open('profilepic.jpg', 'rb')
    return send_file(pic, mimetype='image/JPG')

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)