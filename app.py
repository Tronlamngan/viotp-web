from flask import Flask, render_template, request, jsonify
import requests, threading, time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    phone = request.form.get("phone")
    return jsonify({"status": "processing", "phone": phone})

if __name__ == "__main__":
    app.run(debug=True)
