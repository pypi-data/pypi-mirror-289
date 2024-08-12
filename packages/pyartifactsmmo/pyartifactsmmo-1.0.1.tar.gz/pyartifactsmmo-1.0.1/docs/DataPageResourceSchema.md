# DataPageResourceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceSchema]**](ResourceSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_resource_schema import DataPageResourceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageResourceSchema from a JSON string
data_page_resource_schema_instance = DataPageResourceSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageResourceSchema.to_json())

# convert the object into a dict
data_page_resource_schema_dict = data_page_resource_schema_instance.to_dict()
# create an instance of DataPageResourceSchema from a dict
data_page_resource_schema_from_dict = DataPageResourceSchema.from_dict(data_page_resource_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


