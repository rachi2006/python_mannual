from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("form.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    age = request.form["age"]

    message = f"<h2>Hello {name}, you are {age} years old. this is what your data is processed from server side</h2>"

    return message

if __name__ == "__main__":
    app.run(debug=True)