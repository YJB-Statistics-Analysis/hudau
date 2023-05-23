# Hudau (magic in Welsh)
Hudau is a package for useful functions in Python for the YJB Statistics and Analysis Team

## Installation
To install this package run the following command:

    pip install git+https://github.com/YJB-Statistics-Analysis/hudau.git
    

## Usage  
To use the ```standardise_cms_yjs``` function:

    from hudau.datacleaning import standardise_cms_yjs

Functions implemented:

- datacleaning.standardise_cms_yjs: For standardising YJS names in Redshift

     # Example
     df_clean = standardise_cms_yjs(df_cms, 'yot_name') # where df_cms is a dataset from Redshift and 'yot_name' is the column containing the names to standardise
