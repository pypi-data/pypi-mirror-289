# TokenResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from pyartifactsmmo.models.token_response_schema import TokenResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseSchema from a JSON string
token_response_schema_instance = TokenResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TokenResponseSchema.to_json())

# convert the object into a dict
token_response_schema_dict = token_response_schema_instance.to_dict()
# create an instance of TokenResponseSchema from a dict
token_response_schema_from_dict = TokenResponseSchema.from_dict(token_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


