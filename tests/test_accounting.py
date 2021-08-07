from financial_inference.accounting import Accounting
from financial_inference.model import Model
import pytest


@pytest.fixture
def vgr_model():
    yield Model(json_path="data/vgr/vgr-2021-q2-10q.json")


@pytest.fixture
def accounting(vgr_model):
    yield Accounting(vgr_model)


@pytest.mark.parametrize(
    "kwargs,expected",
    [
        ({"quarter": 2, "segment": "tobacco"}, None),
        ({"half": 1, "segment": "tobacco"}, None),
        ({"quarter": 2}, 229_119_000),
        ({"half": 1}, 409_341_000),
    ]
)
def test_gross_profit(vgr_model, accounting, kwargs, expected):
    # GIVEN
    # WHEN
    got = accounting.gross_profit(**kwargs)
    # THEN
    if expected is None:
        expected = vgr_model("gross profit", **kwargs)
    assert expected == got


@pytest.mark.parametrize(
    "kwargs",
    [
        {"quarter": 2, "segment": "tobacco"},
        {"half": 1, "segment": "tobacco"},
    ]
)
def test_cogs(vgr_model, accounting, kwargs):
    # GIVEN
    # WHEN
    got = accounting.cogs(**kwargs)
    # THEN
    expected = vgr_model("cogs", **kwargs)
    assert expected == got

