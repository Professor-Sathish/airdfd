# detect_art.py
"""
This script runs the detection pipeline for determining if art is AI-generated.
"""
import os
from preprocess import preprocess_image
from model import load_model, predict

def detect(input_dir, model_path, output_dir):
    """Run detection on a directory of images."""
    model = load_model(model_path)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        image = preprocess_image(file_path)
        prediction = predict(model, image)
        
        with open(os.path.join(output_dir, f"{file_name}.txt"), "w") as f:
            f.write(f"Prediction: {prediction[0]}")
