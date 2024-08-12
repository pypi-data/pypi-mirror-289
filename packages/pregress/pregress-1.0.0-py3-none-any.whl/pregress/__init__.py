"""
PRegress Package
================

A package for Python Regression analysis and data visualization.

Modules
-------
modeling
    Functions for model fitting and prediction.
plots
    Functions for various types of plots.

Functions
---------
Modeling functions:
- add_explicit_variable
- apply_transformation
- boxCox
- bpTest
- BSR
- EvalEnvironment
- extract_variable
- fit
- format_summary
- handle_included_vars
- parse_formula
- predict
- print_anova_and_summary
- print_anova_table
- print_r_summary
- print_stata_summary
- shapiroTest
- significance_code
- step
- summary
- vif
- xysplit

Plotting functions:
- barplot
- boxplot
- customLine
- hist
- hists
- plotCor
- plotCook
- plotQQ
- plotR
- plotRH
- plots
- plotXY
"""

# Import modeling functions
from .modeling import (
    add_explicit_variable, apply_transformation, boxCox, bpTest, BSR, EvalEnvironment, extract_variable, fit,
    format_summary, handle_included_vars, intervals, parse_formula, predict,
    print_anova_and_summary, print_anova_table, print_r_summary, print_stata_summary, shapiroTest,
    significance_code, step, summary, vif, xysplit
)

# Import plotting functions
from .plots import (
    barplot, boxplot, customLine, hist, hists, plotCor, plotCook, plotQQ, plotR, plotRH, plots, plotXY
)

from .plots.plots import plots

from .utils import get_data

__all__ = [
    # Modeling functions
    'add_explicit_variable', 'apply_transformation', 'boxCox', 'bpTest', 'BSR', 'EvalEnvironment', 'extract_variable', 'fit',
    'format_summary', 'handle_included_vars', 'intervals', 'parse_formula', 'predict',
    'print_anova_and_summary', 'print_anova_table', 'print_r_summary', 'print_stata_summary', 'shapiroTest',
    'significance_code', 'step', 'summary', 'vif', 'xysplit',
    
    # Plotting functions
    'barplot','boxplot', 'customLine', 'hist', 'hists', 'plotCor', 'plotCook', 'plotQQ', 'plotR', 
    'plotRH', 'plots', 'plotXY',
    
    # Utility functions
    'get_data'
]
