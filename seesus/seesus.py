"""Identify 17 Sustainable Development Goals (SDGs) and their 169 targets in text,
and classify into social, environmental, and economic sustainability"""

from seesus.SDG_keys import SDG_keys 
from seesus.see_keys import see_keys 
import regex as re

def id_sus(text):
    """
    Identify the UN Sustainable Development Goals (SDGs) and their associated targets in text.
    
    Input: a string.
    Output:
        sdg: a list of SDGs identified in text.
        target: a list of SDG targets identified in text.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    sdgs = []
    targets = []
    matches = []
    for item in SDG_keys:
        sdg_id = item["SDG_id"]
        sdg_keywords = item["SDG_keywords"]
        match_type = item["match_tpye"]
        if re.search(sdg_keywords, text, re.IGNORECASE):
            sdgs.append(sdg_id.split("_")[0])
            targets.append(sdg_id)
            matches.append(match_type)
    sdgs = list(set(sdgs)) # keep unique sdgs
    targets = list(set(targets)) # keep unique targets
    matches = list(set(matches)) # keep unique match types
    return sdgs, targets, matches

def cat_sus(target):
    """
    Categorize SDG targets into social, environmental, and economic sustainability.
    Input: a list of SDG targets.
    Output: a dictionary of boolean values with social, environmental, and economic sustainability
    as keys.
    """
    see = {"social_sustainability":0, "environmental_sustainability":0, "economic_sustainability":0}
    for item in see_keys:
        sdg_id, soc, env, econ = item[:4]
        for i in range(len(target)):
            if target[i] == sdg_id:
                see["social_sustainability"] += int(soc)
                see["environmental_sustainability"] += int(env)
                see["economic_sustainability"] += int(econ)
    see = {key: True if see[key] > 0 else False for key in see} # convert to boolean values
    return see

class SeeSus():
    """A social, environmental, and economic sustainability classifier."""
    def __init__(self, text):
        self.sdg, self.target, self.match = id_sus(text)
        self.see = cat_sus(self.target)
