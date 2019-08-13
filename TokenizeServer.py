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
        body = self.encoder.encode(self.nlp(req.params["param"]))
        resp.body = json.dumps(body)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"success": True})
