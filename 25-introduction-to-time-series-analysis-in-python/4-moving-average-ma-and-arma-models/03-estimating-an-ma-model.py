'''
Estimating an MA Model

You will estimate the MA(1) parameter, <theta>, of one of the simulated series that you generated in the earlier exercise. Since the parameters are known for a simulated series, it is a good way to understand the estimation routines before applying it to real data.

For simulated_data_1 with a true <theta> of -0.9, you will print out the estimate of <theta>. In addition, you will also print out the entire output that is produced when you fit a time series, so you can get an idea of what other tests and summary statistics are available in statsmodels.
'''

import numpy as np

from statsmodels.tsa.arima_process import ArmaProcess

ar1 = np.array([1])
ma1 = np.array([1, -0.9])
MA_object1 = ArmaProcess(ar1, ma1)
simulated_data_1 = MA_object1.generate_sample(nsample=1000)

'''
INSTRUCTIONS

*   Import the class ARMA in the module statsmodels.tsa.arima_model.
*   Create an instance of the ARMA class called mod using the simulated data simulated_data_1 and the order (p,q) of the model (in this case, for an MA(1)), is order=(0,1).
*   Fit the model mod using the method .fit() and save it in a results object called res.
*   Print out the entire summmary of results using the .summary() method.
*   Just print out an estimate of the constant and phi parameter using the .params attribute (no arguments).
'''

# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Fit an MA(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for theta
print("When the true theta=-0.9, the estimate of theta (and the consant) are:")
print(res.params)