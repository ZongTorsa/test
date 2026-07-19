import os
from pyspark import SparkContext, SparkConf

os.environ['PYSPARK_PYTHON'] = "C:/Users/Administrator/Desktop/python_project/.venv/Scripts/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

data_dict = {}
data_read = sc.textFile("D:/search_log.txt")
data_list = data_read.map(lambda x: x.split("\t"))



data_hot = data_list.map(lambda x: (x[0][:2], 1))\
                    .reduceByKey(lambda a,b:a+b)\
                    .sortBy(lambda x:x[1], ascending=False)\
                    .take(3)
print(f"热门第一时间段是{data_hot[0][0]}点,第二是{data_hot[1][0]}点,第三是是{data_hot[2][0]}点")



data_name = data_list.map(lambda x: (x[2], 1))\
                     .reduceByKey(lambda a,b:a+b)\
                     .sortBy(lambda x:x[1], ascending=False)\
                     .take(3)
print(f"名字排名是{data_name[0][0]},第二是{data_name[1][0]},第三是{data_name[2][0]}")



hot_name = data_list.filter(lambda x:x[2]=="黑马程序员")\
                    .map(lambda x: (x[0][:2], 1))\
                    .reduceByKey(lambda x,y:x+y)\
                    .sortBy(lambda x:x[1], ascending=False)\
                    .take(1)

print(f"黑马程序员被搜索次数最多时间段是{hot_name[0][0]}点")


sc.stop()
                    
                
