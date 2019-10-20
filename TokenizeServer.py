import falcon
import json

import spacy
from spacy import displacy
from MySerializers import TokenEncoder, DependencyTreeEncoder


class TokenizeEndpoint(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.encoder = TokenEncoder()
        self.dependencyEncoder = DependencyTreeEncoder()

    def on_get(self, req, resp):

        if 'param' not in req.params:
            body = {"phrase": "", "tokens": {}}
            resp.body = json.dumps(body)
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.set_header('Access-Control-Allow-Methods', 'GET')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        else:
            phrase = req.params["param"]
            tokens = self.nlp(phrase)
            encodedTokens = self.encoder.encode(tokens)
            dependencyParsed = self.dependencyEncoder.encode(tokens)
            body = {"phrase": phrase, "tokens": encodedTokens, "dependencyTree": dependencyParsed}
            resp.body = json.dumps(body)
            resp.status = falcon.HTTP_200
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.set_header('Access-Control-Allow-Methods', 'GET')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type')



            # for token in tokens:
            #     print(
            #         token.text + "=dep:" + token.dep_ + " head: '" + token.head.text + "' pos: '" + token.head.pos_ + "'",
            #         [child for child in token.children])
            # print("\n")
            #
            # for chunk in tokens.noun_chunks:
            #     print(chunk.text, chunk.label_, chunk.root.text)
            #
            # print("\n\n\n")
    # def on_options(self, req, res):
    #     res.status = falcon.HTTP_200
    #     res.set_header('Access-Control-Allow-Origin', '*')
    #     res.set_header('Access-Control-Allow-Methods', 'GET')
    #     res.set_header('Access-Control-Allow-Headers', 'Content-Type')
