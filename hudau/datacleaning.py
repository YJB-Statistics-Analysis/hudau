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

    # Example where df_cms is a dataset from Redshift and 'yot_name' 
    # is the column containing the names to standardise
    # from hudau.datacleaning import standardise_cms_yjs
    #  df_clean = standardise_cms_yjs(df_cms, 'yot_name') 

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

    # Example where df_cms is a dataset from Redshift and 'yot_name' is the column containing 
    # the labels
    # from hudau.datacleaning import get_list_unique_labels
    # check_non_matching_names(df_cms, 'yot_name') 


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

    # Example where 'yot_names' is the list with unique names from a Redshift dataset and 
    # 'yjs_names' is a list with the standardised names 
    # from hudau.datacleaning import check_non_matching_values
    # check_non_matching_names(yot_names, 'yjs_names') 


def convert_quarter(quarter_end):
    """
    Convert a quarter end date string to yyyy-mm-dd format.

    Parameters:
    quarter_end (str): A string representing the quarter end date in the format 'mmm-yy', where 'mmm'
                       is a three-letter abbreviation for the month (e.g., 'Mar') and 'yy' is the last
                       two digits of the year.

    Returns:
    str: A string representing the corresponding date in 'yyyy-mm-dd' format, where 'yyyy' is the year
         of the quarter end and 'mm-dd' represents the last day of the quarter.

         If the input quarter end date string is not recognized, the function returns 'error'.
    """
    quarter_dict = {'Mar': '-03-31', 'Jun': '-06-30', 'Sep': '-09-30', 'Dec': '-12-31'}
    
    if quarter_end[:3] in quarter_dict:
        return '20' + quarter_end[-2:] + quarter_dict[quarter_end[:3]]
    else:
        return 'error'
    
def convert_month(month_abbr):
    """
    Convert a three-letter abbreviation of a month to a numeric value.

    Parameters:
    month_abbr (str): A string representing the three-letter abbreviation of a month (e.g., 'Jan', 'Feb', etc.).

    Returns:
    int or str: If the input abbreviation is recognized, returns an integer representing the corresponding month (1 for
               January, 2 for February, etc.). If the input abbreviation is not recognized, returns the string 'error'.
    """
    month_dict = {'Apr': '04', 'Jul': '07', 'Oct': '10', 'Jan': '01'}
    
    if month_abbr in month_dict:
        return month_dict[month_abbr]
    else:
        return 'error'

