'''
Hypothesis test: are they slowing down?

Now we will test the null hypothesis that the swimmer's split time is not at all correlated with the distance they are at in the swim. We will use the Pearson correlation coefficient (computed using dcst.pearson_r()) as the test statistic.
'''

import numpy as np
import dc_stat_think as dcst

# Original datasets

split_number = np.array([ 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

splits = np.array([
       [35.04, 36.39, 35.92, 36.23, 36.67, 36.76, 36.48, 36.85, 36.92, 36.68, 36.97, 36.98],
       [34.14, 34.22, 33.67, 33.88, 34.15, 33.91, 34.41, 33.92, 34.36, 34.38, 34.60, 34.45],
       [31.80, 31.91, 31.95, 32.04, 31.95, 31.65, 31.57, 31.39, 31.61, 31.43, 31.46, 31.47],
       [33.16, 32.90, 32.68, 32.84, 33.55, 33.74, 33.71, 33.60, 33.71, 33.12, 33.14, 32.79],
       [32.97, 32.83, 32.99, 32.94, 33.19, 33.60, 33.72, 33.74, 33.82, 33.67, 33.86, 33.59],
       [34.60, 34.57, 34.62, 34.96, 35.10, 35.22, 35.63, 35.56, 35.43, 35.67, 35.26, 35.42],
       [32.18, 32.17, 32.15, 32.16, 32.31, 32.27, 32.32, 32.23, 32.42, 32.34, 32.32, 32.27],
       [32.40, 32.14, 32.46, 32.43, 32.58, 32.46, 32.60, 32.42, 32.79, 32.33, 32.47, 32.63],
       [32.67, 32.54, 32.48, 32.42, 32.55, 32.45, 32.94, 33.03, 33.12, 33.47, 33.42, 33.48],
       [33.76, 34.95, 34.76, 35.45, 34.99, 36.11, 35.27, 35.82, 35.48, 36.12, 35.20, 36.07],
       [32.57, 32.70, 32.53, 32.73, 32.84, 32.70, 32.75, 33.07, 33.01, 33.11, 33.17, 33.02],
       [35.04, 34.69, 34.24, 34.07, 34.47, 34.39, 34.98, 34.56, 35.30, 34.90, 35.03, 34.08],
       [32.61, 32.97, 33.09, 33.19, 33.72, 33.92, 34.12, 33.82, 34.07, 34.22, 34.26, 34.07],
       [31.01, 31.49, 31.38, 31.47, 31.58, 31.56, 31.68, 31.68, 32.09, 31.83, 32.25, 31.67],
       [32.29, 32.36, 32.43, 32.56, 32.84, 32.73, 32.77, 32.78, 32.91, 33.15, 33.19, 33.32],
       [31.92, 32.14, 31.87, 32.02, 31.84, 32.47, 32.17, 32.73, 32.45, 33.16, 33.01, 33.08],
       [32.10, 32.47, 32.32, 32.84, 32.38, 32.93, 32.36, 32.96, 32.72, 33.35, 32.95, 33.77],
       [35.97, 35.96, 36.09, 36.00, 36.59, 36.55, 36.40, 36.58, 36.89, 36.69, 36.81, 36.73],
       [31.69, 31.56, 31.76, 31.43, 31.69, 31.77, 31.88, 31.66, 31.96, 31.87, 31.66, 31.73],
       [31.71, 32.23, 31.89, 32.31, 32.01, 32.62, 32.12, 33.00, 32.63, 33.14, 32.55, 33.39],
       [31.99, 31.94, 31.82, 32.02, 31.71, 32.00, 31.79, 31.87, 31.97, 32.15, 32.09, 32.30],
       [31.88, 31.78, 31.67, 31.68, 31.97, 31.70, 31.71, 31.87, 31.91, 32.00, 31.83, 32.13],
       [32.49, 32.32, 32.77, 32.80, 32.87, 32.85, 32.89, 33.00, 33.12, 32.86, 33.05, 32.75],
       [31.99, 31.93, 31.76, 31.85, 31.95, 31.82, 31.64, 31.49, 31.78, 31.67, 32.28, 31.85],
       [32.19, 32.32, 32.55, 32.74, 32.59, 32.94, 32.75, 33.09, 32.91, 33.53, 33.06, 33.00],
       [32.37, 32.62, 32.38, 33.07, 32.91, 33.45, 32.97, 33.38, 33.24, 33.33, 32.93, 32.53],
       [32.80, 33.38, 33.18, 33.78, 33.78, 34.32, 34.10, 34.88, 33.97, 34.96, 34.44, 34.93],
       [34.90, 35.03, 35.25, 35.42, 35.88, 35.63, 35.63, 35.66, 35.45, 35.66, 35.39, 35.34],
       [32.67, 32.30, 32.40, 32.48, 32.52, 32.59, 32.73, 32.67, 32.97, 32.70, 32.87, 32.82],
       [32.68, 33.02, 32.80, 32.94, 33.28, 33.46, 33.20, 33.42, 33.14, 33.36, 33.38, 33.31],
       [33.96, 33.93, 33.62, 33.76, 33.31, 33.70, 33.02, 33.66, 33.57, 33.37, 33.91, 33.92],
       [32.36, 32.60, 32.12, 32.67, 32.56, 32.91, 32.84, 33.17, 32.95, 33.44, 33.25, 33.59],
       [31.69, 31.81, 31.99, 31.99, 32.01, 31.77, 31.67, 31.62, 31.66, 31.82, 31.63, 31.72],
       [36.95, 37.44, 36.96, 37.12, 37.51, 37.07, 37.49, 36.66, 36.84, 37.11, 37.55, 37.60],
       [32.61, 32.92, 32.74, 32.88, 33.16, 33.21, 33.20, 33.13, 33.04, 33.09, 33.31, 33.45],
       [31.01, 31.50, 31.29, 31.59, 31.77, 31.67, 31.79, 31.94, 32.00, 31.98, 32.10, 32.03],
       [33.66, 33.92, 33.99, 34.21, 33.99, 34.16, 34.22, 34.44, 34.11, 34.37, 34.43, 34.33],
       [32.91, 33.59, 33.56, 33.96, 34.83, 34.98, 35.43, 35.09, 35.94, 35.99, 36.16, 35.74],
       [33.23, 34.10, 33.87, 34.28, 34.23, 34.37, 34.19, 34.38, 34.23, 34.48, 34.34, 34.40],
       [32.34, 32.30, 32.13, 32.40, 32.74, 32.57, 32.81, 32.92, 32.89, 32.92, 33.01, 32.73],
       [30.77, 31.10, 31.20, 31.36, 31.31, 31.44, 31.31, 31.70, 31.75, 31.64, 31.86, 31.97],
       [31.90, 31.98, 32.04, 31.98, 31.97, 31.83, 32.04, 31.92, 32.02, 31.96, 32.07, 31.99],
       [32.39, 32.13, 32.24, 32.28, 32.17, 32.22, 32.10, 32.25, 32.40, 32.55, 32.64, 32.48]])

# Compute the mean split times
mean_splits = np.mean(splits, axis=0)

'''
INSTRUCTIONS

*   Compute the observed Pearson correlation, storing it as rho.
*   Using np.empty(), initialize the array of 10,000 permutation replicates of the Pearson correlation, naming it perm_reps_rho.
*   Write a for loop to:
    *   Scramble the split number array using np.random.permutation(), naming it scrambled_split_number.
    *   Compute the Pearson correlation coefficient between the scrambled split number array and the mean split times and store it in perm_reps_rho.
*   Compute the p-value and display it on the screen. Take "at least as extreme as" to mean that the Pearson correlation is at least as big as was observed.
'''

# Observed correlation
rho = dcst.pearson_r(split_number, mean_splits)

# Initialize permutation reps
perm_reps_rho = np.empty(10000)

# Make permutation reps
for i in range(10000):
    # Scramble the split number array
    scrambled_split_number = np.random.permutation(split_number)
    
    # Compute the Pearson correlation coefficient
    perm_reps_rho[i] = dcst.pearson_r(scrambled_split_number, mean_splits)
    
# Compute and print p-value
p_val = np.sum(perm_reps_rho >= rho) / len(perm_reps_rho)
print('p =', p_val)