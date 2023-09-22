"""Identify 17 Sustainable Development Goals (SDGs) and their 169 targets in text,
and classify into social, environmental, and economic sustainability."""

import regex as re

from seesus.SDG_keys import SDG_keys
from seesus.see_keys import see_keys
from seesus.SDG_desc import goal_desc, tar_desc

def id_sus(text):
    """
    Identify the UN Sustainable Development Goals (SDGs) and their associated targets in text.

    Parameters
    ----------
    text: str
        Text to be analyzed.
        It is recommended to input one sentence rather than a lengthy paragraph.

    Returns
    -------
    sus: bool
        Whether text aligns with sustainability as defined by the SDGs.
        True: text aligns with the SDGs.
        False: text does not align with the SDGs.
    sdgs: list
        Goal-level SDGs identified in text.
    targets: list
        SDG targets identified in text.
    matches: a list
        Match types, either "direct" (e.g., "no poverty" matches SDG1: No Poverty)
        or "indirect" (e.g., "no more starving" matches SDG2: Zero Hunger).

    Raises
    ------
    TypeError: if text is not a string.
    """
    if not isinstance(text, str): # check input data type
        raise TypeError("Input must be a string.")

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
    targets = list(set(targets))
    matches = list(set(matches))
    sus = bool(sdgs)

    return sus, sdgs, targets, matches

def cat_sus(target):
    """
    Categorize SDG targets into social, environmental, and economic sustainability.

    Parameters
    ----------
    target: list
        SDG targets.

    Returns
    -------
    see: dict
        A dictionary of boolean values with social, environmental, and economic sustainability
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

    Parameters
    ----------
    sdg_id: list
        A list of SDG id.

    Returns
    -------
    sdg_desc: list
        SDG descriptions corresponding to the list of SDG id.
        Source: https://sdgs.un.org/goals
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

    Parameters
    ----------
    target_id: list
        A list of target id.

    Returns
    -------
    target_desc: list
        Target descriptions corresponding to the list of target id.
        Source: https://unstats.un.org/sdgs/indicators/indicators-list/
    """
    target_desc = []

    for item in tar_desc:
        tar_id, desc = item[:2]
        for i in range(len(target_id)):
            if target_id[i] == tar_id:
                target_desc.append(desc)

    return target_desc

class SeeSus():
    """
    A social, environmental, and economic sustainability classifier.

    Attributes
    ----------
    sus: bool
        Whether text aligns with sustainability as defined by the SDGs.
        True: text aligns with the SDGs.
        False: text does not align with the SDGs.
    sdg: list
        Goal-level SDGs identified in text.
    target: list
        SDG targets identified in text.
    match: list
        Match types, either "direct" (e.g., "no poverty" matches SDG1: No Poverty)
        or "indirect" (e.g., "no more starving" matches SDG2: Zero Hunger).
    sdg_desc: list
        SDG descriptions corresponding to the list of SDGs.
        Source: https://sdgs.un.org/goals
    target_desc: list
        Target descriptions corresponding to the list of SDG targets.
        Source: https://unstats.un.org/sdgs/indicators/indicators-list/
    see: dict
        A dictionary of boolean values with social, environmental, and economic sustainability
        as keys.
    """

    def __init__(self, text):
        """
        Parameters
        ----------
        text: str
            Text to be analyzed. It is recommended to input one sentence rather than
            a lengthy paragraph.
        """
        self.sus, self.sdg, self.target, self.match = id_sus(text)
        self.sdg_desc = label_sdg(self.sdg)
        self.target_desc = label_target(self.target)
        self.see = cat_sus(self.target)

    @staticmethod
    def show_syntax(sdg_id):
        """
        Print the regular expression match syntax of target-level SDGs.

        Parameters
        ----------
        sdg_id: str
            Target-level SDG id (e.g., "SDG1_1").

        Returns
        -------
        None

        Raises
        ------
        ValueError: if sdg_id is invalid.
        """
        ids = list({item["SDG_id"] for item in SDG_keys})
        if sdg_id not in ids: # check if sdg id is valid
            raise ValueError(f"Invalid input. Choose one in the list: {ids}")

        syntax = [d for d in SDG_keys if d["SDG_id"] == sdg_id]
        print(syntax)

    @staticmethod
    def edit_syntax(sdg_id, new_syntax, match_type="indirect"):
        """
        Edit the regular expression match syntax of target-level SDGs.

        Parameters
        ----------
        sdg_id: str
            Target level SDG id (e.g., "SDG1_1").
        new_syntax: str
            User defined matching syntax.
            More info on regular expressions: https://regex101.com/.
        match_type: str, optional
            The match type of syntax to be edited, either "direct" (e.g., "SDG 1")
            or "indirect" ("no more starving"). Default is "indirect".

        Returns
        -------
        None

        Raises
        ------
        ValueError: if sdg_id is invalid.
        ValueError: if match_type is invalid.
        """
        ids = list({item["SDG_id"] for item in SDG_keys})
        if sdg_id not in ids:  # check if sdg id is valid
            raise ValueError(f"Invalid input '{sdg_id}'. Use one in the list: {ids}.")
        if match_type not in ["direct", "indirect"]:  # check if match type is valid
            raise ValueError(
                f"Invalid input '{match_type}'. Use 'direct' or 'indirect'. Default is 'indirect'.")

        match = 0
        for item in SDG_keys:
            if item["SDG_id"] == sdg_id and item["match_type"] == match_type:
                match += 1
                item.update({"SDG_keywords": new_syntax})
        if match == 0: # when the direct/indirect match type does not exist
            SDG_keys.append({"SDG_id": sdg_id,
                             "SDG_keywords": new_syntax,
                             "match_type": match_type})

        print(f"The {match_type} match syntax of {sdg_id} has been updated.")
