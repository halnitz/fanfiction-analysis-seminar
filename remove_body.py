import sys
import csv

max_int_size = sys.maxsize

while True:
    try:
        csv.field_size_limit(max_int_size)
        break
    except OverflowError:
        max_int_size = int(max_int_size/10)

with open("1001.csv","rt") as source:
    rdr = csv.reader(source)
    with open("1002.csv","wt") as result:
        wtr = csv.writer(result)        
        for r in rdr:
            if len(r) > 0:
                wtr.writerow((r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17]))