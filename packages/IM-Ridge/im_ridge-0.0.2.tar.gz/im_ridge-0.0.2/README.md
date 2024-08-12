# Ridge Model
## Features  

- **Comprehensive Metrics:**  This model can be used for Regression.  

## Installation  

Install the package using pip:  

```bash  
pip install IM_Ridge

#Import Necessary Functions:

from IM_Metrics import Save_Metrics
from IM_Ridge import Ridge
import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from IM_Metrics import Save_Metrics

df = pd.read_excel('KR-F-10Lags-t3.xlsx')
n,m=df.shape
X=df.iloc[:,0:(m-1)]
y=df.iloc[:,(m-1)]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=None,shuffle=False)

C_Ridge = 0.1
theta, y_train_pred, y_test_pred = Ridge(X_train, y_train, X_test, C_Ridge)  

metrics_filename = 'Results of Ridge.xlsx'
Save_Metrics(y_train, y_train_pred, y_test, y_test_pred,metrics_filename)


