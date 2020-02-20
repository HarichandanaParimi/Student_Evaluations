class Remove(object):
    def __init__(self):
        pass

    def remove_hashtag(self, tokens):
        tokensList = [x for x in tokens if not x.startswith(r"\#")]
        return tokensList
