# Hudau (magic in Welsh)
Hudau is a package for useful functions in Python for the YJB Statistics and Analysis Team

## Installation
To install this package run the following command:

    pip install git+https://github.com/YJB-Statistics-Analysis/hudau.git
    

## Usage examples

**datacleaning.standardise_cms_yjs** : For standardising YJS names in Redshift:

    # Example where df_cms is a dataset from Redshift and 'yot_name' is the column containing the names to standardise
    from hudau import standardise_cms_yjs
    df_clean = standardise_cms_yjs(df_cms, 'yot_name') 
    
**datacleaning.check_non_matching_names** : For changing non matching names against the standardised form for YJS names:

    # Example where df_cms is a dataset from Redshift and 'yot_name' is the column containing 
    # the names to check for non matches
    from hudau import check_non_matching_names
    check_non_matching_names(df_cms, 'yot_name') 
