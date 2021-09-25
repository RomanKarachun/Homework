import csv
import operator
 
with open('students.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
 
    with open('new.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, quoting=csv.QUOTE_MINIMAL)
 
        for line in csv_reader:
            line = sorted(csv_reader, key=operator.itemgetter(1), reverse=True)
            csv_writer.writerow(line)
