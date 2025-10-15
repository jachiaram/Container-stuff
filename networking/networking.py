from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello():
    return "hi from webserver", 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
