# GETransactionResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GETransactionListSchema**](GETransactionListSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.ge_transaction_response_schema import GETransactionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GETransactionResponseSchema from a JSON string
ge_transaction_response_schema_instance = GETransactionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GETransactionResponseSchema.to_json())

# convert the object into a dict
ge_transaction_response_schema_dict = ge_transaction_response_schema_instance.to_dict()
# create an instance of GETransactionResponseSchema from a dict
ge_transaction_response_schema_from_dict = GETransactionResponseSchema.from_dict(ge_transaction_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


