# seesus: a social, environmental, and economic sustainability classifier

`seesus` is a **Python** software that evaluates whether a textual expression aligns with the concept of sustainability as defined by the United Nations Sustainable Development Goals (SDGs). It labels a statement with the 17 SDGs as well as 169 specific targets and categorizes the statement into social, environmental, or economic sustainability. For analysis in **R**, please check <a href="https://github.com/Yingjie4Science/SDGdetector" target="_blank">`SDGdector`</a>.

`seesus` currently has four main functions:

1. Evaluate whether a statement aligns with the concept of sustainability
2. Identify SDGs and associated targets in a statement
3. Classify a statement into social, environmental, and economic sustainability
4. Examine and customize match syntax

# Installation

`pip install seesus`

or

`git clone https://github.com/caimeng2/seesus.git`

# Example

```python
from seesus import SeeSus
text = "We aim to contribute to the mitigation of climate change by reducing carbon emissions in the city."
result = SeeSus(text)
print(result.sus)
print(result.sdg_desc)
print(result.target_desc)
print(result.see)
```

```python
SeeSus.show_syntax("SDG1_general")
```

Please run `example.ipynb` to see more example usage.