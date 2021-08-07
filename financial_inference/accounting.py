"""
Acounting identities
"""

class Accounting:

    def __init__(self, model):
        self.model = model

    def gross_profit(self, **kwargs):
        return self.model("revenue", **kwargs) - self.model("cogs", **kwargs)

    def cogs(self, **kwargs):
        d = self.model.get(["income statement", "cogs"], **kwargs)
        ret = sum([float(v) for k,v in d.items() if k not in ["total", "value"]])
        return ret
