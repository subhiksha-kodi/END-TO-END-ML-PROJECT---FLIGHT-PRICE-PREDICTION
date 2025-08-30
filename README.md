# ✈️ Flight Price Prediction App

This is a **Streamlit web application** that predicts flight ticket prices based on multiple features such as airline, source city, destination city, class, number of days left, duration, and other relevant information.

## 🚀 Features
- User-friendly interface built with **Streamlit**.
- Select airline, source city, destination city, and class from dropdowns.
- Enter numeric values (e.g., days left, duration).
- Predicts the estimated flight ticket price in **Indian Rupees (₹)**.
- Automatically adapts to all dataset features (except target column `price`).

## 📂 Project Structure
```
.
├── app.py                 # Streamlit app
├── model.pkl              # Trained GradientBoostingRegressor model
├── label_encoders.pkl     # Saved LabelEncoders for categorical features
├── cleaned_dataset.csv    # Training dataset
├── train_model.py         # Script to retrain the model
└── README.md              # Project documentation
```

## ⚙️ Installation

1. Clone the repository or download the project files.

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Required libraries:
- pandas
- scikit-learn
- streamlit
- pickle (standard library)

3. Make sure you have `cleaned_dataset.csv` in the same folder.

## 🏋️ Training the Model
Run the training script to retrain and save the model:
```bash
python train_model.py
```

This will generate:
- `model.pkl` – trained GradientBoostingRegressor model
- `label_encoders.pkl` – label encoders for categorical columns

## ▶️ Running the App
Start the Streamlit app with:
```bash
streamlit run app.py
```

The web app will open in your browser at `http://localhost:8501`.

## 📊 Dataset
The dataset used (`cleaned_dataset.csv`) contains flight details with features like:
- Airline
- Source City
- Destination City
- Class
- Days Left
- Duration (hours & minutes)
- Stops
- Arrival & Departure Time
- Price (target variable)

⚠️ Note: The model is trained on **all columns except `price`**.

## ✅ Example Usage
1. Select an airline (e.g., IndiGo).
2. Choose source city and destination city.
3. Enter days left before departure (e.g., 15).
4. Input duration in hours and minutes.
5. Click **Predict Price** to get the estimated flight ticket price.

## 🛠️ Future Improvements
- Add data visualizations for flight trends.
- Improve model accuracy using hyperparameter tuning.
- Deploy the app on **Streamlit Cloud / Heroku / AWS**.

---

💡 Developed with ❤️ using Python, scikit-learn, and Streamlit.
