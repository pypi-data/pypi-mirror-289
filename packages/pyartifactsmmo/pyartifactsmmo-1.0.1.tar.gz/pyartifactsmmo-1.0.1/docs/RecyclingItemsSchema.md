# RecyclingItemsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DropSchema]**](DropSchema.md) | Objects received. | 

## Example

```python
from pyartifactsmmo.models.recycling_items_schema import RecyclingItemsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RecyclingItemsSchema from a JSON string
recycling_items_schema_instance = RecyclingItemsSchema.from_json(json)
# print the JSON string representation of the object
print(RecyclingItemsSchema.to_json())

# convert the object into a dict
recycling_items_schema_dict = recycling_items_schema_instance.to_dict()
# create an instance of RecyclingItemsSchema from a dict
recycling_items_schema_from_dict = RecyclingItemsSchema.from_dict(recycling_items_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


