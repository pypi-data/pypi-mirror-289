# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:28:04 2024

@author: user
"""


import numpy as np  

def Ridge(X_train, y_train, X_test, lambda_):  
    """  
    Perform Ridge Regression.  

    Parameters:  
    X_train (numpy.ndarray): Training data features.  
    y_train (numpy.ndarray): Training data target values.  
    X_test (numpy.ndarray): Test data features.  
    lambda_ (float): Regularization parameter.  

    Returns:  
    tuple: Coefficients (theta), predictions on training data (ytr), predictions on test data (yts).  
    """  
    # Number of training examples  
    m = X_train.shape[0]  
    # Number of features  
    n = X_train.shape[1]  

    # Add bias term (column of ones) to the training data  
    X_train_bias = np.hstack((np.ones((m, 1)), X_train))  

    # Compute the Ridge Regression coefficients  
    # theta = (X'X + lambda*I) \ X'y  
    # where I is the identity matrix of size (n+1) to match X'X  
    I = np.eye(n + 1)  
    I[0, 0] = 0  # Do not regularize the bias term  
    A = X_train_bias.T @ X_train_bias + lambda_ * I  
    b = X_train_bias.T @ y_train  
    theta = np.linalg.solve(A, b)  # Use np.linalg.solve to solve the linear system  

    # Add bias term to the test data  
    X_test_bias = np.hstack((np.ones((X_test.shape[0], 1)), X_test))  

    # Make predictions on the test data  
    yts = X_test_bias @ theta  
    ytr = X_train_bias @ theta  

    return theta, ytr, yts


