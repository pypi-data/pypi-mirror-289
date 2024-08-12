# ItemEffectSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Effect name. | 
**value** | **int** | Effect value. | 

## Example

```python
from pyartifactsmmo.models.item_effect_schema import ItemEffectSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ItemEffectSchema from a JSON string
item_effect_schema_instance = ItemEffectSchema.from_json(json)
# print the JSON string representation of the object
print(ItemEffectSchema.to_json())

# convert the object into a dict
item_effect_schema_dict = item_effect_schema_instance.to_dict()
# create an instance of ItemEffectSchema from a dict
item_effect_schema_from_dict = ItemEffectSchema.from_dict(item_effect_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


