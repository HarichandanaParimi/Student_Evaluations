import csv


class Utility(object):
    def __init__(self):
        pass

    def getEmoticonDict(self):
        with open('lexicon/emoticon-lexicon.csv', 'rU') as csvFile:
            emoticonReader = csv.reader(csvFile, delimiter=',')
            emoticonEmotion = {}
            for line in emoticonReader:
                if line[0] in emoticonEmotion.keys():
                    emoticonEmotion[line[0]].append(line[1])
                else:
                    emoticonEmotion[line[0]] = [line[1]]
            return emoticonEmotion

    def getWordEmotionDict(self):
        with open('lexicon/wordEmotionSentiment.csv', 'rU') as csvFile:
            emotionReader = csv.reader(csvFile, delimiter=',')
            wordEmotion = {}
            #emotionReader.next()
            next(emotionReader)
            for line in emotionReader:
                if line[0] in wordEmotion.keys():
                    wordEmotion[line[0]].append(line[1])
                else:
                    wordEmotion[line[0]] = [line[1]]
            return wordEmotion

    def getSource(self, rawSource):
        if "iPhone" in rawSource:
            return "iPhone"
        elif "Android" in rawSource:
            return "Android"
        elif "Web" in rawSource:
            return "web"
        elif "TweetDeck" in rawSource:
            return "TweetDeck"

    def getHashtagEmotion(self):
        hashFile = open('lexicon/Hashtag-emotion.txt', 'r')
        data = hashFile.readlines()
        hashTagEmotion = {}
        for line in data:
            if (len(line.split('\t'))) == 3:
                emotion, hashtag, score = line.split('\t')
                hashTagEmotion[hashtag.replace('#', '')] = [emotion, float(score.replace("\r", "").replace("\n", ""))]
        return hashTagEmotion

    def getWordList(self, wordDict):
        angerWordList = ' '.join(wordDict["anger"])
        trustWordList = ' '.join(wordDict["trust"])
        fearWordList = ' '.join(wordDict["fear"])
        sadnessWordList = ' '.join(wordDict["sadness"])
        anticipationWordList = ' '.join(wordDict["anticipation"])
        disgustWordList = ' '.join(wordDict["disgust"])
        surpriseWordList = ' '.join(wordDict["surprise"])
        joyWordList = ' '.join(wordDict["joy"])
        positiveWordList = ' '.join(wordDict["positive"])
        negativeWordList = ' '.join(wordDict["negative"])
        return angerWordList, trustWordList, fearWordList, sadnessWordList, anticipationWordList, disgustWordList, surpriseWordList, joyWordList, positiveWordList, negativeWordList

    def getEmoticonList(self,EmoticonDict):
        angerEmoticonList = ' '.join(EmoticonDict["anger"])
        trustEmoticonList = ' '.join(EmoticonDict["trust"])
        fearEmoticonList = ' '.join(EmoticonDict["fear"])
        sadnessEmoticonList = ' '.join(EmoticonDict["sadness"])
        anticipationEmoticonList = ' '.join(EmoticonDict["anticipation"])
        disgustEmoticonList = ' '.join(EmoticonDict["disgust"])
        surpriseEmoticonList = ' '.join(EmoticonDict["surprise"])
        joyEmoticonList = ' '.join(EmoticonDict["joy"])
        return angerEmoticonList, trustEmoticonList, fearEmoticonList, sadnessEmoticonList, anticipationEmoticonList, disgustEmoticonList, surpriseEmoticonList, joyEmoticonList

    def getHashtagList(self,hashtagDict):
        angerHashtagList = ' '.join(hashtagDict["anger"])
        trustHashtagList = ' '.join(hashtagDict["trust"])
        fearHashtagList = ' '.join(hashtagDict["fear"])
        sadnessHashtagList = ' '.join(hashtagDict["sadness"])
        anticipationHashtagList = ' '.join(hashtagDict["anticipation"])
        disgustHashtagList = ' '.join(hashtagDict["disgust"])
        surpriseHashtagList = ' '.join(hashtagDict["surprise"])
        joyHashtaglist = ' '.join(hashtagDict["joy"])
        return angerHashtagList, trustHashtagList, fearHashtagList, sadnessHashtagList, anticipationHashtagList, disgustHashtagList, surpriseHashtagList,joyHashtaglist