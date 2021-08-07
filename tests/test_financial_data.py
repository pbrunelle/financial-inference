from financial_inference.model import Model
import pytest


def test_read():
    # GIVEN
    # WHEN
    model = Model(json_path="data/vgr/vgr-2021-q2-10q.json")
    # THEN
    assert model.obj["company"]["ticker"] == "VGR"


@pytest.fixture
def vgr_model():
    yield Model(json_path="data/vgr/vgr-2021-q2-10q.json")


@pytest.mark.parametrize(
    "name,expected",
    [
        ("revenue", 729529000.0),
        ("cogs", 500410000.0),
        ("diluted eps", 0.61),
    ]
)
def test_call(vgr_model, name, expected):
    assert expected == vgr_model(name)


@pytest.mark.parametrize(
    "name,segment,expected",
    [
        ("revenue", "tobacco", 329496000.0),
        ("revenue", "real estate", 400033000.0),
        ("cogs", "tobacco", 206145000.0),
        ("cogs", "real estate", 294265000.0),
    ]
)
def test_call_segment(vgr_model, name, segment, expected):
    assert expected == vgr_model(name, segment=segment)
