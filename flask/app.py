from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

@app.route("/params_in_url")
def params_in_url():
    data = request.args.get("x")
    return f"return the query params value = {data}"

if __name__=="__main__":
    app.run(host="0.0.0.0")