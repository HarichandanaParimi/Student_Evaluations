#read the file countaining the tweets


text_file = sc.textFile("text.txt")
# Getting counts of each word
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# Sorting based on value
output = counts.map(lambda (k,v): (v,k)).sortByKey(False)
#Saving as counts
output.saveAsTextFile("counts")