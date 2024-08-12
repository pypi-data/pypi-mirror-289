# CharacterFightResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CharacterFightDataSchema**](CharacterFightDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.character_fight_response_schema import CharacterFightResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterFightResponseSchema from a JSON string
character_fight_response_schema_instance = CharacterFightResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterFightResponseSchema.to_json())

# convert the object into a dict
character_fight_response_schema_dict = character_fight_response_schema_instance.to_dict()
# create an instance of CharacterFightResponseSchema from a dict
character_fight_response_schema_from_dict = CharacterFightResponseSchema.from_dict(character_fight_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


