from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

#load model and files
data = pickle.load(open("model.pkl", "rb"))

model = data["model"]
columns = data["columns"]
brand_list = data["brand_list"]
model_list = data["model_list"]

#home page
@app.route("/")
def home():
    return render_template("index.html",
                           brands=brand_list,
                           models=model_list)

#prediction route
@app.route("/predict", methods=["POST"])
def predict():
    brand = request.form["brand"]
    model_name = request.form["model"]
    year = int(request.form["year"])
    km = int(request.form["km"])
    fuel = request.form["fuel"]
    seller = request.form["seller"]
    transmission = request.form["transmission"]
    owner = request.form["owner"]

    # feature engineering (same as training)
    car_age = 2024 - year
    km_per_year = km if car_age == 0 else km/car_age
    age_squared = car_age**2
    luxury_brands = ["BMW","Mercedes-Benz","Audi","Jaguar","Land"]
    is_luxury = 1 if brand in luxury_brands else 0

    # empty dataframe with same columns
    input_df = pd.DataFrame(columns=columns)
    input_df.loc[0] = 0

    # numeric values
    input_df["year"] = year
    input_df["km_driven"] = km
    input_df["car_age"] = car_age
    input_df["km_per_year"] = km_per_year
    input_df["age_squared"] = age_squared
    input_df["is_luxury"] = is_luxury

    # categorical one-hot
    def set_col(name):
        if name in input_df.columns:
            input_df[name] = 1

    set_col("brand_" + brand)
    set_col("model_" + model_name)
    set_col("fuel_" + fuel)
    set_col("seller_type_" + seller)
    set_col("transmission_" + transmission)
    set_col("owner_" + owner)

    prediction = model.predict(input_df)[0]
    prediction = round(prediction, 2)

    return render_template("index.html",
                           prediction_text=f"Estimated Car Price: ₹ {prediction}",
                           brands=brand_list,
                           models=model_list)

# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)