# README
Content
- `code` folder contains demo to create pydantic datamodel objects from datamodel in model.py
- `model` contains manually fixed datamodel python file that is usable
- `data` all the schema defintion and data used

## Current Issues

`datamodel-codegen` command cannot directly create usable model

- There are single word definition in the schema that confuses python -> for key definition like "Site" or "Social", they should be changed into "Site_" or "Site ". Otherwise, we need to manually adjust the field name and field alias in the created model.py 
- `pydantic_demo.ipynb` is runnable except the second block that executes `datamodel-codegen` for the reason above. Replacing content in `model.py` with the content in `/model/model_fixed.py` can make the remaining of the code work. 