from typing import re

import falcon
import json

import spacy

from MySerializers import TokenEncoder


class TokenizeEndpoint(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.encoder = TokenEncoder()

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
            body = {"phrase": phrase, "tokens": encodedTokens}
            resp.body = json.dumps(body)
            resp.status = falcon.HTTP_200
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.set_header('Access-Control-Allow-Methods', 'GET')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type')

    # def on_options(self, req, res):
    #     res.status = falcon.HTTP_200
    #     res.set_header('Access-Control-Allow-Origin', '*')
    #     res.set_header('Access-Control-Allow-Methods', 'GET')
    #     res.set_header('Access-Control-Allow-Headers', 'Content-Type')
