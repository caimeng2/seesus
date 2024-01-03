<p align="center">
  <img src="docs/logo.jpg" width="400"/>
</p>

# seesus: a social, environmental, and economic sustainability classifier

`seesus` is a **Python** package that evaluates whether a textual expression aligns with the concept of sustainability as defined by the United Nations Sustainable Development Goals (SDGs). It labels a statement with the 17 SDGs as well as 169 specific targets and categorizes the statement into social, environmental, or economic sustainability. For analysis in **R**, please check <a target="_blank" href="https://github.com/Yingjie4Science/SDGdetector">`SDGdector`</a>.

`seesus` currently has four main functions:

1. Evaluate whether a statement aligns with the concept of sustainability
2. Identify SDGs and associated targets in a statement
3. Classify a statement into social, environmental, and economic sustainability
4. Examine and customize match syntax

# Installation

`pip install seesus`


# Example

```python
from seesus import SeeSus

text = "We aim to contribute to the mitigation of climate change by reducing carbon emissions in the city."
result = SeeSus(text)

# print a summary of the results
print(result)

# print result on whether a statement aligns with sustainability, True or False
print(result.sus)

# print the names of identified SDGs
print(result.sdg)
# print the descriptions of identified SDGs
print(result.sdg_desc)

# print the names of identified SDG targets
print(result.target)
# print the descriptions of identified SDG targets
print(result.target_desc)

# determine which dimension of sustainability (social, environmental, or economic) a statement belongs to
print(result.see)

# print match syntax
SeeSus.show_syntax("SDG1_general")

# customize match dyntax
SeeSus.edit_syntax("SDG1_general", "my match terms")
```

Please run `example.ipynb` to see more example usage.
