# SkillInfoSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xp** | **int** | The amount of xp gained. | 
**items** | [**List[DropSchema]**](DropSchema.md) | Objects received. | 

## Example

```python
from pyartifactsmmo.models.skill_info_schema import SkillInfoSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SkillInfoSchema from a JSON string
skill_info_schema_instance = SkillInfoSchema.from_json(json)
# print the JSON string representation of the object
print(SkillInfoSchema.to_json())

# convert the object into a dict
skill_info_schema_dict = skill_info_schema_instance.to_dict()
# create an instance of SkillInfoSchema from a dict
skill_info_schema_from_dict = SkillInfoSchema.from_dict(skill_info_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


