# dict-reorder
**dict-reorder** is a Python package designed to reorder dictionaries.

## Usage
Swapping keys:
```python
import dict_reorder
example = {
    "chemical_formula": "NaCl",
    "compound_name": "Sodium Chloride",
    "molar_mass": 58.443,
    "state_at_room_temp": "solid",
    "melting_point": 800.7,
    "boiling_point": 1465,
    "solubility_in_water": "high",
    "hazard_classification": None
}
example = dict_reorder.swapKeys(example, "compound_name", "chemical_formula")
# New value:
#{
# 'compound_name': 'Sodium Chloride',
# 'chemical_formula': 'NaCl',
# 'molar_mass': 58.443,
# 'state_at_room_temp': 'solid',
# 'melting_point': 800.7,
# 'boiling_point': 1465,
# 'solubility_in_water': 'high',
# 'hazard_classification': None
#}

```

This can also be done with indexes:
```python
dict_reorder.changeKeyIndex(example, "compound_name", 0)
```

Creating your own dictionary and assigning to indexes can also be done:
```python
from dict_reorder import DictReorder
planet = DictReorder()
planet.addKey(name="name", value="earth", index=0)
planet.addKey("gravity", 9.80665, index=2)
planet.addKey("mass", 5.97219e24, 1)
planetInfo = planet.getDictionary()
# `planetInfo`
#{
# 'name': 'earth',
# 'mass': 5.9722e+24,
# 'gravity': 9.80665
#}
```
