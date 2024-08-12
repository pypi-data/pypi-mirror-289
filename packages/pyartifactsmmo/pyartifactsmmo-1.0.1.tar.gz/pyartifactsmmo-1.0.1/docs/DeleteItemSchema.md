# DeleteItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**item** | [**SimpleItemSchema**](SimpleItemSchema.md) | Item details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.delete_item_schema import DeleteItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemSchema from a JSON string
delete_item_schema_instance = DeleteItemSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteItemSchema.to_json())

# convert the object into a dict
delete_item_schema_dict = delete_item_schema_instance.to_dict()
# create an instance of DeleteItemSchema from a dict
delete_item_schema_from_dict = DeleteItemSchema.from_dict(delete_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


