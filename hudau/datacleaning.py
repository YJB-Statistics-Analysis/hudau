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

def get_list_unique_labels(df, col_name):
    """
    Takes a DataFrame object and the column name and gets the unique values and returns a list.
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
    col_name: str

    Returns
    -------
    Prints a message confirming there are not any non-matches or prints the values that do not match.
    """
    unique_labels = list(df[col_name].unique())
    return unique_labels

def check_non_matching_values(list_values1, list_values2):
    """
    Takes two lists and searches for non-matching values in the two lists.
    
    Parameters
    ----------
    list_values1: list
    list_values2: list

    Returns
    -------
    Prints a message confirming there are not any non-matches or prints the values that do not match.
    """

    list_values1_not_list_values2 = set(list_values1) -set(list_values2)
    list_values2_not_list_values1 = set(list_values2) -set(list_values1)
    if len(list_values1_not_list_values2) == 0:
        print (f"All values in the list List 1 match the values in List 2")
    else: print(f" The following values do not match {list_values1_not_list_values2}")

    if len(list_values2_not_list_values1) == 0:
        print (f"All values in the list List 2 match the values in List 1")
    else: print(f" The following values do not match {list_values2_not_list_values1}")


