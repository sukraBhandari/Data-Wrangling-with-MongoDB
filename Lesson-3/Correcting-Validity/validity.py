"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'
def convertYear(date):
    if date != 'NULL':
        d = int( date[0:4]) 
        if d > 1885 and d < 2014:
            return d
        else:
            return None
    return None
def process_file(input_file, output_good, output_bad):
    goodData = []
    badData = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        #print header
        count = 0
        for each in reader:
            if count > 2:
                #print each
                uri = each['URI']
                productionYear = convertYear(each['productionStartYear']) 
                #print productionYear
                if productionYear is not None:
                    each['productionStartYear'] = productionYear
                    goodData.append(each)
                else:
                    badData.append(each)                
            else:
                count += 1
            

        #COMPLETE THIS FUNCTION
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in goodData:
            writer.writerow(row)
    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in badData:
            writer.writerow(row)

    '''
        
    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in YOURDATA:
            writer.writerow(row)
    '''

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)
    
    


if __name__ == "__main__":
    test()
