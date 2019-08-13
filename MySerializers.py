import json
from json import JSONEncoder


class TokenEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = {'text': token.text, 'lemma': token.lemma_, "tag": token.tag_}
            results.append(result)
        return results


class NerEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = {'text': token.text, 'label': token.label_, 'start': token.start_char, 'end': token.end_char}
            results.append(result)
        return results
