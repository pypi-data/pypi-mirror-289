# ItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SingleItemSchema**](SingleItemSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.item_response_schema import ItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponseSchema from a JSON string
item_response_schema_instance = ItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ItemResponseSchema.to_json())

# convert the object into a dict
item_response_schema_dict = item_response_schema_instance.to_dict()
# create an instance of ItemResponseSchema from a dict
item_response_schema_from_dict = ItemResponseSchema.from_dict(item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


