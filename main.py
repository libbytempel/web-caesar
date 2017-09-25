from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/add" method="post">
            <label for="rot">
            Rotate by:
            <input type="text" name="rot" value="0"/><br>
            </label>
            <textarea type="text" name="text"/></textarea><br>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/add", methods=['POST'])
def encrypt():
    text = str(request.form['text'])
    rot = int(request.form['rot'])
    rotated=rotate_string(text,rot)
    content = "<h1>" + rotated + "</h1>"
    return content

app.run()