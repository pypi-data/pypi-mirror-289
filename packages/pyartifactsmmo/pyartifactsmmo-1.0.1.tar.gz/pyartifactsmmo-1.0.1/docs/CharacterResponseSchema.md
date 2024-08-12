# CharacterResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CharacterSchema**](CharacterSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.character_response_schema import CharacterResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterResponseSchema from a JSON string
character_response_schema_instance = CharacterResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterResponseSchema.to_json())

# convert the object into a dict
character_response_schema_dict = character_response_schema_instance.to_dict()
# create an instance of CharacterResponseSchema from a dict
character_response_schema_from_dict = CharacterResponseSchema.from_dict(character_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


