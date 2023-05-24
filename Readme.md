# Hudau (magic in Welsh)
Hudau is a package for useful functions in Python for the YJB Statistics and Analysis Team

## Installation
To install this package run the following command:

    pip install git+https://github.com/YJB-Statistics-Analysis/hudau.git
    

## Functionality
### Examples are provided in the documentation

**datacleaning.standardise_cms_yjs** : For standardising YJS names in Redshift.

**datacleaning.get_list_unique_labels** : For getting a list of unique labels from a column in DataFrame.

**datacleaning.check_non_matching_values** : Compares two lists for non-matching values.


## How to contribute
Create a new branch and add any new function with docstrings and example of usage for the function.
Depending on the function it can be either added to the existent scripts in ```hudau``` or a new py file can be created.
Then, please update the examples.md file adding the function name and input and output examples.   
Finally, create a Pull Request to merge with the main branch.
