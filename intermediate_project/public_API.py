'''
able to view this page in this like
https://iambatman.pythonanywhere.com/
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return ("Hello World")

@app.route('/me')
def me():
    user_name = request.args.get('name', type=str,default='Batman')

    if isinstance(user_name, str):
        return f"Hello {user_name}"
    else:
        return "Enter a valid input"

if __name__ == '__main__':
    app.run()
