# SimpleItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**quantity** | **int** | Item quantity. | 

## Example

```python
from pyartifactsmmo.models.simple_item_schema import SimpleItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleItemSchema from a JSON string
simple_item_schema_instance = SimpleItemSchema.from_json(json)
# print the JSON string representation of the object
print(SimpleItemSchema.to_json())

# convert the object into a dict
simple_item_schema_dict = simple_item_schema_instance.to_dict()
# create an instance of SimpleItemSchema from a dict
simple_item_schema_from_dict = SimpleItemSchema.from_dict(simple_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


