import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np

def create_model():
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False

    model = Sequential([
        base_model,
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    model = create_model()
    X_train = np.load('data/processed/X_train.npy')
    y_train = np.load('data/processed/y_train.npy')
    X_val = np.load('data/processed/X_val.npy')
    y_val = np.load('data/processed/y_val.npy')

    # Train the model
    model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    # Save the model
    model.save('models/car_damage_classifier.h5')
