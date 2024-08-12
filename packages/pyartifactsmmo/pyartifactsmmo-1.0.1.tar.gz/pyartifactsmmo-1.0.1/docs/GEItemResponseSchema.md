# GEItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GEItemSchema**](GEItemSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.ge_item_response_schema import GEItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GEItemResponseSchema from a JSON string
ge_item_response_schema_instance = GEItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GEItemResponseSchema.to_json())

# convert the object into a dict
ge_item_response_schema_dict = ge_item_response_schema_instance.to_dict()
# create an instance of GEItemResponseSchema from a dict
ge_item_response_schema_from_dict = GEItemResponseSchema.from_dict(ge_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


