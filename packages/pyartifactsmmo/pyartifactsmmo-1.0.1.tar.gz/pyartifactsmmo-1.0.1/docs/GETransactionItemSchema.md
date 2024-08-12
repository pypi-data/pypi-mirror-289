# GETransactionItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**quantity** | **int** | Item quantity. | 
**price** | **int** | Item price. Item price validation protects you if the price has changed since you last checked the buy/sale price of an item. | 

## Example

```python
from pyartifactsmmo.models.ge_transaction_item_schema import GETransactionItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GETransactionItemSchema from a JSON string
ge_transaction_item_schema_instance = GETransactionItemSchema.from_json(json)
# print the JSON string representation of the object
print(GETransactionItemSchema.to_json())

# convert the object into a dict
ge_transaction_item_schema_dict = ge_transaction_item_schema_instance.to_dict()
# create an instance of GETransactionItemSchema from a dict
ge_transaction_item_schema_from_dict = GETransactionItemSchema.from_dict(ge_transaction_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


