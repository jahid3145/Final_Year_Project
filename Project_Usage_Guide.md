# Stock Price Prediction Model - Project Usage Guide

This document provides a comprehensive guide on how to run, use, and check the Stock Price Prediction project. It covers instructions for both the **Remote User** and the **Service Provider** (Admin).

---

## 1. How to Run the Project

Before using the project, you must start the Django development server.

1. Open your terminal or command prompt.
2. Navigate to the project root directory where `manage.py` is located:
   ```bash
   cd C:\Users\DELL\Desktop\B.tech-Project\StockPrice-Code
   ```
3. Run the development server:
   ```bash
   python manage.py runserver
   ```
4. Once running, you should see output indicating the server is running at `http://127.0.0.1:8000/`. Do not close this terminal while you are using the application.

---

## 2. Remote User Flow

The **Remote User** represents a standard client who wants to predict stock trends.

### Accessing the Remote User Interface
- **Home Page**: Navigate to `http://127.0.0.1:8000/` in your web browser.

### Step-by-Step Usage:
1. **Register**
   - Go to the **Register** page (`http://127.0.0.1:8000/Register1/`).
   - Fill in your details: Username, Email, Password, Phone Number, Country, State, City, Address, and Gender.
   - Submit the form to successfully register your account.
2. **Login**
   - Go to the **Login** page (`http://127.0.0.1:8000/login/`).
   - Enter your registered `username` and `password`.
   - Upon successful login, you will be redirected to your profile view.
3. **View Profile**
   - After logging in, you can view your personal details on the **View Profile** page (`http://127.0.0.1:8000/ViewYourProfile/`).
4. **Predict Investor Sentiment Type**
   - Go to the **Predict Investor Sentiment** page (`http://127.0.0.1:8000/Predict_Investor_Sentiment_Type/`).
   - Fill out the form with details such as Investor Age, Gender, Date, Stock Text, Stock Name, and Company Name.
   - When you submit, the application will process the `Stock_Text` utilizing a Voting Machine Learning Classifier (SVM, Logistic Regression, Decision Tree) trained on `Datasets.csv`.
   - The application will output the prediction trend (e.g., **Uptrends** or **Downtrends**) and save this result to the database.

---

## 3. Service Provider Flow

The **Service Provider** acts as the system administrator, monitoring users, training models, and reviewing prediction metrics.

### Accessing the Service Provider Interface
- **Login Page**: Navigate to `http://127.0.0.1:8000/serviceproviderlogin/`.

### Step-by-Step Usage:
1. **Login**
   - Enter the hardcoded administrator credentials:
     - **Username:** `Admin`
     - **Password:** `Admin`
   - Upon logging in, previous detection accuracies will be reset, and you will be taken to the dashboard.
2. **View Remote Users**
   - Go to `http://127.0.0.1:8000/View_Remote_Users/`.
   - Here, you can see a list of all Remote Users who have registered on the platform, along with their details (email, location, etc.).
3. **Train Machine Learning Models**
   - Go to `http://127.0.0.1:8000/train_model/`.
   - This action will trigger the backend to load `Datasets.csv` and train multiple classification algorithms:
     - Deep Neural Network (DNN)
     - Support Vector Machine (SVM)
     - Logistic Regression
     - Decision Tree Classifier
     - K-Neighbors Classifier
     - Gradient Boosting Classifier
   - It will display the Accuracy, Classification Report, and Confusion Matrix for each model, recording the accuracy internally.
4. **View User Predictions**
   - Go to `http://127.0.0.1:8000/View_Prediction_Of_Investor_Sentiment_Type/`.
   - Review the history of all predictions made by the Remote Users (e.g., their inputs and whether the result was Uptrends or Downtrends).
5. **Analyze Prediction Ratios**
   - Go to `http://127.0.0.1:8000/View_Prediction_Of_Investor_Sentiment_Type_Ratio/`.
   - The system calculates the percentage ratio of overall **Uptrends** vs. **Downtrends** based on total predictions made and displays it to the admin.
6. **Download Prediction Datasets**
   - Go to `http://127.0.0.1:8000/Download_Predicted_DataSets/`.
   - Generates and downloads an Excel file (`Predicted_Datasets.xls`) containing all the prediction records made by the users.
7. **View Charts / Visualizations**
   - You can view graphical representations of the detection ratios and algorithm accuracies using the respective chart-related routes (`/charts/`, `/charts1/`, `/likeschart/`) as available in the Service Provider dashboard navigation.

---

## 4. How to Check/Verify the Project is Working Functionally
To quickly perform a functional test of the whole system:

1. Start the server via `python manage.py runserver`.
2. As a **Remote User**, create a test account via `/Register1/` and log in.
3. Submit a dummy prediction text at `/Predict_Investor_Sentiment_Type/`. Note if it successfully predicts Uptrend or Downtrend.
4. Open a new tab and go to `/serviceproviderlogin/`. Log in with username `Admin` and password `Admin`.
5. Under the Service Provider menu, go to "View Prediction of Investor Sentiment" and verify that your Remote User's recent prediction appears in the list.
6. Click "Train Model" and wait for it to process. Ensure that model accuracies are displayed successfully without errors.
7. Finally, try downloading the predicted dataset to ensure Excel serialization (`xlwt`) is working properly.
