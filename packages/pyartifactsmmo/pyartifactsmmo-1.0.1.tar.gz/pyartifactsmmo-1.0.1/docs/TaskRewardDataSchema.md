# TaskRewardDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**reward** | [**TaskRewardSchema**](TaskRewardSchema.md) | Reward details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.task_reward_data_schema import TaskRewardDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRewardDataSchema from a JSON string
task_reward_data_schema_instance = TaskRewardDataSchema.from_json(json)
# print the JSON string representation of the object
print(TaskRewardDataSchema.to_json())

# convert the object into a dict
task_reward_data_schema_dict = task_reward_data_schema_instance.to_dict()
# create an instance of TaskRewardDataSchema from a dict
task_reward_data_schema_from_dict = TaskRewardDataSchema.from_dict(task_reward_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


