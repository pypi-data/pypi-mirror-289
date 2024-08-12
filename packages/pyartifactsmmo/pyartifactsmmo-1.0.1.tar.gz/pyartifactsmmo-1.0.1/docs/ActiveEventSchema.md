# ActiveEventSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event. | 
**map** | [**MapSchema**](MapSchema.md) | Map of the event. | 
**previous_skin** | **str** | Previous map skin. | 
**duration** | **int** | Duration in minutes. | 
**expiration** | **datetime** | Expiration datetime. | 
**created_at** | **datetime** | Start datetime. | 

## Example

```python
from pyartifactsmmo.models.active_event_schema import ActiveEventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveEventSchema from a JSON string
active_event_schema_instance = ActiveEventSchema.from_json(json)
# print the JSON string representation of the object
print(ActiveEventSchema.to_json())

# convert the object into a dict
active_event_schema_dict = active_event_schema_instance.to_dict()
# create an instance of ActiveEventSchema from a dict
active_event_schema_from_dict = ActiveEventSchema.from_dict(active_event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


