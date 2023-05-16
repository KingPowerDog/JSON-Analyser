# JSON-Analyser
Simple Python Script to analyse JSON data with customised rules and create a CSV report

## Introduction
The purpose of this script is just to take a JSON file with data, apply custom rules (as defined in rules.json) and output a CSV file that can be used for some basic data analysis


## Important files
The 3 main files are as follows:

1. **JSON_Analyser.py** = the main Python script
2. **rules.json** = a JSON file that contains the custom rules for analysis
3. **output.cfg** = an ini file that contains the configuration for the output CSV file, such as the source and target filenames, the separator character, etc.

These files all need to be in the same directory on execution.


### rules.json
The expected attributes of a rule are explained below:

1. **name**: Just give a name for your rule. This will also be used for the heading of the respective column in the target CSV
2. **attribute**: The respective data attribute in the source JSON file that will be inspected
3. **operator**: What type of operation will be performed on the attribute as part of analysis. The currently supported operators are listed in the next section
4. **value**: Varies depending on the operator, but in general acts as a control value for the analysis


### Supported operator values

- **"equals"**: Checks if the "attribute" is equal to the "value" in the rule. If it is equal, mark in the report.
- **"return"**: Returns the value of "attribute" from the source JSON as is. The contents of "value" is not checked for this rule.
- **"contains"**: Checks if the "attribute" contains the string indicated in "value". If it is found, mark in the report.
- **"notContains"**: The opposite of the "contains" operator. If the value is not found, mark in the report.
- **"notContainsOrNotExists"**: Checks if the value is either not found, or the attribute itself does not exist at all
- **"containsOrNotExists"**: Checks if "value" is in "attribute", or "attribute" does not exist. Useful if the "attribute" is implicitly active if not indicated.

### test.json

A sample file called _test.json_ is included for reference as a basis for the type of JSON files I designed this for.

## TODO
- Add more operator support (I may add only based on what I need)
- Add some error handling