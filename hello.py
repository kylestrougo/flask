from flask import Flask , redirect
from flask_script import Manager
##from flask_script._compat import text_type

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return redirect("https://www.google.com/?client=safari")
#test
if __name__ == '__main__':
    manager.run()