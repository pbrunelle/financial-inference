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


def test_revenue(vgr_model):
    # GIVEN
    # WHEN
    got = vgr_model.revenue()
    # THEN
    assert 729529000.0 == got


@pytest.mark.parametrize(
    "segment,expected",
    [
        ("tobacco", 329496000.0),
        ("real estate", 400033000.0),
    ]
)
def test_revenue_segment(vgr_model, segment, expected):
    # GIVEN
    # WHEN
    got = vgr_model.revenue(segment=segment)
    # THEN
    assert expected == got


def test_call_revenue(vgr_model):
    # GIVEN
    # WHEN
    got = vgr_model("revenue")
    # THEN
    assert 729529000.0 == got


@pytest.mark.parametrize(
    "segment,expected",
    [
        ("tobacco", 329496000.0),
        ("real estate", 400033000.0),
    ]
)
def test_call_revenue_segment(vgr_model, segment, expected):
    # GIVEN
    # WHEN
    got = vgr_model("revenue", segment=segment)
    # THEN
    assert expected == got
