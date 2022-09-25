
from flask import Flask, render_template, request, valid_login

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

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return (request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run(debug=True);

