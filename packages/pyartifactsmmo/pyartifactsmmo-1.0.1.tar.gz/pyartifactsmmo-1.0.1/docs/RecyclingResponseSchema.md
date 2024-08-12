# RecyclingResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RecyclingDataSchema**](RecyclingDataSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.recycling_response_schema import RecyclingResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RecyclingResponseSchema from a JSON string
recycling_response_schema_instance = RecyclingResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RecyclingResponseSchema.to_json())

# convert the object into a dict
recycling_response_schema_dict = recycling_response_schema_instance.to_dict()
# create an instance of RecyclingResponseSchema from a dict
recycling_response_schema_from_dict = RecyclingResponseSchema.from_dict(recycling_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


