# DeleteCharacterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Character name. | 

## Example

```python
from pyartifactsmmo.models.delete_character_schema import DeleteCharacterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCharacterSchema from a JSON string
delete_character_schema_instance = DeleteCharacterSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteCharacterSchema.to_json())

# convert the object into a dict
delete_character_schema_dict = delete_character_schema_instance.to_dict()
# create an instance of DeleteCharacterSchema from a dict
delete_character_schema_from_dict = DeleteCharacterSchema.from_dict(delete_character_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


