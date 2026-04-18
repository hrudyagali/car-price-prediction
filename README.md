# Car Price Prediction Using Flask

## Overview
This project is a machine learning-based web application that predicts the selling price of used cars in India. It uses a Gradient Boosting Regressor model trained on real-world data and is deployed using Flask to provide an interactive user interface.

---

## Tech Stack
- Machine Learning: Scikit-learn (Gradient Boosting Regressor)
- Backend: Flask
- Programming Language: Python
- Libraries: NumPy, Pandas

---

## Project Structure
```
ml_flask_app/
│
├── app.py              # Flask application
├── model.pkl           # Trained model (generated after training)
├── requirements.txt    # Project dependencies
├── train_model.py      # Script to train the model
└── templates/
    └── index.html      # Frontend interface
```

---

## Installation and Setup

### 1. Clone the repository
```
git clone https://github.com/hrudyagali/car-price-prediction
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Train the model
```
python train_model.py
```

### 4. Run the Flask application
```
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000/
```

---

## Dataset
Source: Kaggle

The dataset contains information about used cars in India and includes the following features:

- car_name: Full name of the car  
- brand: Manufacturer of the car  
- model: Specific model name  
- seller_type: Type of seller  
- fuel_type: Fuel used  
- transmission_type: Transmission type  
- vehicle_age: Age of the vehicle  
- mileage: Distance per litre  
- engine: Engine capacity (cc)  
- max_power: Maximum power (BHP)  
- seats: Number of seats  
- selling_price: Target variable  

---

## How It Works
- The model is trained using historical car data  
- User inputs are collected through the web interface  
- The Flask backend processes the input and sends it to the trained model  
- The model predicts the selling price  
- The predicted price is displayed to the user  

---

## Features
- Predicts used car prices based on multiple parameters  
- Simple and interactive web interface  
- Integration of machine learning model with a web application  
- Easy to run locally  
