import falcon
import json

import spacy

from NerServer import NerEndpoint
from TestServer import TestEndpoint, TestCompoundEndpoint, TestParamEndpoint
from TokenizeServer import TokenizeEndpoint

api = falcon.API()
token_endpoint = TokenizeEndpoint()
ner_endpoint = NerEndpoint()
test_endpoint = TestEndpoint()
testParam = TestParamEndpoint()


testCompound = TestCompoundEndpoint()
api.add_route('/tokenizer', token_endpoint)
api.add_route('/ner', ner_endpoint)
api.add_route('/testCompound', testCompound)
api.add_route('/testParam', testParam)
