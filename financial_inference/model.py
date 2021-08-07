"""
Represent financial data about a company
"""

import json


class Model:

    def __init__(self, json_path):
        with open(json_path, "r") as fin:
            self.obj = json.load(fin)
            self.period_data = self.obj["data"]

    def value(self, path, fn=float):
        o = self.period_data[0]
        for p in path:
            o = o[p]
        return fn(o)

    def revenue(self):
        return self.value(["income statement", "revenue"])
