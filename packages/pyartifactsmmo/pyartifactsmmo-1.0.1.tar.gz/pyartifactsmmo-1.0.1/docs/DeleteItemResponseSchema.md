# DeleteItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteItemSchema**](DeleteItemSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.delete_item_response_schema import DeleteItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemResponseSchema from a JSON string
delete_item_response_schema_instance = DeleteItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteItemResponseSchema.to_json())

# convert the object into a dict
delete_item_response_schema_dict = delete_item_response_schema_instance.to_dict()
# create an instance of DeleteItemResponseSchema from a dict
delete_item_response_schema_from_dict = DeleteItemResponseSchema.from_dict(delete_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


