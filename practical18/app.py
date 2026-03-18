from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# create uploads folder if not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

    return "File uploaded successfully <br><a href='/'>Go Back</a>"


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)