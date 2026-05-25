import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
s=pd.read_csv('diabetes.csv')
x=s[['Glucose','BloodPressure','BMI','Age']]
y=s['Outcome']
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.2,random_state=0)
model=LogisticRegression()
model.fit(x_train,y_train)
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")