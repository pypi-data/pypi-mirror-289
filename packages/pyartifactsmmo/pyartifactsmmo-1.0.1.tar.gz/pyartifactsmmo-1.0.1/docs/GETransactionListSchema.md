# GETransactionListSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**transaction** | [**GETransactionSchema**](GETransactionSchema.md) | Transaction details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Character details. | 

## Example

```python
from pyartifactsmmo.models.ge_transaction_list_schema import GETransactionListSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GETransactionListSchema from a JSON string
ge_transaction_list_schema_instance = GETransactionListSchema.from_json(json)
# print the JSON string representation of the object
print(GETransactionListSchema.to_json())

# convert the object into a dict
ge_transaction_list_schema_dict = ge_transaction_list_schema_instance.to_dict()
# create an instance of GETransactionListSchema from a dict
ge_transaction_list_schema_from_dict = GETransactionListSchema.from_dict(ge_transaction_list_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


