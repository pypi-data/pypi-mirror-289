# GoldResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoldTransactionSchema**](GoldTransactionSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.gold_response_schema import GoldResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GoldResponseSchema from a JSON string
gold_response_schema_instance = GoldResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GoldResponseSchema.to_json())

# convert the object into a dict
gold_response_schema_dict = gold_response_schema_instance.to_dict()
# create an instance of GoldResponseSchema from a dict
gold_response_schema_from_dict = GoldResponseSchema.from_dict(gold_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


