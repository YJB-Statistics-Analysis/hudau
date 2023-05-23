import pandas as pd

def standardise_cms_yjs (df, yjs_col):
    """
    Takes a DataFrame object with the naming convention used in Redshift and substitutes the names 
    of the YJS in the standardised format, allowing joins.
    

    Parameters
    ----------
    df_cms: pandas.core.frame.DataFrame
        A dataframe containing the naming convention used in Redshift.
    yjs_col: str
        The name of the date column containing the names of the YJSs.

     
    Returns
    -------
    pandas.core.frame.DataFrame
        A pandas dataframe with the YJS names in the standardised form. 
    """
    df_cms = df.copy()
    df_cms[yjs_col]= df_cms[yjs_col].replace('Cheshire East, Cheshire West, Halton and Warrington', 'Cheshire East Cheshire West Halton and Warrington')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Cornwall', 'Cornwall and Isles of Scilly')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Dorset', 'Dorset Combined YOS')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Gwynedd & Ynys Mon', 'Gwynedd and Ynys Mon')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Kingston-upon-Hull', 'Kingston upon Hull')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Southend-on-Sea', 'Southend on Sea')
    df_cms[yjs_col]= df_cms[yjs_col].replace('St. Helens', 'St Helens')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Stockton-on-Tees', 'Stockton on Tees')
    df_cms[yjs_col]= df_cms[yjs_col].replace('Stoke-on-Trent', 'Stoke on Trent')
    df_cms = df_cms[df_cms[yjs_col].str.contains("Western Bay")!=True]
    return (df_cms)

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
