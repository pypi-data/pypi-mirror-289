# GETransactionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**quantity** | **int** | Item quantity. | 
**price** | **int** | Item price. | 
**total_price** | **int** | Total price of the transaction. | 

## Example

```python
from pyartifactsmmo.models.ge_transaction_schema import GETransactionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GETransactionSchema from a JSON string
ge_transaction_schema_instance = GETransactionSchema.from_json(json)
# print the JSON string representation of the object
print(GETransactionSchema.to_json())

# convert the object into a dict
ge_transaction_schema_dict = ge_transaction_schema_instance.to_dict()
# create an instance of GETransactionSchema from a dict
ge_transaction_schema_from_dict = GETransactionSchema.from_dict(ge_transaction_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


