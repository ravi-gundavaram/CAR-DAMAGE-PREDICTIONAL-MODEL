import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

data_dir = "C:/Users/SONY/Downloads/Car-Damage-Model/data/raw"
def load_images(data_dir):
    images = []
    labels = []
    for label in ['damaged', 'not-damaged']:
        path = os.path.join(data_dir, label)
        print(f"Checking path: {path}")
        if not os.path.exists(path):
            print(f"Path does not exist: {path}")
            continue

        if len(os.listdir(path)) == 0:
            print(f"No images found in directory: {path}")
            continue

        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Could not read image: {img_path}")
                continue
            img = cv2.resize(img, (224, 224))
            images.append(img)
            labels.append(0 if label == 'damaged' else 1)
    return np.array(images), np.array(labels)


import os

def preprocess_and_split(data_dir, output_dir):
    X, y = load_images(data_dir)
    X = X / 255.0  # Normalize the images

    X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    np.save(os.path.join(output_dir, 'X_train.npy'), X_train)
    np.save(os.path.join(output_dir, 'y_train.npy'), y_train)
    np.save(os.path.join(output_dir, 'X_val.npy'), X_val)
    np.save(os.path.join(output_dir, 'y_val.npy'), y_val)
    np.save(os.path.join(output_dir, 'X_test.npy'), X_test)
    np.save(os.path.join(output_dir, 'y_test.npy'), y_test)

if __name__ == "__main__":
    preprocess_and_split("data/raw", "data/processed")


