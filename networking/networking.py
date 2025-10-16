from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def log_request_info():
	print(f"{request.url}")

@app.get("/")
def root():
	response = "Root says hello!"
	return response, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.get("/hello")
def hello():
	response = "Everything looks good!"
	return response, 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
