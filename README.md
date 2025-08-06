# Bengaluru House Price Prediction 🏡

This project uses machine learning to predict house prices in Bengaluru, India. It includes the entire workflow from data cleaning and feature engineering to model training and deployment. The final model is deployed as a simple, interactive web application using Streamlit.

## 🚀 Features

* **Data Cleaning & Preprocessing**: Handles missing values, performs feature engineering, and removes outliers to prepare the dataset for modeling.
* **Machine Learning Model**: A Linear Regression model is trained on the cleaned data to predict house prices.
* **Interactive Web App**: A user-friendly web application built with Streamlit allows for easy input and provides instant price predictions.
* **Reproducible Workflow**: A Jupyter Notebook (`.ipynb`) is included with a step-by-step walkthrough of the entire data science process.

## 🛠️ Technologies Used

* **Python**: The core programming language.
* **Pandas & NumPy**: For data manipulation, cleaning, and numerical operations.
* **Scikit-learn**: For building and evaluating the machine learning model.
* **Jupyter Notebook**: For interactive development and documentation.
* **Streamlit**: To create and deploy the web application.
* **Pickle**: For serializing the trained model.

## ⚙️ How to Run Locally

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/shriguruu/bengaluru-house-price-prediction
cd bengaluru-house-price-prediction
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Create a `requirements.txt` file with the following content:

```txt
pandas
numpy
scikit-learn
streamlit
```

Then, install the required libraries using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

Once the dependencies are installed, run the Streamlit application from your terminal:

```bash
streamlit run streamlit_app.py
```

This will open the web application in your default browser, typically at `http://localhost:8501`.

## 📂 File Structure

The repository is organized as follows:

```
.
├── banglore_home_prices_model.pickle  # The serialized trained model
├── bengaluru_house_price_prediction.ipynb # Jupyter notebook with the full workflow
├── columns.json                       # Data columns required for prediction
├── streamlit_app.py                   # The Streamlit web application script
├── requirements.txt                   # Project dependencies
└── README.md                          # This README file
```