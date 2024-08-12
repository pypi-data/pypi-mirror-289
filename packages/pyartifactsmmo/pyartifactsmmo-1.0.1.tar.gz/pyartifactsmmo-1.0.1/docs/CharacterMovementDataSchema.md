# CharacterMovementDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details | 
**destination** | [**MapSchema**](MapSchema.md) | Destination details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Character details. | 

## Example

```python
from pyartifactsmmo.models.character_movement_data_schema import CharacterMovementDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterMovementDataSchema from a JSON string
character_movement_data_schema_instance = CharacterMovementDataSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterMovementDataSchema.to_json())

# convert the object into a dict
character_movement_data_schema_dict = character_movement_data_schema_instance.to_dict()
# create an instance of CharacterMovementDataSchema from a dict
character_movement_data_schema_from_dict = CharacterMovementDataSchema.from_dict(character_movement_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


