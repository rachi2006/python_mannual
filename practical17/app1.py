from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app1 = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["loginDB"]
users = db["users"]

# Home → Login Page
@app1.route('/')
def home():
    return render_template("login.html")

# Register Page
@app1.route('/register')
def register_page():
    return render_template("register.html")

# Register Logic
@app1.route('/register_user', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    users.insert_one({
        "username": username,
        "password": password
    })

    return redirect('/')

# Login Logic
@app1.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = users.find_one({
        "username": username,
        "password": password
    })

    if user:
        return render_template("dashboard.html", username=username)
    else:
        return "Invalid Credentials ❌"

if __name__ == "__main__":
    app1.run(debug=True)