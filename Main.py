import falcon
import json

import spacy

from NerServer import NerEndpoint
from TokenizeServer import TokenizeEndpoint

api = falcon.API()
token_endpoint = TokenizeEndpoint()
ner_endpoint=NerEndpoint()
api.add_route('/tokenizer', token_endpoint)
api.add_route('/ner', ner_endpoint)
