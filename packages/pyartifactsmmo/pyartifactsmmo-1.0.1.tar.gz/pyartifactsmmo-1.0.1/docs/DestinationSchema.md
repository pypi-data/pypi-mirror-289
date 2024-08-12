# DestinationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | The x coordinate of the destination. | 
**y** | **int** | The y coordinate of the destination. | 

## Example

```python
from pyartifactsmmo.models.destination_schema import DestinationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationSchema from a JSON string
destination_schema_instance = DestinationSchema.from_json(json)
# print the JSON string representation of the object
print(DestinationSchema.to_json())

# convert the object into a dict
destination_schema_dict = destination_schema_instance.to_dict()
# create an instance of DestinationSchema from a dict
destination_schema_from_dict = DestinationSchema.from_dict(destination_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


