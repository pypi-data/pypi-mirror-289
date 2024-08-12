# DataPageMapSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MapSchema]**](MapSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_map_schema import DataPageMapSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageMapSchema from a JSON string
data_page_map_schema_instance = DataPageMapSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageMapSchema.to_json())

# convert the object into a dict
data_page_map_schema_dict = data_page_map_schema_instance.to_dict()
# create an instance of DataPageMapSchema from a dict
data_page_map_schema_from_dict = DataPageMapSchema.from_dict(data_page_map_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


