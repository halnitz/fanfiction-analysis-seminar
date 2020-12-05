import sys
import csv
import re

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

regex = re.compile('[^a-zA-Z]')

def readCsv():
    with open('1001.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if len(row) != 0:                    
                    if row[8] == 'English':
                        print(f'title: "{regex.sub("", row[1])}", language: "{row[8]}"')
                        with open(regex.sub('', row[1]) + '.txt', 'w+') as file:
                            print(f'creating file for title: "{row[1]}"...')
                            file.write(row[18])
                            print(f'wrote file successfuly!"')
                    else:
                        print(f'title: "{row[1]}",language is not English, language is "{row[8]}"')
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
    
readCsv()