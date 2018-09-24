from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from caesar import rotate_string

app = Flask(__name__)

main = '''
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
          <!-- create your form here -->
          <form>
            <label for="rot" placeholder="0">Rotate by: </label>
            <input name="rot"></input>
            <textarea name="text">{0}</textarea>
            <button>SUBMIT</button>
          </form>
        </body>
    </html>
'''

@app.route('/')
def index():
    #data = request.get('rot');
    #print(request)
    #print("This is after the request")
    #rot = int(rot)
    #text = chr(text)
    #encrypted = text(rotate_character)
    #return render_template("index.html")
    return main

@app.route('/', methods=["POST"])
def encrypt(rot, text):
    return "<h1>" + rot + "</h1>" + "<h1>" + text + "</h1>"


if( __name__ == "__main__"):
    app.run()
