# from pyspark import SparkConf, SparkContext
# import collections

# conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
# sc = SparkContext(conf = conf)

# lines = sc.textFile("file:///SparkCourse/movielens/data/u.data")
# ratings = lines.map(lambda x: x.split()[2])
# result = ratings.countByValue()

# sortedResults = collections.OrderedDict(sorted(result.items()))
# for key, value in sortedResults.items():
#     print("%s %i" % (key, value))


import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

print("Kaviyarasu 😎")

#Bala's 1st commit
print("Bala")
