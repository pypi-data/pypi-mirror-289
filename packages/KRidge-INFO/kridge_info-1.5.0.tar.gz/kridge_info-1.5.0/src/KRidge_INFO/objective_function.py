# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 04:11:18 2024

@author: user
"""

# objective_function.py  

import numpy as np  
from kernel_ridge_regression import KRidge_train, KRidge_test  

def objective_function_KRidge(x, X_train, X_test, y_train, y_test, kernel_type,UC,UKF):  
    x = np.ravel(x)  
    try:  
        WW1, kp, y_train_pred = KRidge_train(x, kernel_type, X_train, y_train,UC,UKF)  
        RMSE, y_test_pred = KRidge_test(WW1, kernel_type, kp, X_train, X_test, y_test)   
    except Exception as e:  
        print(f"Error during KRidge execution: {e}")  
        RMSE = np.inf      
    return RMSE



def Extract_PredictedValues_KRidge(best_parameters, kernel_type, 
                            X_train, y_train,X_test, y_test,UC,UKF):
    WW1, kp, y_train_pred = KRidge_train(best_parameters, kernel_type, X_train, y_train,UC,UKF)
    _, y_test_pred  = KRidge_test(WW1, kernel_type, kp, X_train, X_test, y_test)
    return y_train_pred, y_train,y_test_pred,y_test 
