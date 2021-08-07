from financial_inference.model import Model

def test_1():
    model = Model(json_path="data/vgr/vgr-2021-q2-10q.json")
    assert model.obj["company"]["ticker"] == "VGR"
