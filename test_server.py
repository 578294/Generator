from flask import Flask, render_template, request
from test import ConnectGenerator

test_server = Flask(__name__)

@test_server.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index1.html")
    ConnectGenerator.username = request.form["username"]
    ConnectGenerator.hostname = request.form["hostname"]
    ConnectGenerator.port = request.form["port"]
    ConnectGenerator.password = request.form["password"]
    return f"Привет, {ConnectGenerator.username}!"

if __name__ == "__main__":
    test_server.run(debug=True)