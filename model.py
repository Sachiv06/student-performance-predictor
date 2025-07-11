import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('student_data.csv')
X = df[['Hours', 'Attendance', 'PreviousScore']]
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
