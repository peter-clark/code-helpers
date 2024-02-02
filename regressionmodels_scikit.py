import sklearn
import numpy as np

# MULTI OUTPUT REGRESSION EXAMPLES

# Create test dataset
# 1000 examples:
# Input: 10 features (5 informative)
# Output: 2 variables
# (10)->(2)

# Create dataset
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, n_targets=2, random_state=1, noise=0.5)
print(X.shape, y.shape)

# Random 10 feature input for all test cases.
row = [0.21947749, 0.32948997, 0.81560036, 0.440956, -0.0606303, -0.29257894, -0.2820059, -0.00290545, 0.96402263, 0.04992249]

# Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
y_lin = model.predict([row])
print(y_lin[0])

# k-Nearest Neighbor Regression
from sklearn.neighbors import KNeighborsRegressor
model2 = KNeighborsRegressor()
model2.fit(X,y)
y_kNN = model2.predict([row])
print(y_kNN[0])

# Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor
model3 = DecisionTreeRegressor()
model3.fit(X,y)
y_dt = model3.predict([row])
print(y_dt[0])

# MultiOutputRegressor Wrapper for other regression types. (LinearSVM)
from sklearn.svm import LinearSVR
from sklearn.multioutput import MultiOutputRegressor
model4 = LinearSVR()
model4_wrapper = MultiOutputRegressor(model4) # test on the wrapper, not the model
model4_wrapper.fit(X,y)
y_svm = model4_wrapper.predict([row])
print(y_svm[0])

#--------------------------------------------------------#
# Evaluation of models
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
#   Define procedure
cross_validation = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1) # 10-fold
#   Evaluate
n_scores = np.abs(cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cross_validation,n_jobs=-1)) # mean abs error as metric
n_scores2 = np.abs(cross_val_score(model2, X, y, scoring='neg_mean_absolute_error', cv=cross_validation,n_jobs=-1))
n_scores3 = np.abs(cross_val_score(model3, X, y, scoring='neg_mean_absolute_error', cv=cross_validation,n_jobs=-1))
n_scores4 = np.abs(cross_val_score(model4_wrapper, X, y, scoring='neg_mean_absolute_error', cv=cross_validation,n_jobs=-1))

print("Mean Abs Error[Linear]: %.3f (%.3f)" % (np.mean(n_scores), np.std(n_scores)))
print("Mean Abs Error[kNN]: %.3f (%.3f)" % (np.mean(n_scores2), np.std(n_scores2)))
print("Mean Abs Error[DecisionTree]: %.3f (%.3f)" % (np.mean(n_scores3), np.std(n_scores3)))
print("Mean Abs Error[SVR]: %.3f (%.3f)" % (np.mean(n_scores4), np.std(n_scores4)))



