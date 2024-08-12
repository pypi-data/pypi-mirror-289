# CharacterMovementResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CharacterMovementDataSchema**](CharacterMovementDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.character_movement_response_schema import CharacterMovementResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterMovementResponseSchema from a JSON string
character_movement_response_schema_instance = CharacterMovementResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterMovementResponseSchema.to_json())

# convert the object into a dict
character_movement_response_schema_dict = character_movement_response_schema_instance.to_dict()
# create an instance of CharacterMovementResponseSchema from a dict
character_movement_response_schema_from_dict = CharacterMovementResponseSchema.from_dict(character_movement_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


