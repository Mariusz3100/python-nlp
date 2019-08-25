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
        else:
            phrase = req.params["param"]
            tokens = self.nlp(phrase)
            encodedTokens = self.encoder.encode(tokens)
            body = {"phrase": phrase, "tokens": encodedTokens}
            resp.body = json.dumps(body)
