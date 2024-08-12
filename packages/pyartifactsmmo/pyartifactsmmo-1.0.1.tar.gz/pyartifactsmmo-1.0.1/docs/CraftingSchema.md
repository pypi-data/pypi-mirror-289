# CraftingSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Craft code. | 
**quantity** | **int** | Quantity of items to craft. | [optional] [default to 1]

## Example

```python
from pyartifactsmmo.models.crafting_schema import CraftingSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CraftingSchema from a JSON string
crafting_schema_instance = CraftingSchema.from_json(json)
# print the JSON string representation of the object
print(CraftingSchema.to_json())

# convert the object into a dict
crafting_schema_dict = crafting_schema_instance.to_dict()
# create an instance of CraftingSchema from a dict
crafting_schema_from_dict = CraftingSchema.from_dict(crafting_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


