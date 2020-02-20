import csv

#Read the dataset
input = open('Data/datawithemotions.csv', 'r')
data = input.read()
# Open the file to be written.
output = open('Data/dataset-final.csv', 'w')
writer = csv.writer(output)

#Writing the headers
writer.writerow(["finalEmotion", "anger", "trust", "fear", "sadness", "anticipation", "disgust",
        "surprise" , "joy", "positive", "negetive", "love", "people",
        "message", "instant", "get", "know", "going",
        "Term",  "Course", "Question",
        "tokens", "Comments"])

#Splitting the dataset into lines
data = data.split('\n')
statusList = []
for line in data:
    print (len(line.split('\t')))
    # Ommitting lines more than the required variables
    if (len(line.split('\t'))) == 44:
        #assigning all the variables from the dataset
        Term, Course, Question, tokens, Comments, anger, trust, fear, sadness, anticipation, disgust, \
        surprise , joy, positive, negetive, angerWordList, trustWordList,\
        fearWordList, sadnessWordList, anticipationWordList, disgustWordList, surpriseWordList, \
        angerEmoticonList, trustEmoticonList, fearEmoticonList, sadnessEmoticonList, \
        anticipationEmoticonList, disgustEmoticonList, surpriseEmoticonList, \
        angerHashtagList, trustHashtagList, fearHashtagList, sadnessHashtagList, anticipationHashtagList, \
        disgustHashtagList, surpriseHashtagList, love, people, \
        message, instant, get, know, going, finalEmotion = line.split('\t')

#        if UserStatus is None:
#            UserStatus = "None"
#        if MediaEntities is '':
#            MediaEntities = "None"
            
        #Picking your choice of variables to be written into the final dataset
        row = [finalEmotion, anger, trust, fear, sadness, anticipation, disgust,
        surprise , joy, positive, negetive, love, people, message, instant, get, know, going,
        Term, Course, Question, tokens, Comments]
        #writing into the dataset
        writer.writerow(row)