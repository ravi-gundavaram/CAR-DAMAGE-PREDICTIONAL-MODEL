Car Damage Detection Model
Problem Statement
The goal of this project is to develop, containerize, and deploy a machine learning model for car damage classification using local and free-tier cloud resources. Specifically, the model should classify images of cars as either damaged or not damaged. The focus is on building a reproducible end-to-end machine learning pipeline that is ready for deployment.

Project Overview
This project includes:

Data preprocessing
Model development using a pre-trained model
Pipeline automation
Containerization of the model and API using Docker
Deployment using free-tier services (e.g., Heroku)
Implementation of logging for monitoring and debugging
CI/CD pipeline setup using GitHub Actions
Technologies Used
Python 3.12
TensorFlow
OpenCV
Flask
Docker
GitHub Actions (CI/CD)
Heroku (deployment)
Project Structure
graphql
Copy code
Car-Damage-Model/
│
├── data/
│   ├── raw/
│   │   ├── damaged/
│   │   └── not-damaged/
│   └── processed/
│       ├── X_train.npy
│       ├── y_train.npy
│       ├── X_val.npy
│       ├── y_val.npy
│       ├── X_test.npy
│       └── y_test.npy
│
├── app.py                  # Flask API for model predictions
├── data_preprocessing.py   # Script for data preprocessing
├── model_training.py       # Script for model training
├── Dockerfile              # Dockerfile to containerize the model and API
├── requirements.txt        # Python dependencies
├── run_pipeline.sh         # Bash script to run the entire pipeline
├── test_api.py             # Unit test for the Flask API
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions workflow for CI/CD
└── README.md               # Project documentation
Step-by-Step Guide
Step 1: Data Preprocessing
Download the Dataset:

Download the car damage detection dataset from Kaggle.
Place the downloaded images into data/raw/damaged/ and data/raw/not-damaged/.
Run the Preprocessing Script:

The data_preprocessing.py script will:

Resize and normalize the images.
Split the data into training, validation, and test sets.
Save the processed data for later use.
Command:


python data_preprocessing.py
Step 2: Model Development
Model Training:

We are using a pre-trained ResNet50 model to classify car damage.
The training script (model_training.py) loads the processed data, fine-tunes the model, and saves the trained model to the models/ directory.
Run the Model Training Script:

Command:

python model_training.py
Step 3: Pipeline Automation
Automate the Pipeline:
We have a bash script (run_pipeline.sh) that automates the entire pipeline, including data preprocessing and model training.
Command:

bash run_pipeline.sh
Step 4: REST API Development and Containerization
REST API Development:

We created a Flask API (app.py) that serves the model.
The API endpoint /predict accepts an image file and returns a classification result (damaged or not_damaged).
Logging:

Logging has been added to the API to track incoming requests and prediction results for debugging and monitoring purposes.
Containerization:

The Dockerfile is used to containerize the model and the API, making it easier to deploy across different environments.
Dockerfile Example:
dockerfile

FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the model and API files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
Build and Run the Docker Container:

Build the Docker Image:

docker build -t car_damage_classifier .
Run the Container:

docker run -p 5000:5000 car_damage_classifier
Step 5: Testing the API
Unit Testing:

A test script (test_api.py) is used to test the /predict endpoint of the Flask API.
Command:

pytest test_api.py
Manual Testing Using cURL:

You can also manually test the API using cURL:

curl -X POST -F "image=@path/to/sample_damaged.jpg" http://localhost:5000/predict
Step 6: CI/CD Setup with GitHub Actions
GitHub Actions Workflow:

We set up a CI/CD pipeline using GitHub Actions.
The workflow (.github/workflows/main.yml) performs the following tasks on every push:
Checkout the repository
Install dependencies
Run tests
Build and push the Docker image to a container registry
Example GitHub Actions Workflow:


name: CI/CD Pipeline

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Run Tests
        run: pytest

      - name: Build Docker Image
        run: docker build -t car_damage_classifier .

      - name: Push Docker Image to Docker Hub
        env:
          DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
          DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
        run: |
          echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
          docker push yourusername/car_damage_classifier
Step 7: Deployment
Deploy on Heroku:

We deployed the container to Heroku using their container registry.
Steps:
Login to Heroku:

heroku login
Create a new Heroku app:

heroku create car-damage-api
Push the Docker container to Heroku:

heroku container:push web --app car-damage-api
heroku container:release web --app car-damage-api
Access the API:

Use the Heroku-provided URL to make a prediction:

curl -X POST -F "image=@path/to/sample_damaged.jpg" https://car-damage-api.herokuapp.com/predict
Step 8: Monitoring and Logging
Logging in the API:

We used Python’s logging library to log incoming requests and prediction results.
This helps in monitoring the service and debugging issues.
Monitoring in the Cloud:

When deployed to the cloud, logs can be monitored using services like Heroku Logs or other cloud-native monitoring tools like AWS CloudWatch.
How to Use This Project
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/car-damage-model.git
cd car-damage-model
Create a Virtual Environment:


python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
Install Requirements:


pip install -r requirements.txt
Run the Preprocessing Script:


python data_preprocessing.py
Train the Model:


python model_training.py
Run the API:


python app.py
Docker Commands:

Build:

docker build -t car_damage_classifier .
Run:

docker run -p 5000:5000 car_damage_classifier
Future Improvements
Model Improvements: Explore other pre-trained models for better accuracy.
Model Deployment: Deploy to Kubernetes for better scalability.
Monitoring: Add more sophisticated monitoring using Prometheus and Grafana.
Auto-Retraining: Set up a pipeline for auto-retraining the model when drift is detected.
Conclusion
This project demonstrates an end-to-end workflow for developing, containerizing, and deploying a machine learning model for car damage classification. The solution is cloud-ready and employs good engineering practices, including logging, containerization, and automation via CI/CD pipelines.
