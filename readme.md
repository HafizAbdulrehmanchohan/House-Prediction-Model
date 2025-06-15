# 🏡 House Price Prediction using Support Vector Regression (SVR)

This project demonstrates a full machine learning pipeline for predicting house prices using Support Vector Regression (SVR) and the principles of Object-Oriented Programming (OOP) in Python. The notebook walks through data loading, preprocessing, EDA, model training, and evaluation.

## 📁 Project Structure


## 🔧 Technologies Used

- **Python 3**
- **Jupyter Notebook**
- **Pandas, NumPy** – for data manipulation
- **Matplotlib, Seaborn** – for visualization
- **Scikit-learn (sklearn)** – for model training and evaluation
- **Pickle** – for model serialization

## 📊 Workflow Overview

### 📥 Step 1: Data Collection & Understanding
- Load the dataset using a custom `DataCollector` class.
- Preview, describe, and summarize the dataset.

### 🧹 Step 2: Data Preprocessing
- Handle missing values and outliers.
- Encode categorical features (if any).
- Normalize features using `StandardScaler`.

### 📈 Step 3: Exploratory Data Analysis (EDA)
- **Univariate Analysis**: Distribution of features (e.g., price, area, etc.).
- **Bivariate Analysis**: Relationships between variables (e.g., price vs. area).

### ✂ Step 4: Data Splitting
- Split the dataset into training and testing sets using `train_test_split`.

### 🤖 Step 5: Model Training (Support Vector Regression)
- Implement a `HousePriceModel` class using SVR from Scikit-learn.
- Train the model on the training set.

### ✅ Step 6: Model Evaluation
- Evaluate performance using RMSE and R² Score.
- Analyze predictions vs. actual prices.

### 💾 Step 7: Model Saving
- Save the trained model using `pickle` for future inference.

## 🚀 How to Run

1. Clone this repository or download the `.ipynb` file.
2. Ensure required libraries are installed:
   ```bash
   pip install pandas numpy seaborn matplotlib scikit-learn
