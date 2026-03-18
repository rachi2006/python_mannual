from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    name = "Rachith kumar"
    course = "python"
    return render_template("index.html", name= name, course=course)
if __name__ == "__main__":
    app.run(debug=True)