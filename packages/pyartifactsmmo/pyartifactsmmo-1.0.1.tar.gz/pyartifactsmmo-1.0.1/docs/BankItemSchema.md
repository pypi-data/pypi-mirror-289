# BankItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**item** | [**ItemSchema**](ItemSchema.md) | Item details. | 
**bank** | [**List[SimpleItemSchema]**](SimpleItemSchema.md) | Items in your banks. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.bank_item_schema import BankItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BankItemSchema from a JSON string
bank_item_schema_instance = BankItemSchema.from_json(json)
# print the JSON string representation of the object
print(BankItemSchema.to_json())

# convert the object into a dict
bank_item_schema_dict = bank_item_schema_instance.to_dict()
# create an instance of BankItemSchema from a dict
bank_item_schema_from_dict = BankItemSchema.from_dict(bank_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


