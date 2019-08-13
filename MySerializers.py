from json import JSONEncoder


class TokenEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = ['{text:' + token.text + '}, {lemma:' + token.lemma_ + '}, {pos:' + token.pos_ + '}, {tag:' + token.tag_ + '} ']
            results.append(result)
        return results


class NerEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = ['{text:' + token.text + '}, {label:' + token.label_ + '} ']
            results.append(result)
        return results
