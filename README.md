# car-price-prediction-using-flask-
Developed a machine learning model using Gradient Boosting Regressor to predict used car prices , Built a Flask-based web application to take user input and display predicted price.
ml_flask_app/ 
│ 
├── app.py 
├── model.pkl 
├── requirements.txt 
├──train_model.py
└── templates/ 
└── index.html 


Run the train_model.py file to get the model.pkl file 

app.py is the flask application

 Requirements File (requirements.txt) 
1.flask 
2.numpy 
3.pandas 
4.scikit-learn 

The dataset is taken from kaggle.com

About this Dataset
The used car market in India is a dynamic and ever-changing landscape. Prices can fluctuate wildly based on a variety of factors including the make and model of the car, its mileage, its condition and the current market conditions. As a result, it can be difficult for sellers to accurately price their cars.

This dataset contains information about used cars.
This data can be used for a lot of purposes such as Used Car Price Prediction using different Machine Learning Techniques.

Data Description (Feature Information)

car_name: Car's Full name, which includes brand and specific model name.
brand: Brand Name of the particular car.
model: Exact model name of the car of a particular brand.
seller_type: Which Type of seller is selling the used car
fuel_type: Fuel used in the used car, which was put up on sale.
transmission_type: Transmission used in the used car, which was put on sale.
vehicle_age: The count of years since car was bought.
mileage: It is the number of kilometer the car runs per litre.
engine: It is the engine capacity in cc(cubic centimeters)
max_power: Max power it produces in BHP.
seats: Total number of seats in car.
selling_price: The sale price which was put up on website.

