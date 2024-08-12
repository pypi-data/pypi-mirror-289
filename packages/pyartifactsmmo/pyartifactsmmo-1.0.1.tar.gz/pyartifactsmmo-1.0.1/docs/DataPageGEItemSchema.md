# DataPageGEItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GEItemSchema]**](GEItemSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_ge_item_schema import DataPageGEItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageGEItemSchema from a JSON string
data_page_ge_item_schema_instance = DataPageGEItemSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageGEItemSchema.to_json())

# convert the object into a dict
data_page_ge_item_schema_dict = data_page_ge_item_schema_instance.to_dict()
# create an instance of DataPageGEItemSchema from a dict
data_page_ge_item_schema_from_dict = DataPageGEItemSchema.from_dict(data_page_ge_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


