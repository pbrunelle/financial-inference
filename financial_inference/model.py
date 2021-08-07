"""
Represent financial data about a company
"""

import json


class Model:

    ModelMapping = {
        "revenue": {"path": ["income statement", "revenue"]},
        "cogs": {"path": ["income statement", "cogs"]},
        "diluted eps": {"path": ["income statement", "net income per diluted share"]},
    }

    def __init__(self, json_path):
        with open(json_path, "r") as fin:
            self.obj = json.load(fin)
            self.period_data = self.obj["data"]

    def value(self, path, year=None, quarter=None, half=None, segment=None, fn=float):
        o = self.period_data
        if year:
            o = [x for x in o if x.get("period", {}).get("year") == year]
        if quarter:
            o = [x for x in o if x.get("period", {}).get("quarter") == quarter]
        if half:
            o = [x for x in o if x.get("period", {}).get("half") == half]
        assert len(o) == 1, f"Expected 1 matching period got {len(o)}"
        o = o[0]
        if segment:
            segments = [x for x in o["segments"] if x["segment"] == segment]
            assert len(segments) == 1
            o = segments[0]
        for p in path:
            o = o[p]
        if isinstance(o, dict):
            if "total" in o:
                o = o["total"]
            elif "value" in o:
                o = o["value"]
        return fn(o)

    def __call__(self, name, **kwargs):
        return self.value(**Model.ModelMapping[name], **kwargs)
