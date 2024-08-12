# StatusSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Server status | 
**version** | **str** |  | [optional] 
**characters_online** | **int** |  | [optional] 
**server_time** | **datetime** |  | [optional] 
**announcements** | [**List[AnnouncementSchema]**](AnnouncementSchema.md) |  | [optional] 
**last_wipe** | **str** | Last server wipe. | 
**next_wipe** | **str** | Next server wipe. | 

## Example

```python
from pyartifactsmmo.models.status_schema import StatusSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StatusSchema from a JSON string
status_schema_instance = StatusSchema.from_json(json)
# print the JSON string representation of the object
print(StatusSchema.to_json())

# convert the object into a dict
status_schema_dict = status_schema_instance.to_dict()
# create an instance of StatusSchema from a dict
status_schema_from_dict = StatusSchema.from_dict(status_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


