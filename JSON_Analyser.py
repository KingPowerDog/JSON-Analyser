# This python script reads a source json file and applies rules to be able to generate a basic analysis to CSV format
# Requres 2 other files:
#    rules.json: contains the rules for analysis
#    output.cfg: defines the CSV format, such as separator and marker value

import json
import csv
import os
import array as arr
from configparser import ConfigParser

def import_rules(rule_filename):

    #imports the rules to a JSON object so we don't keep the file open
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    rf = open(current_dir + "/" + rule_filename)
    ruledata = json.load(rf)
    rf.close()
    
    return ruledata

def import_cfg(cfg_filename):
    
    #imports the config variables
    global csv_separator 
    global csv_marker
    global sourcefile
    global csv_dataattrib
    global csv_targetfile
    
    current_dir = os.path.dirname(os.path.realpath(__file__))

    configdata = ConfigParser()
    configdata.read(current_dir + "/" + cfg_filename)

    
    csv_separator = configdata.get("csv_output","separator") 
    csv_marker = configdata.get("csv_output","marker")
    sourcefile = configdata.get("csv_output","sourcefile")
    csv_dataattrib = configdata.get("csv_output","data_attribute")
    csv_targetfile = configdata.get("csv_output","targetfile")

    return 0

#Step 1 - import all the rules and config
rules = import_rules("rules.json")
config_success = import_cfg("output.cfg")

#Step 2 - open the source file
sf = open(sourcefile)
source_data = json.load(sf)

#Step 3 - create the header line
headingLine = csv_dataattrib 
for rule in rules['rules']:
    headingLine += csv_separator + rule["name"] 

#Step 4 - create the target file or clear the file if it exists
tgtfile = open(csv_targetfile, 'w')
tgtfile.write(headingLine + "\n")

#Step 5 - generate the report
for entry in source_data[csv_dataattrib]:

    current_entry = source_data[csv_dataattrib][entry]

    current_csv_line = entry

    for rule in rules['rules']:

        #the expected attributes for each rule are name:attribute:operator:value
        attrib = rule["attribute"]

        if rule["operator"] == "equals" :
            if attrib in current_entry:
                if current_entry[attrib] == rule["value"]:
                    current_csv_line += csv_separator + csv_marker 
                else:
                    current_csv_line += csv_separator + ""
            else:
                current_csv_line +=  csv_separator + "" 
        if rule["operator"] == "return":
            if attrib in current_entry:
                current_csv_line +=  csv_separator + str(current_entry[attrib])
            else:
                current_csv_line +=  csv_separator + ""
        if rule["operator"] == "contains":
            if attrib in current_entry:
                if rule["value"] in current_entry[attrib]:
                    current_csv_line += csv_separator + csv_marker
                else:
                    current_csv_line +=  csv_separator + ""
            else:
                current_csv_line +=  csv_separator + ""
        if rule["operator"] == "notContains":
            if attrib in current_entry:
                if rule["value"] not in current_entry[attrib]:
                    current_csv_line += csv_separator + csv_marker
                else:
                    current_csv_line +=  csv_separator + ""
            else:
                current_csv_line +=  csv_separator + ""

    tgtfile.write(current_csv_line + "\n")

tgtfile.close()