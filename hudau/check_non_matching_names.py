import pandas as pd


def check_non_matching_names(df_cms, yjs_col):
    """
    Takes a DataFrame object with the naming convention used in Redshift and checks 
    for non-matching names against the Standardised form.
    

    Parameters
    ----------
    df_cms: pandas.core.frame.DataFrame
        A dataframe containing the naming convention used in Redshift.
    yjs_col: str
        The name of the date column containing the names of the YJSs.

     
    Returns
    -------
    A set with the non-matching names if there are or a message confirming there are no non-matches. 
    """   

    yot_names = pd.read_csv('data/raw/YJS_names_standardised.csv')
    values_yjs_standardised = list(yot_names['yjs_name'].unique())
    values_yots_cms = list(df_cms[yjs_col].unique())
    in_cms_not_yjs = set(values_yots_cms) -set(values_yjs_standardised)
    if len(in_cms_not_yjs) == 0:
        print (f"'All names in the column {yjs_col} match the standardised naming")
    else:
        print(f" The following names do not match the standard form {in_cms_not_yjs}")
