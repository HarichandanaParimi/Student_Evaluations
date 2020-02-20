
from nltk.corpus import stopwords

from tweetemotion import TweetProcessor
from io import open
obj = TweetProcessor()


# Function to get slangs from text file
def getSlangs():
    dict = {}
    with open('lexicon/slangs.txt', encoding='utf-8') as data:
        slangs = data.readlines()
        for line in slangs:
            slang, abbr = line.split('\t')
            dict[slang] = abbr
    return dict

# Reading the raw data
input = open('Data/2018-2019ParsedData.txt', encoding='Latin-1')

# Creating the output file
output = open('Data/studentEvaluation-0324-preprocessed.txt', 'wb')
# Reading lines
data = input.readlines()
textList = []
# Getting stop words of english
stopwordsList = stopwords.words("english")
#print(stopwordsList)
# Iterating through the data
for line in data:
    # filtering lines of length 25. i.e. 25 columns
    if (len(line.split('\t'))) == 5:
        # Assigning values to variables
        Year, Term, Course, Question, Comments = line.split('\t')
        try:
            # Using the cleaning module to clean the comments
            tokens = obj.cleanComments(Comments)
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue
        slangs = getSlangs()
        extraTokens = []
        for token in tokens:
            # Decoding slangs in comments
            if token in slangs.keys():
                print ("Slang:",token)
                if len(slangs[token].split(' ')) > 1:
                    extraTokens.extend(slangs[token].split(' '))
                else:
                    extraTokens.append(slangs[token])
                tokens.remove(token)
        # Adding the slangs meaning to the comemnts
        for token in extraTokens:
            tokens.append(token.strip('\n'))
        # Removing stop words
        for idx, stopWord in enumerate(stopwordsList):
            if stopWord in tokens:
                tokens.remove(stopWord)
#        print (Comments)
#        print (tokens)
        tokenJoined = ' '.join(tokens)
        if len(tokenJoined) > 1:
            #print(len(tokenJoined))
            # Writing data to the output file.
            sequence = (
                Year, Term, Course, Question, tokenJoined, Comments)
            rowData = '\t'.join(sequence)
            #print("RowDATA:", rowData)
            output.write(rowData.encode('ascii', 'ignore'))
output.close