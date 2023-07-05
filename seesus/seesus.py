"""Identify 17 Sustainable Development Goals (SDGs) and their 169 targets in text,
and classify into social, environmental, and economic sustainability"""

import csv
import pathlib
import regex as re

def datapath():
    """A helper function for setting up data path."""
    return pathlib.Path(__file__).parent.resolve()

def id_sus(text):
    """
    Identify the UN SDGs and their associated targets in text.
    Input: a string.
    Output:
        sdg: a list of SDGs identified in text.
        target: a list of SDG targets identified in text.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    sdgs = []
    targets = []
    with open(datapath() / "data" / "SDG_keys.csv", "r") as file:
        for row in csv.DictReader(file):
            sdg_id = row["SDG_id"]
            sdg_keywords = row["SDG_keywords"]
            try:
                if re.search(sdg_keywords, text, re.IGNORECASE):
                    targets.append(sdg_id)
                    sdgs.append(sdg_id.split("_")[0])
            except Exception as error:
                print(sdg_keywords)
                print(f"ERROR: {error}")
    sdg = list(set(sdgs)) # keep unique sdgs
    target = list(set(targets)) # keep unique targets
    return sdg, target

def cat_sus(target):
    """
    Categorize SDG targets into social, environmental, and economic sustainability.
    Input: a list of SDG targets.
    Output: a dictionary of boolean values with social, environmental, and economic sustainability
    as keys.
    """
    see = {"social_sustainability":0, "environmental_sustainability":0, "economic_sustainability":0}
    with open(datapath() / "data" / "see.csv", "r") as file:
        next(file) # skip csv header
        for row in csv.reader(file):
            sdg_id, soc, env, econ = row[:4]
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
        self.sdg, self.target = id_sus(text)
        self.see = cat_sus(self.target)
