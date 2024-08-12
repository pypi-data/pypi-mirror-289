# ActionItemBankResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankItemSchema**](BankItemSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.action_item_bank_response_schema import ActionItemBankResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ActionItemBankResponseSchema from a JSON string
action_item_bank_response_schema_instance = ActionItemBankResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ActionItemBankResponseSchema.to_json())

# convert the object into a dict
action_item_bank_response_schema_dict = action_item_bank_response_schema_instance.to_dict()
# create an instance of ActionItemBankResponseSchema from a dict
action_item_bank_response_schema_from_dict = ActionItemBankResponseSchema.from_dict(action_item_bank_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


