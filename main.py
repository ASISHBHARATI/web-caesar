from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <link rel="icon" type="image/png" href="images/orangeIcon.png">
            <style>
                html, body{{
                  background: url('https://images.unsplash.com/photo-1514820402329-de527fdd2e6d?ixlib=rb-0.3.5&s=5c41456ea7b33814c0507de11c14ec9b&auto=format&fit=crop&w=1952&q=80') no-repeat fixed;
                  -moz-background-size: cover;
                  -o-background-size: cover;
                  background-size: cover;
                }}
                form{{
                    background-color: #eee;
                    background-color: #80A7AF;
                    padding: 20px;
                    margin: 5vh auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                h1 {{
                    padding: 10vh 0 0 0;
                }}
                h1, p {{
                    font-family: verdana;
                    text-align: center;
                    color: white;
                }}
                input[type=submit] {{
                    background-color: white;
                    border: none;
                    padding: 10px 22px;
                }}
                footer {{
                    font-size: 14px;
                    font-family: verdana;
                    color: white;
                    position: absolute;
                    bottom: 0;
                    right: 0;
                }}
            </style>
        </head>
        <body>
            <h1>Web-Caesar Cipher</h1>
            <p><strong>Encryption </strong>Enter your message and the rotation number for letters to rotate by</p>

            <form action="/" method="POST">
                <label>Rotate by:
                 <input type="text" name="rot" value="0">
                </label>
                <textarea name="text">{0}</textarea>
                <input type="submit" value="Submit Query">
            </form>
            <footer>Presented by ASISH KUMAR BHARATI</footer>
        </body>
    </html>
"""

@app.route("/")
def index():
    new_string = ""
    return form.format(new_string)

@app.route("/", methods=['POST'])
def encrypt():
    text = str(request.form["text"])
    rot= int(request.form["rot"])
    encrypted_string = rotate_string(text,rot)
    
    return '<h1> ' + form.format(encrypted_string) + '</h1>'
app.run()


