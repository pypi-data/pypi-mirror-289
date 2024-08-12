# GEItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**stock** | **int** | Item stock. | 
**sell_price** | **int** | The item&#39;s selling price. | [optional] 
**buy_price** | **int** | The item&#39;s buying price. | [optional] 

## Example

```python
from pyartifactsmmo.models.ge_item_schema import GEItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GEItemSchema from a JSON string
ge_item_schema_instance = GEItemSchema.from_json(json)
# print the JSON string representation of the object
print(GEItemSchema.to_json())

# convert the object into a dict
ge_item_schema_dict = ge_item_schema_instance.to_dict()
# create an instance of GEItemSchema from a dict
ge_item_schema_from_dict = GEItemSchema.from_dict(ge_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


