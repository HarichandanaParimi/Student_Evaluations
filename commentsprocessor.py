
from cleanComments import CleanComments
from remover import Remove
from nltk.tokenize import TweetTokenizer
import re

regex_str = [
    #emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    #r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    tknzr = TweetTokenizer()
    return tknzr.tokenize(s)


def preprocess(s, lowercase=True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token.lower() for token in tokens]
        tokens = [token.decode("utf8").encode('ascii', 'ignore') for token in tokens]
        tokens = [token for token in tokens if len(token)>1]
    return tokens


class CommentsProcessor(object):
    def __init__(self):
        self.cleaner = CleanTweet()
        self.remover = Remove()

    def cleanComments(self, string):
        for cleanup_method in self.cleaner.iterate():
            string = cleanup_method(string)
        finalTokens = preprocess(string)
        for token in finalTokens:
            if token == 'rt':
                finalTokens.remove(token)
        return finalTokens

