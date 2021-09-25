import csv
import operator

with open("students.csv") as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        sortedlist = sorted(reader, key=operator.itemgetter(2), reverse=True)
        print(sortedlist[:5])
