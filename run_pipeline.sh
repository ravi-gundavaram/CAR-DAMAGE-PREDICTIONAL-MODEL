#!/bin/bash
set -e

echo "Starting data preprocessing..."
python data_preprocessing.py

echo "Training the model..."
python model_training.py
