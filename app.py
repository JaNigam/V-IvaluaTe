from flask import Flask, render_template, request, redirect, get_flashed_messages
import os
from flask.helpers import url_for
import pymongo
from werkzeug.utils import secure_filename


#python Scripts
import ocr 


UPLOAD_FOLDER = "./static/files"
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    filelocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text = ocr.extract_text(filelocation)

    #once the extraction is done remove the file from the folder
    os.remove(filelocation)
    return render_template('home.html', text = text)


if __name__ =="__main__":
    app.run(debug=True)
