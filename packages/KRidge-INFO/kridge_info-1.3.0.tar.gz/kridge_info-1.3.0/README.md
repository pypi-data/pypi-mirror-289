# INFO-Optimized Kernel Ridge Regression (KRidge)  

This code implements a Kernel Ridge Regression (KRidge) model optimized using the **INFO** (Weighted Mean of Vectors Optimization) algorithm. The provided implementation focuses on predicting a target variable from a dataset and evaluating its performance using various metrics.  

## Features  

- **KRidge Regression:** A powerful non-linear regression technique using kernel functions to capture complex relationships in data.  
- **INFO Optimization:** Employs the INFO algorithm to determine optimal hyperparameters for the KRidge model, enhancing its predictive accuracy.  
- **Performance Evaluation:** Calculates and saves a comprehensive set of regression metrics (R2, RMSE, MAPE, KGE, NSE, WHD, VSD, WAI) to assess model performance on training and testing datasets.  
- **Excel Output:** Saves the calculated metrics and actual vs. predicted values into a well-structured Excel file for easy analysis and comparison.  

## Requirements  

- Python 3.x  
- Libraries: pandas, scikit-learn, openpyxl (install using `pip install pandas scikit-learn openpyxl`)  
- `Metrics.py`: A separate Python file containing the `Save_Metrics` function (provided in previous responses).  
- `Run_INFO.py`: A separate Python file containing the `RUN_INFO` and `PredictedValue_TrainTest` functions.  

## Usage  

1. **Data Preparation:**  
   - Ensure your dataset is in an Excel file (e.g., 'Data.xlsx').  
   - The last column of the dataset should contain the target variable you want to predict.  

2. **Configuration:**  
   - **`nTs`:** Specifies the percentage of data to be used for testing (e.g., 0.3 for 30%).  
   - **`kernel_type`:** Defines the kernel function to be used in KRidge (e.g., 'wavelet', 'rbf', etc.).  
   - **`nP`:** The number of particles for the INFO optimization algorithm.  
   - **`MaxIt`:** The maximum number of iterations for the INFO algorithm.  
   - **`UC`:** Upper bound for the KRidge regularization parameter (C).  
   - **`UKF`:** Upper bound for the KRidge kernel function coefficient.

3. **Running the Code:**  
   - Execute the Python script.  
   - The optimized KRidge model will be trained, and results will be saved to 'Results of KRidge.xlsx'.  

## Output  

The code will generate an Excel file named 'Results of KRidge.xlsx' containing the following sheets:  

- **Metrics:** Summarizes the calculated regression metrics for both training and testing sets.  
- **Train_Predictions:** Shows the actual target values (`y_train`) and the corresponding model predictions (`y_train_pred`) for the training dataset.  
- **Test_Predict

*********************************************************************************
*********************************************************************************

Eample: 

import pandas as pd  
from sklearn.model_selection import train_test_split  
from IM_Metrics import Save_Metrics
from KRidge_INFO import RUN_INFO,PredictedValue_TrainTest 

# Read data  
data = pd.read_excel('Data.xlsx')   

nTs = 0.3  # Percentage of test dataset     
X = data.iloc[:, :-1].values  
y = data.iloc[:, -1].values  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=nTs, random_state=0)  
    
 
kernel_type = 'wavelet'  
nP = 50
MaxIt = 20
UC = 2e10    #Upper Bound for C coefficient in KRidge model
UKF = 2e10   #Upper Bound for kernel function coefficient in KRidge model


best_parameters = RUN_INFO(nP, MaxIt,X_train, X_test, y_train, y_test,kernel_type,UC,UKF)

# After obtaining final predictions  

y_train_pred, y_train,y_test_pred,y_test = PredictedValue_TrainTest(best_parameters, kernel_type, 
                            X_train, y_train,X_test, y_test)

metrics_filename = 'Results of KRidge.xlsx'
Save_Metrics(y_train, y_train_pred, y_test, y_test_pred,metrics_filename)
