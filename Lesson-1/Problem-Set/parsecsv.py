# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)    
    sheet = workbook.sheet_by_index(0)    
    data = {}
    for each in range(1,sheet.ncols-1):
        station = sheet.cell_value(0,each)
        d = sheet.col_values(each, start_rowx = 1, end_rowx = None)
        maxi = max(d)        
        maxiDate = xlrd.xldate_as_tuple(sheet.cell_value(d.index(maxi) + 1, 0),0)[:-2]
        data[station] = {"maxi" : maxi, "maxiDate" : maxiDate}     
    return data

def save_file(data, filename):    
    with open(filename, "w") as q:
        w = csv.writer(q, delimiter = '|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for each in data:
            year, month, day, hour = data[each]['maxiDate']
            w.writerow([each, year, month, day, hour, data[each]['maxi']])

    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()
