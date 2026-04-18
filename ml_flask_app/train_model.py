import pandas as pd #data handling
import pickle #save and load trained ML models.Loads model later for prediction(Flask/web app)
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import GradientBoostingRegressor#Combines multiple weak models to give strong prediction.
from sklearn.metrics import r2_score #Used to check model accuracy.more near to one more better

#Loading dataset
df = pd.read_csv("car_csv.csv")
df = df.dropna()#remove missing/null vals

#Split brand and model from name
df["brand"] = df["name"].apply(lambda x: x.split()[0])
df["model"] = df["name"].apply(lambda x: " ".join(x.split()[1:3]))
df = df.drop("name", axis=1)

#feature engineering
# created new features like car age, km per year, luxury indicator and brand-model 
# combination to improve model accuracy.
current_year = 2026
df["car_age"] = current_year - df["year"]#lesser more price

df["km_per_year"] = df["km_driven"] / df["car_age"]
df["km_per_year"] = df["km_per_year"].fillna(df["km_driven"])#More usage → less price

df["age_squared"] = df["car_age"]**2#Captures non-linear relation between age & price

luxury_brands = ["BMW","Mercedes-Benz","Audi","Jaguar","Land"]
df["is_luxury"] = df["brand"].apply(lambda x: 1 if x in luxury_brands else 0)#Luxury cars → higher price

df["brand_model"] = df["brand"] + "_" + df["model"]

#brand and model for drop down menu
brand_list = sorted(df["brand"].unique().tolist())
model_list = sorted(df["model"].unique().tolist())

#one hot encoding
df = pd.get_dummies(df, drop_first=True) #categorical → numerical

#Split features and target
X = df.drop("selling_price", axis=1)
y = df["selling_price"]


#train and test data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = GradientBoostingRegressor(
    n_estimators=500,#no of trees
    learning_rate=0.05,
    max_depth=5,#max depth to avoid overfitting
    random_state=42
)

model.fit(X_train, y_train) 

#Evaluation
y_pred = model.predict(X_test)

print("\n MODEL PERFORMANCE")
print("R2 Score:", r2_score(y_test, y_pred))


#Save everything in one .pkl file
data_to_save = {
    "model": model,
    "columns": X.columns,
    "brand_list": brand_list,
    "model_list": model_list
}

pickle.dump(data_to_save, open("model.pkl", "wb"))#wb is write binary

print("\n All files saved in single model.pkl file")
