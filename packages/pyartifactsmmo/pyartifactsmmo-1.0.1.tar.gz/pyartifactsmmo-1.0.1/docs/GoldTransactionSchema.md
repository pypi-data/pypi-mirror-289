# GoldTransactionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**bank** | [**GoldSchema**](GoldSchema.md) | Bank details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.gold_transaction_schema import GoldTransactionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GoldTransactionSchema from a JSON string
gold_transaction_schema_instance = GoldTransactionSchema.from_json(json)
# print the JSON string representation of the object
print(GoldTransactionSchema.to_json())

# convert the object into a dict
gold_transaction_schema_dict = gold_transaction_schema_instance.to_dict()
# create an instance of GoldTransactionSchema from a dict
gold_transaction_schema_from_dict = GoldTransactionSchema.from_dict(gold_transaction_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


