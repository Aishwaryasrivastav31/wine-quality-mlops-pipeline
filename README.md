🍷 Wine Insight: End-to-End MLOps Pipeline
This repository demonstrates a complete Machine Learning lifecycle—from raw data preprocessing and experiment tracking to deploying a production-ready API. The project achieves 97% accuracy in classifying wine categories based on their chemical composition.
Project Highlights
High Performance: Built a Random Forest Classifier with 97% accuracy.

MLOps Integration: Utilized MLflow for experiment tracking, parameter logging, and artifact management.

Scalable API: Deployed the model via FastAPI with Pydantic validation for real-time predictions.

Automated Documentation: Built-in Swagger UI for easy API testing.

🏗️ Technical Stack
Language: Python 3.10+

ML Framework: Scikit-Learn

Tracking: MLflow

API: FastAPI & Uvicorn

Data Handling: Pandas & NumPy

📊 Features Used for Prediction
The model focuses on the 5 most significant chemical markers:

hue

diluted_wines

proline

total_phenols

flavanoids

🛠️ Installation & Setup
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/wine-insight-api.git
cd wine-insight-api
Install dependencies:

Bash

pip install -r requirements.txt
Run the API server:

Bash

uvicorn main:app --reload
Test the API: Open your browser and go to http://127.0.0.1:8000/docs to access the interactive Swagger UI.

📈 Model Performance (MLflow)
Experiments were tracked using MLflow. Below is the summary of the best run:


Accuracy: 97%

Deployment Format: Pickle (.pkl)
