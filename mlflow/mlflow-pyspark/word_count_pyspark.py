import pyspark
import sys
sc = pyspark.SparkContext('local[*]')

filepath = str(sys.argv[1])
txt = sc.textFile(filepath)
print(txt.count())

python_lines = txt.filter(lambda line: 'limeguru' in line.lower())
limeguru_count = python_lines.count()
print("+++++++++++++++++++++++++++++++")
print("limeguru word count: "+ str(limeguru_count))
print("+++++++++++++++++++++++++++++++")
