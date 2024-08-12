# CooldownSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_seconds** | **int** | The total seconds of the cooldown. | 
**remaining_seconds** | **int** | The remaining seconds of the cooldown. | 
**started_at** | **datetime** | The start of the cooldown. | 
**expiration** | **datetime** | The expiration of the cooldown. | 
**reason** | **str** | The reason of the cooldown. | 

## Example

```python
from pyartifactsmmo.models.cooldown_schema import CooldownSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CooldownSchema from a JSON string
cooldown_schema_instance = CooldownSchema.from_json(json)
# print the JSON string representation of the object
print(CooldownSchema.to_json())

# convert the object into a dict
cooldown_schema_dict = cooldown_schema_instance.to_dict()
# create an instance of CooldownSchema from a dict
cooldown_schema_from_dict = CooldownSchema.from_dict(cooldown_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


