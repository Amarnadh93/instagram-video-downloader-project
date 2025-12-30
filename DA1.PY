import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# =====================================================
# 1. LOAD DATA
# =====================================================
df = pd.read_csv("C:\\Users\\Amar\\OneDrive\\Desktop\\python\\government_scheme_dataset.csv")

# =====================================================
# 2. DATA PREPROCESSING
# =====================================================
# Encode categorical features
le_category = LabelEncoder()
le_gender = LabelEncoder()
le_scheme = LabelEncoder()

df["category_enc"] = le_category.fit_transform(df["category"])
df["gender_enc"] = le_gender.fit_transform(df["gender"])
df["scheme_enc"] = le_scheme.fit_transform(df["eligible_scheme"])

X = df[["age", "annual_income", "category_enc", "gender_enc"]]
y = df["scheme_enc"]

# =====================================================
# 3. TRAIN-TEST SPLIT
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =====================================================
# 4. MODEL TRAINING
# =====================================================
model = DecisionTreeClassifier(
    max_depth=6,
    min_samples_split=10,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================================
# 5. MODEL EVALUATION
# =====================================================
y_pred = model.predict(X_test)

print("\nModel Performance")
print("-----------------")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# =====================================================
# 6. USER PREDICTION
# =====================================================
print("\nGovernment Scheme Prediction")
print("----------------------------")

age = int(input("Enter age: "))
income = int(input("Enter annual income: "))
category = input("Enter category (Student/Farmer/Senior/Disabled/General): ").strip().title()
gender = input("Enter gender (Male/Female): ").strip().title()

user_data = pd.DataFrame([{
    "age": age,
    "annual_income": income,
    "category_enc": le_category.transform([category])[0],
    "gender_enc": le_gender.transform([gender])[0]
}])

prediction = model.predict(user_data)[0]
predicted_scheme = le_scheme.inverse_transform([prediction])[0]

print("\nPredicted Eligible Scheme:")
print("→", predicted_scheme)