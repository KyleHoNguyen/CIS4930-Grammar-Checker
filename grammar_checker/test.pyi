import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Load the data
train_data = pd.read_csv('train_data.csv')
validation_data = pd.read_csv('val_data.csv')
test_data = pd.read_csv('test_data.csv')

# Split the data into input and labels
# Split the data into input and labels
X_train = train_data['input']
y_train = train_data['labels']

X_val = validation_data['input']
y_val = validation_data['labels']

X_test = test_data['input']
# y_test = test_data['labels']


# Text preprocessing
vectorizer = TfidfVectorizer(max_features=5000)
X_train_features = vectorizer.fit_transform(X_train)
X_val_features = vectorizer.transform(X_val)
# X_test_features = vectorizer.transform(X_test)

# Model training
model = SVC(kernel='linear')
# model.fit(X_train_features, y_train)
model.fit(X_train_features, y_train)

# Model evaluation on validation data
y_val_pred = model.predict(X_val_features)
print("Validation Data Classification Report:")
print(classification_report(y_val, y_val_pred))

# # Model evaluation on test data
# y_test_pred = model.predict(X_test_features)
# print("\nTest Data Classification Report:")
# print(classification_report(y_test, y_test_pred))