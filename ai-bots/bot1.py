import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Fetch historical stock data
stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

data = stock[["Close"]]
data.head

# Create technical indicators
data["SMA_10"] = data["Close"].rolling(window=10).mean()
data["SMA_50"] = data["Close"].rolling(window=50).mean()
data["Momentum"] = data["Close"] - data["Close"].shift(5)

# Define target variable (future peice movement)
data["Target"] = (data["Close"].shift(-1) > data["Close"].astype(int)) # 1 = Price up, 0 = Price Down

# Drop NaN values
data.dropna(inplace=True)

# Features (x) and target (y)
x = data[["SMA_10", "SMA_50", "Momentum"]]
y = data["Target"]

data.head()

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, shuffle=False)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

# Predict on test set
y_pred = model.predict(x_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))