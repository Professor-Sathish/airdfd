# utils.py
"""
Utility functions shared across the project.
"""
import os

def ensure_dir(directory):
    """Ensure a directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")
