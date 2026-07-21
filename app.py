from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Innovartus Cloud SaaS",
        "message": "Application is running successfully"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)