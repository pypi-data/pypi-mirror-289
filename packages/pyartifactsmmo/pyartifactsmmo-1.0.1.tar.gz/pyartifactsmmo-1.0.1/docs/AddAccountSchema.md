# AddAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Your desired username. | 
**password** | **str** | Your password. | 
**email** | **str** | Your email. | 

## Example

```python
from pyartifactsmmo.models.add_account_schema import AddAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddAccountSchema from a JSON string
add_account_schema_instance = AddAccountSchema.from_json(json)
# print the JSON string representation of the object
print(AddAccountSchema.to_json())

# convert the object into a dict
add_account_schema_dict = add_account_schema_instance.to_dict()
# create an instance of AddAccountSchema from a dict
add_account_schema_from_dict = AddAccountSchema.from_dict(add_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


