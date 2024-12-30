# model.py
"""
This script defines the AI model used for detecting deepfake art.
"""
import tensorflow as tf

def load_model(model_path):
    """Load a pre-trained model from the specified path."""
    return tf.keras.models.load_model(model_path)

def predict(model, image):
    """Run a prediction on a preprocessed image."""
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return model.predict(image)
