#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", 
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", 
          "areaLand", "areaMetro", "areaUrban"]

def skip_line(input_file, skip):
    for each in range(0, skip):
        next(input_file)
def checkInt(data):
    try:
        return isinstance(int(data), int)
    except:
        return False
def checkFloat(data):
    try:        
        return isinstance(float(data), float)
    except:
        return False
def getType(data):
    if data == "" or data == 'NULL':
        return type(None)
    elif data.startswith("{"):
        data = []
        return type(data)
    elif checkInt(data):
        return type(1)
    elif checkFloat(data):
        return type(1.1)
    else:
        return type(data)
def audit_file(filename, fields):
    fieldtypes = {}
    with open(filename, "r") as f:       
        reader = csv.DictReader(f)
        header = reader.fieldnames
        skip_line(f, 3)
        for each in reader:
            #print each
            for x in fields:
                dType = getType(each[x])
                if fieldtypes.has_key(x):                     
                    fieldtypes[x].add(dType)
                else:
                    fieldtypes[x] = set([dType])
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)
    #print checkFloat('1.13e+07')
    pprint.pprint(fieldtypes)
    #print set(fieldtypes["areaLand"]),set([type(1.1), type([]), type(None)])
    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
