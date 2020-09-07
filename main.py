from spline import Spline
from scipy import *
from matplotlib.pyplot import *
import numpy
import csv

def read_Data(filename):
    d_s = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
               line_count +=1
            else:
                #[x = float(x) for x in row]
                for i in range(len(row)):
                    row[i] = float(row[i])
                d_s.append(tuple(row))
                line_count +=1
    return d_s

ds = read_Data('Data.csv')
print(ds)
#us = numpy.linspace(0,1,5)
#s = Spline(ds,us)

#Något som läser in d:na från fil (tar in filnamn som string och returnerar en lista med tuples)
#Instansierar splinen med listan med tuples
#kallar på plotfunktionen
#Seamus