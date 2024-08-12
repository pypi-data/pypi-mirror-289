import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import norm
from .extract_variable import extract_variable
from .apply_transformation import apply_transformation

def intervals(model, newX, interval='confidence', observation=None, level=0.95, xlab=None, ylab=None, main=None, plot=False, subplot=None):
    """
    Calculate and optionally plot confidence or prediction intervals for a statsmodels object.

    Parameters:
    model : statsmodels object
        The fitted statsmodels model.
    newX : DataFrame
        DataFrame of predictor variables.
    interval : str
        Type of interval to calculate, either 'confidence' or 'prediction'.
    observation : int, optional
        Observation number to plot the PDF for multiple predictors. Required if newX has multiple predictors.
    level : float
        The confidence level for the intervals. Default is 0.95.
    xlab : str, optional
        Label for the x-axis.
    ylab : str, optional
        Label for the y-axis.
    main : str, optional
        Title for the plot.
    plot : bool, optional
        Whether to plot the relationship. Default is False.

    Returns:
    intervals : DataFrame
        DataFrame with lower bound, prediction, and upper bound.
    """
    # Ensure newX is a DataFrame
    if not isinstance(newX, pd.DataFrame):
        newX = pd.DataFrame(newX)

    model_params = model.params.index
    intercept_name = None
    for term in model_params:
        if term.lower() in ['const', 'intercept']:
            intercept_name = term
            break

    if intercept_name and intercept_name not in newX.columns:
        newX.insert(0, intercept_name, 1)

    # Extract the names of the model's predictor variables
    model_columns = model.model.exog_names
    transformations = {}
    for col in model_columns:
        if col != 'Intercept':
            transformations[col] = extract_variable(col)

    # Initialize a new DataFrame to hold transformed values
    transformed_X = pd.DataFrame(index=newX.index)

    # Apply the extracted transformations to newX and handle interaction terms
    for col, info in transformations.items():
        transform_type, variable = info
        if transform_type == 'interaction':
            variables = variable.split(':')
            interaction_term = newX[variables[0]]
            for var in variables[1:]:
                interaction_term *= newX[var]
            transformed_X[col] = interaction_term
        else:
            transformed_X[col] = apply_transformation(newX[variable], transform_type)

    # Add a constant column for the intercept to transformed_X if the model includes an intercept
    if 'Intercept' in model_columns:
        transformed_X['Intercept'] = 1
    if 'const' in model_columns:
        transformed_X['const'] = 1

    # Ensure transformed_X contains all required columns for prediction and raise an error if any are missing
    missing_cols = set(model_columns) - set(transformed_X.columns)
    if missing_cols:
        raise ValueError(f"The following required columns are missing from transformed_X: {missing_cols}")

    # Ensure columns are in the correct order
    transformed_X = transformed_X[model_columns]

    if interval not in ['confidence', 'prediction']:
        raise ValueError("Interval must be 'confidence' or 'prediction'")

    preds = model.get_prediction(transformed_X)
    alpha = 1 - level
    summary_frame = preds.summary_frame(alpha=alpha)

    if interval == 'confidence':
        lower_bound = summary_frame['mean_ci_lower']
        upper_bound = summary_frame['mean_ci_upper']
    elif interval == 'prediction':
        lower_bound = summary_frame['obs_ci_lower']
        upper_bound = summary_frame['obs_ci_upper']

    prediction = summary_frame['mean']

    intervals = pd.DataFrame({
        'Lower Bound': lower_bound,
        'Prediction': prediction,
        'Upper Bound': upper_bound
    })

    if plot:
        # Determine the number of predictor variables (excluding any constant column)
        non_constant_cols = [col for col in newX.columns if not np.all(newX[col] == 1)]
        num_predictors = len(non_constant_cols)

        if num_predictors == 1:
            # Plot response vs predictor
            predictor = newX[non_constant_cols[0]]
            xlab = xlab if xlab else non_constant_cols[0]
            ylab = ylab if ylab else 'Response'
            main = main if main else f'Regression Line with {int(level*100)}% {interval.capitalize()} Interval'
            plt.figure(figsize=(10, 6))
            plt.plot(predictor, model.predict(transformed_X), label='Regression Line', color='blue')
            plt.fill_between(predictor, lower_bound, upper_bound, color='gray', alpha=0.2)
            plt.plot(predictor, lower_bound, 'r--', label=f'{int(level*100)}% {interval.capitalize()} Interval')
            plt.plot(predictor, upper_bound, 'r--')
            plt.title(main)
            plt.xlabel(xlab)
            plt.ylabel(ylab)
            # Dynamically determine legend position
            legend_loc = 'upper right' if model.predict(transformed_X).mean() > np.median(model.predict(transformed_X)) else 'upper left'
            plt.legend(loc=legend_loc)
            plt.grid(True)
            
        else:
            if observation is None:
                raise ValueError("An observation number must be specified for multiple predictors")

            # Plot the PDF of the response with bounds for the specified observation
            xlab = xlab if xlab else 'Response'
            main = main if main else f'{int(level*100)}% {interval.capitalize()} Interval for Observation {observation+1}'
            plt.figure(figsize=(10, 6))
            mu, std = prediction[observation], (upper_bound[observation] - lower_bound[observation]) / 4  # Approximation
            x = np.linspace(mu - 3*std, mu + 3*std, 100)
            pdf = norm.pdf(x, mu, std)
            plt.plot(x, pdf, label='Density', color='blue')
            plt.axvline(mu, color='blue', linestyle='--', label='Prediction')
            plt.axvline(lower_bound[observation], color='red', linestyle='--', label=f'{int(level*100)}% {interval.capitalize()} Interval')
            plt.axvline(upper_bound[observation], color='red', linestyle='--')
            plt.fill_between(x, pdf, color='gray', alpha=0.2)
            plt.title(main)
            plt.xlabel(xlab)
            plt.ylabel('Density')
            plt.legend(loc='upper right')
            plt.grid(True)
            
            
        # Show the plot if subplot is not specified
        if subplot is None:
            plt.show()
            plt.clf()
            plt.close()
            
    return intervals
