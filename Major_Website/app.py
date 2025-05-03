from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model("lstm_ddos_model_2.h5")  # Your trained LSTM model

def preprocess_csv(file_path):
    df = pd.read_csv(file_path)

    drop_columns = ['Flow ID', 'Source IP', 'Destination IP', 'Timestamp']
    df.drop(columns=drop_columns, errors='ignore', inplace=True)

    for col in df.columns[:-1]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    numeric_cols = df.select_dtypes(include=np.number).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    for col in df.columns:
        if col != "Label":
            df[col] = df[col].fillna(df[col].median())

    scaler = StandardScaler()
    df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

    le = LabelEncoder()
    df['Label'] = le.fit_transform(df['Label'])
    label_names = le.classes_

    X = df.drop(columns=['Label'])
    y = df['Label']
    num_classes = len(label_names)

    y_categorical = to_categorical(y, num_classes=num_classes)
    X_lstm = np.reshape(X.values, (X.shape[0], 1, X.shape[1]))

    return X_lstm, y_categorical, label_names

@app.route('/')
def upload_page():
    return render_template("upload.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        X_input, y_true, label_names = preprocess_csv(filepath)

        y_pred_prob = model.predict(X_input)
        y_pred = np.argmax(y_pred_prob, axis=1)

        total = len(y_pred)
        benign_class_index = np.where(label_names == "Benign")[0][0]
        benign_count = np.sum(y_pred == benign_class_index)
        anomaly_count = total - benign_count

        benign_percent = round((benign_count / total) * 100, 2)
        anomaly_percent = round((anomaly_count / total) * 100, 2)

        return render_template("result.html", benign=benign_percent, anomaly=anomaly_percent)

    except Exception as e:
        return f"Error during prediction: {str(e)}", 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
