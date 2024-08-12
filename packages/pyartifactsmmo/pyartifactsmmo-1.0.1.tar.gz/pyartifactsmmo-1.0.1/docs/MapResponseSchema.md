# MapResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MapSchema**](MapSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.map_response_schema import MapResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MapResponseSchema from a JSON string
map_response_schema_instance = MapResponseSchema.from_json(json)
# print the JSON string representation of the object
print(MapResponseSchema.to_json())

# convert the object into a dict
map_response_schema_dict = map_response_schema_instance.to_dict()
# create an instance of MapResponseSchema from a dict
map_response_schema_from_dict = MapResponseSchema.from_dict(map_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


