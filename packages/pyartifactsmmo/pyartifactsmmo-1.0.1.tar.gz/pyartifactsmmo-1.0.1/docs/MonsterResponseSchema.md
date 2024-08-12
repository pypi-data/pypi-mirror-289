# MonsterResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MonsterSchema**](MonsterSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.monster_response_schema import MonsterResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterResponseSchema from a JSON string
monster_response_schema_instance = MonsterResponseSchema.from_json(json)
# print the JSON string representation of the object
print(MonsterResponseSchema.to_json())

# convert the object into a dict
monster_response_schema_dict = monster_response_schema_instance.to_dict()
# create an instance of MonsterResponseSchema from a dict
monster_response_schema_from_dict = MonsterResponseSchema.from_dict(monster_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


