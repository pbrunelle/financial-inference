"""
Represent financial data about a company
"""

import json


class Model:

    def __init__(self, json_path):
        with open(json_path, "r") as fin:
            self.obj = json.load(fin)
