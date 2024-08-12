# StatusResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StatusSchema**](StatusSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.status_response_schema import StatusResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponseSchema from a JSON string
status_response_schema_instance = StatusResponseSchema.from_json(json)
# print the JSON string representation of the object
print(StatusResponseSchema.to_json())

# convert the object into a dict
status_response_schema_dict = status_response_schema_instance.to_dict()
# create an instance of StatusResponseSchema from a dict
status_response_schema_from_dict = StatusResponseSchema.from_dict(status_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


