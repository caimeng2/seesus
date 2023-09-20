"""Identify 17 Sustainable Development Goals (SDGs) and their 169 targets in text,
and classify into social, environmental, and economic sustainability"""

from seesus.SDG_keys import SDG_keys 
from seesus.see_keys import see_keys 
from seesus.SDG_desc import goal_desc, tar_desc
import regex as re

def id_sus(text):
    """
    Identify the UN Sustainable Development Goals (SDGs) and their associated targets in text.
    
    Input: a string.
    Output:
        sdgs: a list of SDGs identified in text.
        targets: a list of SDG targets identified in text.
        matches: a list of match types (direct or indirect).
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    sdgs = []
    targets = []
    matches = []
    for item in SDG_keys:
        sdg_id = item["SDG_id"]
        sdg_keywords = item["SDG_keywords"]
        match_type = item["match_type"]
        if re.search(sdg_keywords, text, re.IGNORECASE):
            sdgs.append(sdg_id.split("_")[0])
            targets.append(sdg_id)
            matches.append(match_type)
    sdgs = list(set(sdgs)) # keep unique sdgs
    targets = list(set(targets)) # keep unique targets
    matches = list(set(matches)) 
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

def label_sdg(sdg_id):
    """
    Label SDG id with SDG description.
    Input: a list of SDG id.
    Output: a list of SDG descriptions corresponding to the list of SDG id.
    """
    sdg_desc = []
    for item in goal_desc:
        goal_id, desc = item[:2]
        for i in range(len(sdg_id)):
            if sdg_id[i] == goal_id:
                sdg_desc.append(desc)
    return sdg_desc

def label_target(target_id):
    """
    Label target id with target description.
    Input: a list of target id.
    Output: a list of target descriptions corresponding to the list of target id.
    """
    target_desc = []
    for item in tar_desc:
        tar_id, desc = item[:2]
        for i in range(len(target_id)):
            if target_id[i] == tar_id:
                target_desc.append(desc)
    return target_desc

class SeeSus():
    """A social, environmental, and economic sustainability classifier."""
    def __init__(self, text):
        self.sdg, self.target, self.match = id_sus(text)
        self.sdg_desc = label_sdg(self.sdg)
        self.target_desc = label_target(self.target)
        self.see = cat_sus(self.target)
