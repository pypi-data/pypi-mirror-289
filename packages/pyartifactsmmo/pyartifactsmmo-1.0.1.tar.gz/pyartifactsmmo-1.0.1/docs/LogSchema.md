# LogSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**character** | **str** | Character name. | 
**account** | **str** | Account character. | 
**type** | **str** | Type of action. | 
**description** | **str** | Description of action. | 
**content** | **object** |  | 
**cooldown** | **int** | Cooldown in seconds. | 
**cooldown_expiration** | **datetime** | Datetime of cooldown expiration. | 
**created_at** | **datetime** | Datetime of creation. | 

## Example

```python
from pyartifactsmmo.models.log_schema import LogSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogSchema from a JSON string
log_schema_instance = LogSchema.from_json(json)
# print the JSON string representation of the object
print(LogSchema.to_json())

# convert the object into a dict
log_schema_dict = log_schema_instance.to_dict()
# create an instance of LogSchema from a dict
log_schema_from_dict = LogSchema.from_dict(log_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


