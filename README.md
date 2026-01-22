 🔍 Fraud Detection System

A machine learning-powered fraud detection application that identifies fraudulent financial transactions in real-time. Built with Python, scikit-learn, and Streamlit, it features an interactive web interface for analyzing transaction patterns.

 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

 🎯 Overview

This project implements a comprehensive fraud detection system designed to analyze financial transactions and predict potential fraudulent activities. The system uses machine learning algorithms trained on historical transaction data to identify suspicious patterns and flag potentially fraudulent transactions in real-time.

 ✨ Features

- **Real-time Fraud Detection**: Instantly analyze transactions and identify potential fraud
- **Interactive Web Interface**: User-friendly Streamlit dashboard for easy transaction input
- **Machine Learning Pipeline**: Pre-trained model with preprocessing and feature engineering
- **Multiple Transaction Types**: Supports Payment, Transfer, Cash Out, and Debit transactions
- **Balance Tracking**: Analyzes sender and receiver balance changes
- **Instant Results**: Immediate classification of transactions as legitimate or fraudulent

🛠️ Technologies Used

- **Python 3.10+**: Core programming language
- **Scikit-learn**: Machine learning algorithms and model building
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Seaborn**: Statistical data visualization
- **Matplotlib**: Plotting and charting
- **Streamlit**: Web application framework for interactive UI
- **Joblib**: Model serialization and deployment

 📊 Dataset Features

The model analyzes the following transaction attributes:

| Feature | Description |
|---------|-------------|
| Transaction Type | Payment, Transfer, Cash Out, or Debit |
| Amount | Transaction amount in currency units |
| Old Balance (Sender) | Sender's balance before transaction |
| New Balance (Sender) | Sender's balance after transaction |
| Old Balance (Receiver) | Receiver's balance before transaction |
| New Balance (Receiver) | Receiver's balance after transaction |

 🚀 Installation

 Prerequisites

- Python 3.10 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fraud-detection.git
cd fraud-detection
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install required dependencies**
```bash
pip install -r requirements.txt
```

4. **Ensure the model file is in the correct location**
```
Place Fraud_detection_pipline.pkl in the project directory
```

## 💻 Usage

1. **Run the Streamlit application**
```bash
streamlit run fraud_detection.py
```

2. **Access the web interface**
   - The application will automatically open in your default browser
   - Default URL: `http://localhost:8501`

3. **Make predictions**
   - Select the transaction type from the dropdown
   - Enter the transaction amount
   - Input sender's old and new balance
   - Input receiver's old and new balance
   - Click "Predict" to get the fraud detection result

## 📁 Project Structure

```
fraud-detection/
│
├── fraud_detection.py              # Main Streamlit application
├── Fraud_detection_pipline.pkl     # Trained ML model
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
├── notebooks/                      # Jupyter notebooks (optional)
│   └── model_training.ipynb        # Model training and EDA
└── data/                           # Dataset directory (optional)
    └── transactions.csv            # Training data
```

## 🎯 Model Information

### Algorithm
The fraud detection model uses a machine learning pipeline that includes:
- One-Hot Encoding for categorical features
- Feature scaling and normalization
- Classification algorithm (Random Forest/Logistic Regression/etc.)

### Performance Metrics
- **Accuracy**: High accuracy in classifying transactions
- **Precision**: Minimizes false positives
- **Recall**: Effectively identifies fraudulent transactions
- **F1-Score**: Balanced performance metric

## 📸 Screenshots

### Main Interface
![Fraud Detection App](screenshots/main_interface.png)
*User-friendly interface for entering transaction details*

### Prediction Result
![Prediction Result](screenshots/prediction.png)
*Real-time fraud detection results*

## 🔧 Requirements

```txt
streamlit==1.28.0
pandas==2.0.0
numpy==1.24.0
scikit-learn==1.0.2
seaborn==0.12.0
matplotlib==3.7.0
joblib==1.3.0
```

## 🔮 Future Enhancements

- [ ] Add model performance metrics dashboard
- [ ] Implement batch prediction for CSV file uploads
- [ ] Include transaction history and analytics
- [ ] Add explainability features (SHAP values)
- [ ] Deploy to cloud platforms (Heroku, AWS, or Azure)
- [ ] Implement user authentication
- [ ] Add API endpoints for integration
- [ ] Real-time monitoring and alerting system

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
--

⭐ **If you find this project useful, please consider giving it a star!** ⭐
