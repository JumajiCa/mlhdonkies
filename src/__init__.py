
from flask import Flask, render_template

app = Flask(__name__);

@app.route("/main_page.html")
def hello_world():
    return "<h1>Hello, World!</h1> <p>uwu</p>"

def main() -> int:
    hello_world();
    return 0;

if __name__ == "__main__":
    app.run(debug=True);
