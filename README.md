Stock Price Prediction & Investor Sentiment Analysis
A full-stack web application developed using Django and Machine Learning to predict stock market trends (Uptrends/Downtrends) based on investor sentiment and historical datasets.

🚀 Overview
This project leverages a Voting Classifier—combining SVM, Logistic Regression, and Decision Trees—to analyze investor sentiment. It provides two distinct interfaces: a Remote User portal for individual predictions and a Service Provider (Admin) dashboard for system monitoring, model training, and data visualization.

🛠️ Tech Stack
Backend: Python 3.x, Django Framework

Frontend: HTML5, CSS3, JavaScript

Machine Learning: Scikit-learn, Pandas, NumPy

Algorithms: DNN, SVM, Logistic Regression, Decision Tree, K-Neighbors, Gradient Boosting

Database: SQLite (Default Django) / MySQL

Tools: VS Code, PowerShell, Git


Shutterstock
📋 Features
Remote User Flow
Authentication: Secure User Registration and Login system.

Profile Management: View and manage user-specific details.

Sentiment Prediction: Input stock-related text to predict market trends using a trained Voting Classifier.

History: All user predictions are stored for future reference.

Service Provider (Admin) Flow
User Management: Monitor all registered remote users.

Model Training: Trigger real-time training on Datasets.csv and view performance metrics (Accuracy, Confusion Matrix, Classification Report).

Data Analysis: View prediction ratios (Uptrends vs. Downtrends) via interactive charts.

Export Data: Download all system-generated predictions as an Excel (.xls) file for offline analysis.

⚙️ Installation & Setup
Clone the Repository

Bash
git clone https://github.com/jahid3145/StockPrice-Code.git
cd StockPrice-Code
Create a Virtual Environment (Optional but Recommended)

Bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
Install Dependencies

Bash
pip install django pandas numpy scikit-learn xlwt
Run Migrations

Bash
python manage.py makemigrations
python manage.py migrate
Start the Server

Bash
python manage.py runserver
Access the app at: http://127.0.0.1:8000/

📊 Model Performance
The system evaluates multiple algorithms to ensure the highest prediction accuracy. The admin can compare:

Deep Neural Networks (DNN)

Support Vector Machines (SVM)

Gradient Boosting

Logistic Regression

🔐 Admin Credentials
To access the Service Provider dashboard:

URL: /serviceproviderlogin/

Username: Admin

Password: Admin

📂 Project Structure
Plaintext
├── StockPrice-Code/
│   ├── manage.py
│   ├── Datasets.csv              # Training data
│   ├── Predicted_Datasets.xls    # Generated reports
│   ├── assets/                   # Static files (CSS/JS/Images)
│   └── ...                       # Django App folders & templates
