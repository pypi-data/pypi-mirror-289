# SingleItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**ItemSchema**](ItemSchema.md) | Item information. | 
**ge** | [**GEItemSchema**](GEItemSchema.md) |  | [optional] 

## Example

```python
from pyartifactsmmo.models.single_item_schema import SingleItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SingleItemSchema from a JSON string
single_item_schema_instance = SingleItemSchema.from_json(json)
# print the JSON string representation of the object
print(SingleItemSchema.to_json())

# convert the object into a dict
single_item_schema_dict = single_item_schema_instance.to_dict()
# create an instance of SingleItemSchema from a dict
single_item_schema_from_dict = SingleItemSchema.from_dict(single_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


