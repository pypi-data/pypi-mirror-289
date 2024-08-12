# ResourceResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceSchema**](ResourceSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.resource_response_schema import ResourceResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceResponseSchema from a JSON string
resource_response_schema_instance = ResourceResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ResourceResponseSchema.to_json())

# convert the object into a dict
resource_response_schema_dict = resource_response_schema_instance.to_dict()
# create an instance of ResourceResponseSchema from a dict
resource_response_schema_from_dict = ResourceResponseSchema.from_dict(resource_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


