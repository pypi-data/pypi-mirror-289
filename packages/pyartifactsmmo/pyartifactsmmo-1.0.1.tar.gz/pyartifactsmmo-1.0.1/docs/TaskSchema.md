# TaskSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Task objective. | 
**type** | **str** | The type of task. | 
**total** | **int** | The total required to complete the task. | 

## Example

```python
from pyartifactsmmo.models.task_schema import TaskSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSchema from a JSON string
task_schema_instance = TaskSchema.from_json(json)
# print the JSON string representation of the object
print(TaskSchema.to_json())

# convert the object into a dict
task_schema_dict = task_schema_instance.to_dict()
# create an instance of TaskSchema from a dict
task_schema_from_dict = TaskSchema.from_dict(task_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


