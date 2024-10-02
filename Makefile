preprocess:
    python data_preprocessing.py

train:
    python model_training.py

all: preprocess train
