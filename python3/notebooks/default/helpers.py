import numpy as np
import pandas as pd
from datetime import date,datetime
from sklearn import preprocessing

# extract this to a function so that we can apply the exact same transformation
# to both train sets and test sets
def get_normalized_df_simple(df, numeric_cols, categorical_cols, test=False):
    """
    Normalize the given dataframe.
    
    Arguments:
      df: original dataframe
      numeric_cols: list of numeric column names to include
      categorical_cols: list of categorical column names to include
      test: if True, there is no target column
    
    Returns a pandas.Dataframe
    """
    
    normalized_df = pd.DataFrame()
   
    if test is False:
        # add target
        binarized_target = df["default"].map(lambda default: 0 if default == False else 1)
        normalized_df = pd.concat([normalized_df,binarized_target],axis=1)

    # numerical features
    for numeric_col_name in numeric_cols:    
        normalized_df=pd.concat([normalized_df,_normalize_numeric(df[numeric_col_name])],axis=1)
    
    # categorical features
    for categorical_col_name in categorical_cols:    
        normalized_df=pd.concat([normalized_df,_normalize_categorical(df[categorical_col_name])],axis=1)

    return normalized_df    

def convert_date_to_number_of_days_from_today(date_string, date_format='%Y-%m-%d'):
    """
    Converts a date string into an integer, referring to the number of days since that
    date and today.
    
    Returns an integer or np.nan, if there were errors in parsing the date string
    """
    today = datetime.today()
    
    try:
        datetime_object = datetime.strptime(date_string, date_format)
    except TypeError:
        return np.nan
    
    delta = today-datetime_object
    
    return delta.days


def _normalize_numeric(column, nan_strategy='mean'):
    """
    Returns a normalized version of the given numerical column (pandas Series).
    
    Arguments:
      column: pandas Series, representing the feature column
      nan_strategy: the strategy to be used to replace NaNs in the data    
        
    Returns a pandas.DataFrame
    
    Note: A full pandas Dataframe is returned, even if the output is a single column.
    """    
    
    supported_strategies = ['mean']
    
    strategy_clean = nan_strategy.lower().strip()
    
    if strategy_clean not in supported_strategies:
        raise Exception("provided strategy {0} not supported. supported values: {1}".format(
        strategy_clean,",".join(supported_strategies)))
    
    # we don't want to modify the original column
    cpy = column.copy()
    x = cpy.values
    
    if strategy_clean == 'mean':
        nan_indices = np.isnan(x)

        non_nan_indices = np.invert(nan_indices)

        mean = np.mean(x[non_nan_indices])
       
        x[nan_indices] = mean
    
    
    # we normalize the data to stop features with large absolute values from disproportionately affecting
    # the result
    sc = preprocessing.MinMaxScaler()
    x_scaled = sc.fit_transform(x.reshape(-1,1))
    out_df = pd.DataFrame(x_scaled)
    
    return out_df

# TODO add 'top' strategy
def _normalize_categorical(column, nan_strategy='nan'):
    """
    Returns a normalized version, one-hot-encoded version of the given categorical column (pandas Series).
    
    Arguments:
      column: pandas Series, representing the feature column
      nan_strategy: the strategy to be used to replace NaNs in the data    
        
    Returns a pandas.DataFrame
    
    Note: A full pandas Dataframe is returned, even if the output is a single column.
    """
    supported_strategies = ['nan']
    
    if nan_strategy.lower().strip() not in supported_strategies:
        raise Exception("provided strategy {0} not supported. supported values: {1}".format(
        nan_strategy,",".join(supported_strategies)))    
        
    # we don't want to modify the original column    
    cpy = column.copy()
    
    if nan_strategy=="nan":
        cpy[pd.isnull(cpy)]  = 'NaN'
    
    # one-hot encode
    
    ohe_df = pd.get_dummies(cpy,prefix=column.name)
    
    return ohe_df