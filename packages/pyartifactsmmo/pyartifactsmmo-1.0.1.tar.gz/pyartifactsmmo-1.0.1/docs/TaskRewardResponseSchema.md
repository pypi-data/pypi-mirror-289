# TaskRewardResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskRewardDataSchema**](TaskRewardDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.task_reward_response_schema import TaskRewardResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRewardResponseSchema from a JSON string
task_reward_response_schema_instance = TaskRewardResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaskRewardResponseSchema.to_json())

# convert the object into a dict
task_reward_response_schema_dict = task_reward_response_schema_instance.to_dict()
# create an instance of TaskRewardResponseSchema from a dict
task_reward_response_schema_from_dict = TaskRewardResponseSchema.from_dict(task_reward_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


