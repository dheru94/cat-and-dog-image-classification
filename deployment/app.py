from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import os

app = Flask(__name__)

# Load the SavedModel
model = tf.keras.models.load_model("saved_models/1/")  # Path to your saved model folder

# Preprocess function for input image
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((256, 256))  # or (size your model expects)
    img_array = np.array(image) / 255.0
    return np.expand_dims(img_array, axis=0)  # shape = (1, 224, 224, 3)

@app.route("/")
def index():
    return render_template("index.html")  # If you are serving frontend too

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty file"}), 400

    try:
        image_bytes = file.read()
        input_tensor = preprocess_image(image_bytes)
        prediction = model.predict(input_tensor)

        predicted_class = 1 if prediction[0][0] > 0.5 else 0  # 0 or 1

        label = "dog" if predicted_class == 1 else "cat"
        
        print("yoyo:", prediction)
        print("yoyo:", predicted_class)
        print("Prediooction:", label)
        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=8000)
