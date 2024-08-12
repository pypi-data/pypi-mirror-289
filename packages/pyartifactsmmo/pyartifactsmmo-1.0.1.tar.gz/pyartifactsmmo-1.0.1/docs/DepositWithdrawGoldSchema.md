# DepositWithdrawGoldSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Quantity of gold. | 

## Example

```python
from pyartifactsmmo.models.deposit_withdraw_gold_schema import DepositWithdrawGoldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DepositWithdrawGoldSchema from a JSON string
deposit_withdraw_gold_schema_instance = DepositWithdrawGoldSchema.from_json(json)
# print the JSON string representation of the object
print(DepositWithdrawGoldSchema.to_json())

# convert the object into a dict
deposit_withdraw_gold_schema_dict = deposit_withdraw_gold_schema_instance.to_dict()
# create an instance of DepositWithdrawGoldSchema from a dict
deposit_withdraw_gold_schema_from_dict = DepositWithdrawGoldSchema.from_dict(deposit_withdraw_gold_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


