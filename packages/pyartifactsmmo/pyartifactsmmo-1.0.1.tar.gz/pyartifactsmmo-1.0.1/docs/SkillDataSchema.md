# SkillDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**details** | [**SkillInfoSchema**](SkillInfoSchema.md) | Craft details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.skill_data_schema import SkillDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SkillDataSchema from a JSON string
skill_data_schema_instance = SkillDataSchema.from_json(json)
# print the JSON string representation of the object
print(SkillDataSchema.to_json())

# convert the object into a dict
skill_data_schema_dict = skill_data_schema_instance.to_dict()
# create an instance of SkillDataSchema from a dict
skill_data_schema_from_dict = SkillDataSchema.from_dict(skill_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


