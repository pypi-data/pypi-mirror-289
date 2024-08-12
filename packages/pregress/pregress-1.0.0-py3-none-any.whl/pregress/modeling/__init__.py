"""
Modeling
===============

This subpackage provides functions for model fitting, prediction, and regression analysis.

Functions
---------
add_explicit_variable
    Add explicit variable to the model.
apply_transformation
    Apply transformation to the data.
BSR
    Perform Best Subsets Regression.
EvalEnvironment
    Evaluation environment for the model.
extract_variable
    Extract variable from the data.
fit
    Fit the model to the data.
format_summary
    Format the summary of the model.
handle_included_vars
    Handle included variables in the model.
handle_included_vars2
    Handle additional included variables in the model.
parse_formula
    Parse the formula for the model.
predict
    Predict using the fitted model.
print_anova_and_summary
    Print ANOVA and summary of the model.
print_anova_table
    Print ANOVA table.
print_r_summary
    Print R summary.
print_stata_summary
    Print Stata summary.
significance_code
    Get significance code.
step
    Perform stepwise, backward elimination, forward selection.
summary
    Get summary of the model.
"""

from .add_explicit_variable import add_explicit_variable
from .apply_transformation import apply_transformation
from .boxCox import boxCox
from .bpTest import bpTest
from .BSR import BSR
from .environment import EvalEnvironment
from .extract_variable import extract_variable
from .fit import fit
from .format_summary import format_summary
from .handle_included_vars import handle_included_vars
from .intervals import intervals
from .parse_formula import parse_formula
from .predict import predict
from .print_anova_and_summary import print_anova_and_summary
from .print_anova_table import print_anova_table
from .print_r_summary import print_r_summary
from .print_stata_summary import print_stata_summary
from .shapiroTest import shapiroTest
from .significance_code import significance_code
from .step import step
from .summary import summary
from .vif import vif
from .xysplit import xysplit

__all__ = [
    'add_explicit_variable', 'apply_transformation', 'boxCox', 'bpTest', 'BSR', 
    'EvalEnvironment', 'extract_variable', 'fit',
    'format_summary', 'handle_included_vars', 'intervals', 'parse_formula', 'predict',
    'print_anova_and_summary', 'print_anova_table', 'print_r_summary', 'print_stata_summary',
    'shapiroTest', 'significance_code', 'step','summary', 'vif', 'xysplit'
]
