# SkillResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SkillDataSchema**](SkillDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.skill_response_schema import SkillResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SkillResponseSchema from a JSON string
skill_response_schema_instance = SkillResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SkillResponseSchema.to_json())

# convert the object into a dict
skill_response_schema_dict = skill_response_schema_instance.to_dict()
# create an instance of SkillResponseSchema from a dict
skill_response_schema_from_dict = SkillResponseSchema.from_dict(skill_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


