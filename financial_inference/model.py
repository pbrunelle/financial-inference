"""
Represent financial data about a company
"""

import json


class Model:

    def __init__(self, json_path):
        with open(json_path, "r") as fin:
            self.obj = json.load(fin)
            self.period_data = self.obj["data"]

    def value(self, path, segment=None, fn=float):
        assert len(self.period_data) == 1
        o = self.period_data[0]
        if segment:
            segments = [x for x in o["segments"] if x["segment"] == segment]
            assert len(segments) == 1
            o = segments[0]
        for p in path:
            o = o[p]
        return fn(o)

    def revenue(self, **kwargs):
        return self.value(path=["income statement", "revenue"], **kwargs)

    def __call__(self, name, **kwargs):
        if name == "revenue":
            return self.value(path=["income statement", "revenue"], **kwargs)
        assert False
