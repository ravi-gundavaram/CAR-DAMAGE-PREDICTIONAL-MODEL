from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
model = tf.keras.models.load_model('models/car_damage_classifier.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Log that a request has been received
    logging.info(f"Received request for prediction.")

    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (224, 224)) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    result = 'damaged' if prediction < 0.5 else 'not-damaged'

    # Log the prediction result
    logging.info(f"Prediction result: {result}")
    
    return jsonify({'classification': result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
