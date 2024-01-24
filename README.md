<p align="center">
  <img src="docs/logo.jpg" width="400"/>
</p>

# seesus: a social, environmental, and economic sustainability classifier

`seesus` is a **Python** package that evaluates whether a textual expression aligns with the concept of sustainability as defined by the United Nations Sustainable Development Goals (SDGs). It labels a statement with the 17 SDGs as well as 169 specific targets and categorizes the statement into social, environmental, or economic sustainability. For analysis in **R**, please check <a target="_blank" href="https://github.com/Yingjie4Science/SDGdetector">`SDGdector`</a>.

`seesus` currently has four main functions:

1. Evaluating whether a statement aligns with the concept of sustainability
2. Identifying SDGs and associated targets in a statement
3. Classifying a statement into social, environmental, and economic sustainability
4. Customizing match syntax


## Installation

You can install `seesus` from PyPI by inputting the following command in your terminal:

`pip install seesus`


## Example

### Analyzing an individual sentence

```python
from seesus import SeeSus

text1 = "We aim to contribute to the mitigation of climate change by reducing carbon emissions in the city."
result1 = SeeSus(text1)

# print a summary of the results
print(result1)

# print result on whether a statement aligns with sustainability, True or False
print(result1.sus)

# print the names of identified SDGs
print(result1.sdg)
# print the descriptions of identified SDGs
print(result1.sdg_desc)

# print the names of identified SDG targets
print(result1.target)
# print the descriptions of identified SDG targets
print(result1.target_desc)

# determine which dimension of sustainability (social, environmental, or economic) a statement belongs to
print(result1.see)
```

### Analyzing a paragraph/ longer document

To achieve the best results, it is recommended to split a paragraph or a whole document into individual sentences (i.e., using individual sentences as the basic unit for `seesus` to analyze). This can be done by tools such as `nltk.tokenize` and `re.split`.

```python
from nltk.tokenize import sent_tokenize

# source: https://www.nyc.gov/site/planning/about/dcp-priorities/resiliency-sustainability.page
text2 = "By working with communities in the floodplain and facilitating flood-resistant building design, DCP is reducing the city’s risks to sea level rise and coastal flooding. Hurricane Sandy was a stark reminder of these risks. The City, led by the Mayor’s Office of Recovery and Resiliency (ORR), has developed a multifaceted plan for recovering from Sandy and improving the city’s resiliency–the ability of its neighborhoods, buildings and infrastructure to withstand and recover quickly from flooding and climate events. As part of this effort, DCP has initiated a series of projects to identify and implement land use and zoning changes as well as other actions needed to support the short-term recovery and long-term vitality of communities affected by Hurricane Sandy and other areas at risk of coastal flooding."

for sent in sent_tokenize(text2):
    result = SeeSus(sent)
    print('"', sent, '"', sep = "")
    print("Is the sentence related to achieving sustainability?", result.sus)
    print("Which SDGs?", result.sdg)
    print("Which SDG targets specifically?", result.target)
    print("which dimensions of sustainability?", result.see)
    print("----------------")
```

### Customizing match syntax

```python
# print match syntax
SeeSus.show_syntax("SDG1_general")

# customize match dyntax
SeeSus.edit_syntax("SDG1_general", "my match terms")
```

Please run `example.ipynb` to see more example usage.


## Maintenance

Please report any [issues](https://github.com/caimeng2/seesus/issues) if you find that a matching syntax is not accurate or can be improved. We welcome contributions to enhance the classification accuracy of `seesus`.
