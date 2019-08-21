import falcon
import json

import spacy

from NerServer import NerEndpoint
from TestServer import TestEndpoint, TestCompoundEndpoint
from TokenizeServer import TokenizeEndpoint

api = falcon.API()
token_endpoint = TokenizeEndpoint()
ner_endpoint = NerEndpoint()
test_endpoint = TestEndpoint()

testCompound = TestCompoundEndpoint()
api.add_route('/tokenizer', token_endpoint)
api.add_route('/ner', ner_endpoint)
api.add_route('/testCompound', testCompound)
