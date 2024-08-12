from .parse_formula import parse_formula
import statsmodels.api as sm
import pandas as pd

def fit(formula, data=None, method = "ols", dummies = True):

    Y_name, X_names, Y_out, X_out = parse_formula(formula, data)
    
    if method.lower() == "ols":
        if dummies:
            
            X_out = pd.get_dummies(X_out, drop_first=True)
            
            # Convert binary variables (True/False) to numeric (0/1)
            binary_columns = X_out.select_dtypes(include=['bool']).columns
            X_out[binary_columns] = X_out[binary_columns].astype(int)

        if X_out.empty:
            raise ValueError("The input data is empty or the specified variables are not found in the data.")

        model = sm.OLS(Y_out, X_out).fit()

    return model
