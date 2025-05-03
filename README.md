# 📊 Anomaly Detection Web App using LSTM

Welcome to the **Anomaly Detection Web App**! This website lets you **upload a CSV file**, runs it through a smart **LSTM machine learning model**, and shows:

- 🔍 How many records are **normal (BENIGN)** vs. **anomalous**
- 📊 A breakdown of different **anomaly types** like DDoS, SQL Injection, Web-XSS

---

## 🌟 What This App Does

1. You upload a `.csv` file containing traffic records.
2. The app processes the data in the background.
3. It uses a trained LSTM model (`.h5`) to predict the class of each row.
4. It then shows:
   - ✅ Percentage of **anomalous data**
   - 📊 How much each **attack type** appears

---

## 🧰 Technologies Used

- 🧠 TensorFlow/Keras (LSTM model)
- 🔧 Flask (Web framework)
- 🐍 Python (Data processing + backend)
- 💅 HTML + CSS (Frontend)

---

## 🚀 How to Run This App

### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/anomaly-lstm-app.git](https://github.com/Akshit0310/Major-Website.git)
cd anomaly-lstm-app

2. Install Python Dependencies
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Then install everything you need:

bash
Copy
Edit
pip install -r requirements.txt
3. Add Your LSTM Model
Put your trained .h5 model file in the project folder and name it:

Copy
Edit
lstm_ddos_model_2.h5
(If your file has a different name, update it in app.py.)

4. Start the App
bash
Copy
Edit
python app.py
Now go to http://127.0.0.1:5000 in your web browser.

📁 Folder Overview
graphql
Copy
Edit
anomaly-lstm-app/
│
├── app.py                # Main backend file
├── lstm_ddos_model_2.h5  # Your LSTM model file
├── uploads/              # Stores uploaded CSVs (auto-created)
├── templates/
│   ├── upload.html       # File upload page
│   └── result.html       # Result display page
├── static/
│   └── style.css         # Styling (optional)
├── requirements.txt      # Python packages
└── README.md             # This file
🧪 Example Output
Once your file is processed, you’ll see something like:

yaml
Copy
Edit
🚨 Anomalies Detected: 32.7%

🧠 Attack Breakdown:
- DDoS: 19.2%
- SQL Injection: 8.9%
- Web-XSS: 4.6%
🙋 FAQ
Q: What kind of CSV files should I upload?
A: Files should have a structure similar to the training data — with numeric features and a "Label" column.

Q: Can I change the model?
A: Yes! Just replace the .h5 file and make sure your input structure matches.

📝 License
This project is licensed under the MIT License. You’re free to use, share, and improve it!
