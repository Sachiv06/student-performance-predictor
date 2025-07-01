import joblib

model = joblib.load('model.pkl')

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
prev_score = float(input("Enter previous score: "))

data = [[hours, attendance, prev_score]]
result = model.predict(data)[0]

print("Likely to Pass ✅" if result else "At Risk ❌")
