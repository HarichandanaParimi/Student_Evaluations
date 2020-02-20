
from HTMLParser import HTMLParser
import re


class CleanComments(object):
    def __init__(self):
        self.htmlParser = HTMLParser()

    def iterate(self):
        for cleanup_method in [self.remove_urls,
                               self.remove_usernames,
                               self.remove_na,
                               #self.remove_special_chars,
                               self.remove_numbers,
                              # self.remove_hashtags,
                               self.decode_data,
                               self.splitWords]:
            yield cleanup_method

    @staticmethod
    def remove_by_regex(comments, regexp):
        comments = re.sub(regexp, "", comments)
        return comments

    def escape_HTML(self, comments):
        return self.htmlParser.unescape(comments)

    def decode_data(self, comments):
        return comments.decode("utf8").encode('ascii', 'ignore')

    def remove_urls(self, comments):
        return CleanComments.remove_by_regex(comments, re.compile(r"http.?://[^\s]+[\s]?"))

    def splitWords(self,comments):
        return " ".join(re.findall('[A-Z][^A-Z]*',comments))

    def remove_na(self, comments):
        if comments != "Not Available":
            return comments

    def remove_hashtags(self, comments):
        return CleanComments.remove_by_regex(comments, re.compile(r"#(\w+)"))

    def remove_special_chars(self, comments):
        for remove in map(lambda r: re.compile(re.escape(r)), [",", "\"", "=", "&", ";", "%", "$",
                                                               "@", "%", "^", "*", "(", ")", "{", "}",
                                                               "[", "]", "|", "/", "\\", ">", "<", "-",
                                                               "!", "?", ".", "'",
                                                               "--", "---"]):
            comments = re.sub(remove, "", comments)
        return comments

    def remove_usernames(self, comments):
        return CleanComments.remove_by_regex(comments, re.compile(r"@[^\s]+[\s]?"))

    def remove_numbers(self, comments):
        return CleanComments.remove_by_regex(comments, re.compile(r"\s?[0-9]+\.?[0-9]*"))
