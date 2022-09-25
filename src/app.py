
from flask import Flask, render_template, request

app = Flask(__name__);

# Misc Functionality.
class user:
    def __init__(self, username, password) -> None:
        print("Creating User \n");
        # NOTE: An actual god - awful piece of code here.
        self.username = username;
        self.password = password;

class g_helper:
    def __init__(self) -> None:
        print("Debug Message. \n");


# Web functions.
@app.route("/")
def render():
    return render_template('p.html', the_title='pog');

@app.route("/home")
def hello_world():
    return render_template('main_page.html', the_title='pog');

