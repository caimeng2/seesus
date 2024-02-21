"""Test seesus module."""

import pytest
from seesus import seesus

def test_id_sus():
    """Test identifying the UN Sustainable Development Goals (SDGs) and their associated targets in text."""
    text1 = "our goal is to end poverty"
    text2 = "we care about SDG 2"
    sus1, sdgs1, targets1, matches1 = seesus.id_sus(text1)
    sus2, sdgs2, targets2, matches2 = seesus.id_sus(text2)
    assert sus1 == True
    assert sdgs1 == ['SDG1']
    assert targets1 == ['SDG1_2']
    assert matches1 == ['indirect']
    assert sus2 == True
    assert sdgs2 == ['SDG2']
    assert targets2 == ['SDG2_general']
    assert matches2 == ['direct']

def test_cat_sus():
    """Test categorizing SDG targets into social, environmental, and economic sustainability."""
    assert seesus.cat_sus(["SDG1_2"]) == {'social_sustainability': True, 
                                             'environmental_sustainability': False, 
                                             'economic_sustainability': False}

def test_label_sdg():
    """Test labeling SDG id with SDG description."""
    assert seesus.label_sdg(["SDG1"]) == ['No Poverty']
    
def test_label_target():
    """Test labeling target id with target description."""
    assert seesus.label_target(['SDG1_2']) == ['By 2030, reduce at least by half the proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions']
    
def test_show_syntax():
    """Test printing the regular expression match syntax of SDGs."""
    assert seesus.SeeSus.show_syntax("SDG1_general") is None
    
def test_edit_syntax():
    """Test editing the regular expression match syntax of target-level SDGs."""
    assert seesus.SeeSus.edit_syntax("SDG1_general", "new terms") is None
    