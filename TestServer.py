from typing import re

import falcon
import json

import spacy

from MySerializers import TokenEncoder


class TestEndpoint(object):

    def on_get(self, req, resp):
        body = {"value": "Ford"}
        resp.body = json.dumps(body)


class TestCompoundEndpoint(object):

    def on_get(self, req, resp):
        entry1 = {"value": "Ford A"}
        entry2 = {"value": "Ford B"}

        entry3 = {"value": "Ford C"}
        body_list = [entry1, entry2, entry3]
        outer_dict = {"list": body_list}
        resp.body = json.dumps(outer_dict)


class TestParamEndpoint(object):

    def on_get(self, req, resp):
        argument = req.params["param"]
        resp.body = json.dumps({"argument": argument})
