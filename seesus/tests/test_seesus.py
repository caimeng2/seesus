import pytest
from seesus.seesus import SeeSus

def test_seesus():
    text = "our goal is to mitigate climate change, end poverty, and reduce inequality globally"
    result = SeeSus(text)
    targets = result.target
    sdgs = result.sdg
    see = result.see
    assert targets == ['SDG13_2', 'SDG13_general', 'SDG10_3', 'SDG1_2']
    assert sdgs == ['SDG10', 'SDG1', 'SDG13']
    assert see == {'social_sustainability': True,
                   'environmental_sustainability': True,
                   'economic_sustainability': False}
