# CraftSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | **str** | Skill required to craft the item. | [optional] 
**level** | **int** | The skill level required to craft the item. | [optional] 
**items** | [**List[SimpleItemSchema]**](SimpleItemSchema.md) | List of items required to craft the item. | [optional] 
**quantity** | **int** | Quantity of items crafted. | [optional] 

## Example

```python
from pyartifactsmmo.models.craft_schema import CraftSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CraftSchema from a JSON string
craft_schema_instance = CraftSchema.from_json(json)
# print the JSON string representation of the object
print(CraftSchema.to_json())

# convert the object into a dict
craft_schema_dict = craft_schema_instance.to_dict()
# create an instance of CraftSchema from a dict
craft_schema_from_dict = CraftSchema.from_dict(craft_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


