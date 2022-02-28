import csv
import statistics
import numpy

with open('std_deviation.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = list(map(int, *data))
deviation = numpy.std(data)
print(deviation)

