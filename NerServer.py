import falcon
import json

import spacy

from MySerializers import TokenEncoder, NerEncoder


class NerEndpoint(object):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.encoder = NerEncoder()

    def on_get(self, req, resp):
        if 'param' not in req.params:
            body = {"phrase": "", "entities": {}}
            resp.body = json.dumps(body)
            resp.status = falcon.HTTP_200
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.set_header('Access-Control-Allow-Methods', 'GET')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
        else:
            phrase = req.params["param"]
            doc = self.nlp(phrase)
            encodedEntities = self.encoder.encode(doc.ents)
            body = {"phrase": phrase, "entities": encodedEntities}
            resp.body = json.dumps(body)
            resp.status = falcon.HTTP_200
            resp.set_header('Access-Control-Allow-Origin', '*')
            resp.set_header('Access-Control-Allow-Methods', 'GET')
            resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
