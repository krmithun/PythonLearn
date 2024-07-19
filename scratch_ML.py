from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Data cleaning
df.dropna(inplace=True)

# Data transformation
df['new_column'] = df['existing_column'] * 2

# Descriptive statistics
print(df.describe())

# Load data
X = df.drop('target', axis=1)
y = df['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print('Accuracy:', accuracy_score(y_test, y_pred))
