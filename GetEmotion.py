#!/usr/bin/python
# -*- coding: ascii -*-
#import os
import csv
import operator
from utility import Utility
#import sys
#import progressbar

class GetEmotion(object):
    def __init__(self):
        # Intializing variables
        #Input file
        self.input = open('Data/studentEvaluation-0324-preprocessed.txt', 'r')
        self.data = self.input.readlines()
        self.util = Utility()
        self.wordEmotion = self.util.getWordEmotionDict()
#        self.hashtagEmotion = self.util.getHashtagEmotion()
        self.emoticonEmotion = self.util.getEmoticonDict()
        #output file
        self.output = open('Data/datawithemotions.csv', 'w', newline='')
        #self.bar = progressbar.ProgressBar(maxval=len(self.data))
        self.writer = csv.writer(self.output)
    
    def process(self):
        for i, line in enumerate(self.data):
            if (len(line.split('\t'))) == 6:
               # self.bar.update(i)
                # Assigning values for all variables
                Year, Term, Course, Question, tokens, Comments = line.split('\t')
                # Empty dictionary for recording emotion scores
                emoDict = {"anger": 0, "trust": 0, "fear": 0, "sadness": 0, "anticipation": 0, "disgust": 0,
                                "surprise": 0,"joy": 0, "positive": 0, "negative": 0}
                # Empty dictionary for recording emotion words
                emoWordDict = {"anger": [], "trust": [], "fear": [], "sadness": [], "anticipation": [],
                                    "disgust": [], "surprise": [], "joy": [], "negative": [], "positive": []}
                # Empty dictionary for recording emotion emoticons
                emoticonDict = {"anger": [], "trust": [], "fear": [], "sadness": [], "anticipation": [],
                                     "disgust": [],
                                     "surprise": [], "joy": [], "negative": [], "positive": []}
                # Empty dictionary for recording emotion Hashtags
#                hashtagDict = {"anger": [], "trust": [], "fear": [], "sadness": [], "anticipation": [],
#                                    "disgust": [],
#                                    "surprise": [], "joy": [], "negative": [], "positive": []}
                # Empty dictionary for recording if frequently occuring word and verbs are present or not
                #frequentDict = {"love": 0, "people": 0, "message": 0, "instant": 0,"get":0,"know":0,"going":0}
                for token in tokens.split(" "):
#                    if "#" in token:
#                        token = token.replace("#", "")
#                        print("inside hash")
#                        # Comparing Hashtag with hashtag emotion lexicon
#                        if token in self.hashtagEmotion.keys():
#                            emoscore = self.hashtagEmotion[token]
#                            emoDict[emoscore[0]] = emoDict[emoscore[0]] + emoscore[1]
#                            hashtagDict[emoscore[0]].append('#'+token)
                    # Comparing word with the word-emotion lexicon
                    if token in self.wordEmotion.keys():
                        for emotion in self.wordEmotion[token]:
                            emoDict[emotion] = emoDict[emotion] + 1
                            emoWordDict[emotion].append(token)
                    # Comparing emoticon with emoticon-emotion lexicon
                    elif token in self.emoticonEmotion.keys():
                        print("inside emoticon")
                        for emotion in self.emoticonEmotion[token]:
                            emoDict[emotion] = emoDict[emotion] + 1
                            emoticonDict[emotion].append(token)
#                for token in tokens.split(" "):
#                    if token in frequentDict.keys():
#                        frequentDict[token] = 1
                # Recording positive and negetive scores
                positive = emoDict["positive"]
                negative = emoDict["negative"]
                # Deleting negetive and positive scores from dictionary
                del emoDict["positive"]
                del emoDict["negative"]
                # Getting final emotion from the dictionary
#                finalEmotion = max(emoDict.iteritems(), key=operator.itemgetter(1))[0]
                finalEmotion = max(emoDict.items(), key=operator.itemgetter(1))[0]
                #print(finalEmotion)
                # Converting source to simpler form
#                source = self.util.getSource(rawSource)
#                if UserStatus is None:
#                    UserStatus = "None"
#                if MediaEntities is '':
#                    MediaEntities = "None"
#                user_timezone = user_timezone.replace('\"','')
#                user_timezone = user_timezone.replace("\'", "")
                # Getting emotion word list
                angerWordList, trustWordList, fearWordList, sadnessWordList, anticipationWordList, disgustWordList, \
                surpriseWordList, joyWordList, positiveWordList, negativeWordList = self.util.getWordList(emoWordDict)
                # Getting emoticon word list
                angerEmoticonList, trustEmoticonList, fearEmoticonList, sadnessEmoticonList, anticipationEmoticonList, \
                disgustEmoticonList, surpriseEmoticonList, joyEmoticonList = self.util.getEmoticonList(emoticonDict)
                # Getting Hashtag word list
#                angerHashtagList, trustHashtagList, fearHashtagList, sadnessHashtagList, anticipationHashtagList, \
#                disgustHashtagList, surpriseHashtagList, joyHashtaglist = self.util.getHashtagList(hashtagDict)
                # filtering emotion whose final score is 0.
                
                if emoDict[finalEmotion] is not 0:
                    # Writing all the variables to the file
                    seq = [Year, Term, Course, Question, tokens, Comments, str(emoDict["anger"]), str(emoDict["trust"]), str(emoDict["fear"]),
                           str(emoDict["sadness"]), str(emoDict["anticipation"]), str(emoDict["disgust"]),
                           str(emoDict["surprise"]), str(emoDict["joy"]), 
#                           str(emoDict["positive"]), str(emoDict["negative"]),
                           str(positive), str(negative), 
                           angerWordList, trustWordList,
                           fearWordList, sadnessWordList, anticipationWordList, disgustWordList, surpriseWordList, joyWordList, positiveWordList, negativeWordList,
                           angerEmoticonList, trustEmoticonList, fearEmoticonList, sadnessEmoticonList,
                           anticipationEmoticonList,  disgustEmoticonList, surpriseEmoticonList, joyEmoticonList,
#                           angerHashtagList, trustHashtagList, fearHashtagList, sadnessHashtagList, anticipationHashtagList,
#                           disgustHashtagList, surpriseHashtagList, joyHashtaglist,
#                           str(frequentDict["love"]),str(frequentDict["people"]),
#                           str(frequentDict["message"]), str(frequentDict["instant"]),str(frequentDict["get"]),
#                           str(frequentDict["know"]),str(frequentDict["going"]), 
                           finalEmotion]
                    self.writer.writerow(seq)

if __name__ == '__main__':
    obj = GetEmotion()
    obj.process()
