from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getdata", methods=["POST"])
def getdata():
    name = request.form["name"]
    message = "Hello " + name
    return jsonify({"result": message})

if __name__ == "__main__":
    app.run(debug=True)