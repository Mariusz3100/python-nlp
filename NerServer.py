
import falcon
import json

import spacy

from MySerializers import TokenEncoder, NerEncoder


class NerEndpoint(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.encoder = NerEncoder()

    def on_get(self, req, resp):
        doc = self.nlp(req.params["param"])
        body = self.encoder.encode(doc.ents)
        resp.body = json.dumps(body)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"success": True})
