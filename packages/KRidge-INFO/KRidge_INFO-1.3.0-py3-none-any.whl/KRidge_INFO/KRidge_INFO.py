# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:40:34 2024

@author: user
"""

import numpy as np  
from info_optimizer import INFO  
from objective_function import objective_function_KRidge,Extract_PredictedValues_KRidge


def RUN_INFO (nP, MaxIt,X_train, X_test, y_train, y_test,kernel_type,UC,UKF):

    # Define dimensionality based on kernel type  
    dim = 4 if kernel_type == 'wavelet' else 2  

    # Set optimizer parameters  
    lb = np.zeros(dim)  
    ub = np.ones(dim)   
 

    fobj= lambda x: objective_function_KRidge(x, X_train, X_test, y_train, y_test, kernel_type,UC,UKF)

    # Run optimization using the imported function  
    optimized_result = INFO(lb=lb, ub=ub, dim=dim, nP=nP, MaxIt=MaxIt,fobj=fobj)  
                        

    # Extract and print results  
    best_parameters = optimized_result.Best_X 
    return best_parameters



def PredictedValue_TrainTest(best_parameters, kernel_type, 
                         X_train, y_train,X_test, y_test,UC,UKF):
   
   y_train_pred, y_train,y_test_pred,y_test = Extract_PredictedValues_KRidge(best_parameters, kernel_type, 
                            X_train, y_train,X_test, y_test,UC,UKF)
   return y_train_pred, y_train,y_test_pred,y_test
