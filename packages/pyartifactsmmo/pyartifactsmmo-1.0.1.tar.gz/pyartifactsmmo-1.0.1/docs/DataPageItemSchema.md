# DataPageItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ItemSchema]**](ItemSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_item_schema import DataPageItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageItemSchema from a JSON string
data_page_item_schema_instance = DataPageItemSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageItemSchema.to_json())

# convert the object into a dict
data_page_item_schema_dict = data_page_item_schema_instance.to_dict()
# create an instance of DataPageItemSchema from a dict
data_page_item_schema_from_dict = DataPageItemSchema.from_dict(data_page_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


