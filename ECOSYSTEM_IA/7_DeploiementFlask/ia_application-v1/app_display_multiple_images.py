import os
import random
from flask import Flask, request, render_template, send_from_directory, redirect

# -----------------------------------------------------------------------------
__author__ = 'moi'

# -----------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = "Aas1!..@@aaa"
app.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000 # 1MB
app.config["UPLOAD"] = os.path.join("static", "images")

os.makedirs(app.config["UPLOAD"], exist_ok=True)

# -----------------------------------------------------------------------------
def process_image(filename):
    results = ["POSTIVO", "NEGATIVO"]

    return {"status": random.choice(results), "acc": f"{random.random():.2f}", "status": random.choice(results)}
# -----------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("complete_display_image.html")
# -----------------------------------------------------------------------------
@app.route("/upload", methods=["POST"])
def upload():
    filename=""
    for upload in request.files.getlist("file"):
        if upload.filename == "":
            continue
        filename = os.path.join(app.config["UPLOAD"],upload.filename)
        upload.save(filename)
        app.logger.debug(f"Uploading {filename}")
        # ==== PROCESS IMAGE
        result = process_image(filename)
        return render_template("gallery.html", filename=upload.filename, result=result), 301
    return redirect('/')
# -----------------------------------------------------------------------------
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory(app.config["UPLOAD"], filename)
# -----------------------------------------------------------------------------
@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    app.logger.debug(image_names)
    return render_template("gallery.html", image_names=image_names)

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(port=4555, debug=True)