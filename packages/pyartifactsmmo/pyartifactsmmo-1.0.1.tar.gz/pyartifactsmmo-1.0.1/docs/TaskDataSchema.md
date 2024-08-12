# TaskDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**task** | [**TaskSchema**](TaskSchema.md) | Task details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.task_data_schema import TaskDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaskDataSchema from a JSON string
task_data_schema_instance = TaskDataSchema.from_json(json)
# print the JSON string representation of the object
print(TaskDataSchema.to_json())

# convert the object into a dict
task_data_schema_dict = task_data_schema_instance.to_dict()
# create an instance of TaskDataSchema from a dict
task_data_schema_from_dict = TaskDataSchema.from_dict(task_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


