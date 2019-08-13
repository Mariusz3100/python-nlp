import spacy
import json
from json import JSONEncoder

from MySerializers import MyEncoder


class MyEncoder(JSONEncoder):
    def default(self, token):
        return '{text:' + token.text + '}, {lemma:' + token.lemma_ + '}, {pos:' + token.pos_ + '}, {tag:' + token.tag_ + '} '


nlp = spacy.load("en_core_web_sm")
doc = nlp(u"2 oz of Mt. Gay Eclipse rum")
n = MyEncoder()
tokensParsed = []
for obj in doc:
    oneElement = '{text:' + obj.text + '}, {lemma:' + obj.lemma_ + '}, {pos:' + obj.pos_ + '}, {tag:' + obj.tag_ + '} '
    tokensParsed.append(oneElement)


print(json.dumps(tokensParsed))
