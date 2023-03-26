import sys
sys.path.append("..")

import pandas as pd
import numpy as np
from helper.preprocessing import Preprocessing
from perceptron.perceptron import Perceptron
from helper.metrics import Metrics

df = pd.read_csv("../data/cancer.csv")
df.dropna(axis=0, inplace=True)


preprocessor = Preprocessing()

y = df.iloc[:, 1]
y = preprocessor.categorical_to_numerical(y)
X = df.drop(df.columns[[0, 1]], axis=1)

accuracy = 0
precision = 0
recall = 0
epochs = 10000

for i in range(1):
    X_train, X_test = preprocessor.train_test_split(
        X, train_size=0.67, random_state=2)
    y_train, y_test = preprocessor.train_test_split(
        y, train_size=0.67, random_state=2)
    X_train  = preprocessor.normalize(X_train)
    perceptron = Perceptron()
    perceptron.fit(X_train, y_train,epochs)
    X_test = preprocessor.normalize(X_test)
    y_pred = perceptron.predict(X_test)
    y_test = preprocessor.categorical_to_numerical(y_test)
    y_test = y_test.to_numpy()

    metrics = Metrics(y_pred, y_test)
    accuracy+=metrics.accuracy()
    precision+=metrics.precision()
    recall+=metrics.recall()

series = pd.Series([accuracy,precision,recall, epochs],index=["accuracy","precision","recall", "epochs"])
print(series)

    
