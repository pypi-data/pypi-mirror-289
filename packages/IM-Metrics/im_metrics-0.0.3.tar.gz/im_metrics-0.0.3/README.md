# Model Metrics and Excel Saver  

This Python package provides functions to calculate common model evaluation metrics and save the results along with predictions to an Excel file. It's designed to streamline the process of assessing and recording model performance.  

## Features  

- **Comprehensive Metrics:** Calculates R-squared (R2), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), Kling-Gupta Efficiency (KGE), Nash-Sutcliffe Efficiency (NSE), Wave Hedges Distance (WHD), Vicis Symmetric Distance (VSD), and Willmott's Agreement Index (WAI).  
- **Excel Export:** Organizes and saves the computed metrics and actual vs. predicted values into a well-structured Excel file for convenient analysis and sharing.  
- **Easy Integration:** Simple and intuitive API for straightforward integration into your machine learning workflows.  

## Installation  

Install the package using pip:  

```bash  
pip install Metrics

#Import Necessary Functions:

from Metrics import Save_Metrics

metrics_filename = 'Results of KRidge.xlsx'
Save_Metrics(y_train, y_train_pred, y_test, y_test_pred,metrics_filename)