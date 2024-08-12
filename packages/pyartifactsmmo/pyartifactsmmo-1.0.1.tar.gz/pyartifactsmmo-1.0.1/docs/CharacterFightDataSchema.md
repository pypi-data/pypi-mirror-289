# CharacterFightDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**fight** | [**FightSchema**](FightSchema.md) | Fight details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.character_fight_data_schema import CharacterFightDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterFightDataSchema from a JSON string
character_fight_data_schema_instance = CharacterFightDataSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterFightDataSchema.to_json())

# convert the object into a dict
character_fight_data_schema_dict = character_fight_data_schema_instance.to_dict()
# create an instance of CharacterFightDataSchema from a dict
character_fight_data_schema_from_dict = CharacterFightDataSchema.from_dict(character_fight_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


