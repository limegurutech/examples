import numpy
from scipy import stats

data = [10, 10, 20, 10, 50]    

mean = numpy.mean(data)
print("MEAN: "+str(mean))

median = numpy.median(data)
print("MEDIAN: "+str(median))

mode = stats.mode(data)
print("MODE: "+str(mode))