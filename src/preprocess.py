# preprocess.py
"""
This script handles preprocessing of images including resizing, normalization,
and other transformations needed for deepfake detection.
"""
import cv2
import numpy as np

def preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess an image."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image / 255.0  # Normalize to [0, 1]
    return image