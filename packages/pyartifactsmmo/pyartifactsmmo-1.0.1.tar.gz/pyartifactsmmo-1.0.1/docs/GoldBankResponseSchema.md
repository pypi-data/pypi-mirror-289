# GoldBankResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GoldSchema**](GoldSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.gold_bank_response_schema import GoldBankResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GoldBankResponseSchema from a JSON string
gold_bank_response_schema_instance = GoldBankResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GoldBankResponseSchema.to_json())

# convert the object into a dict
gold_bank_response_schema_dict = gold_bank_response_schema_instance.to_dict()
# create an instance of GoldBankResponseSchema from a dict
gold_bank_response_schema_from_dict = GoldBankResponseSchema.from_dict(gold_bank_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


