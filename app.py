#!/bin/python3

from flask import Flask, render_template, redirect, url_for, flash, request
from rembg import remove
from PIL import Image
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'static/uploads/')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'your_secret_key_here'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return remove_bg(filepath)
    return render_template("index.html")

def remove_bg(filepath):
    input_image = Image.open(filepath)
    if input_image.mode == 'P':
        input_image = input_image.convert("RGBA")
    output_image = remove(input_image)
    output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    output_image.save(output_filepath)
    print(output_filepath)
    return render_template("end.html", file="uploads/output.png")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

