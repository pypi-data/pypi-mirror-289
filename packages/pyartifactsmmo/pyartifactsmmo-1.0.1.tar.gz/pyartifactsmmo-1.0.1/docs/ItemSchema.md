# ItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Item name. | 
**code** | **str** | Item code. This is the item&#39;s unique identifier (ID). | 
**level** | **int** | Item level. | 
**type** | **str** | Item type. | 
**subtype** | **str** | Item subtype. | 
**description** | **str** | Item description. | 
**effects** | [**List[ItemEffectSchema]**](ItemEffectSchema.md) | List of object effects. For equipment, it will include item stats. | [optional] 
**craft** | [**CraftSchema**](CraftSchema.md) |  | [optional] 

## Example

```python
from pyartifactsmmo.models.item_schema import ItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSchema from a JSON string
item_schema_instance = ItemSchema.from_json(json)
# print the JSON string representation of the object
print(ItemSchema.to_json())

# convert the object into a dict
item_schema_dict = item_schema_instance.to_dict()
# create an instance of ItemSchema from a dict
item_schema_from_dict = ItemSchema.from_dict(item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


