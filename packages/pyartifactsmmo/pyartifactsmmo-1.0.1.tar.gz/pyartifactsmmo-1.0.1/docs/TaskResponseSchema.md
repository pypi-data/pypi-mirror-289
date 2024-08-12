# TaskResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskDataSchema**](TaskDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.task_response_schema import TaskResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResponseSchema from a JSON string
task_response_schema_instance = TaskResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TaskResponseSchema.to_json())

# convert the object into a dict
task_response_schema_dict = task_response_schema_instance.to_dict()
# create an instance of TaskResponseSchema from a dict
task_response_schema_from_dict = TaskResponseSchema.from_dict(task_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


