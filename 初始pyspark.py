

import os
from tarfile import data_filter
from pyspark import SparkConf, SparkContext



os.environ['PYSPARK_PYTHON'] = "C:/Users/Administrator/Desktop/python_project/.venv/Scripts/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.textFile("D:/计算字母数量.txt")
rdd_tuple = rdd.flatMap(lambda x: x.split(" "))
rdd_key = rdd_tuple.map(lambda x: (x, 1))
rdd_data = rdd_key.reduceByKey(lambda a, b: a + b)
rdd_sort = rdd_data.sortBy(lambda x:x[1], ascending=True, numPartitions=1)
print(rdd_sort.collect())

sc.stop()