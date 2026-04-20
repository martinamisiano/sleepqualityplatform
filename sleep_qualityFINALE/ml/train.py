import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.DataFrame({
    "age":[25,40,30,35],
    "stress":[7,3,5,8],
    "activity":[3,5,4,2],
    "bmi":[22,27,24,26],
    "target":["Poor","Good","Good","Poor"]
})

X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,"../backend/model/model.pkl")
