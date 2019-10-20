import json
from json import JSONEncoder


class TokenEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = {'text': token.text, 'lemma': token.lemma_, "tag": token.tag_}
            results.append(result)
        return results


class DependencyTreeEncoder(JSONEncoder):
    def encode(self, tokens):

        if len(tokens) > 0:
            curr = tokens[0]
            while curr != curr.head:
                curr = curr.head

            result = self.parse(curr)
            root = {'text': curr.text, 'relationToParent': curr.dep_, "pos": curr.pos_, "children": result}
        return root

    def parse(self, token_arg):
        results = []

        if token_arg.children:
            for token in token_arg.children:
                children = self.parse(token)
                result = {'text': token.text, 'relationToParent': token.dep_, "pos": token.pos_, "children": children}
                results.append(result)

        return results


class NerEncoder(JSONEncoder):
    def encode(self, tokens):
        results = []
        for token in tokens:
            result = {'text': token.text, 'label': token.label_, 'start': token.start_char, 'end': token.end_char}
            results.append(result)
        return results
