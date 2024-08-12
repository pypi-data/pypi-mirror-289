# TaskRewardSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**quantity** | **int** | Item quantity. | 

## Example

```python
from pyartifactsmmo.models.task_reward_schema import TaskRewardSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRewardSchema from a JSON string
task_reward_schema_instance = TaskRewardSchema.from_json(json)
# print the JSON string representation of the object
print(TaskRewardSchema.to_json())

# convert the object into a dict
task_reward_schema_dict = task_reward_schema_instance.to_dict()
# create an instance of TaskRewardSchema from a dict
task_reward_schema_from_dict = TaskRewardSchema.from_dict(task_reward_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


