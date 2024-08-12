# DataPageLogSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LogSchema]**](LogSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_log_schema import DataPageLogSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageLogSchema from a JSON string
data_page_log_schema_instance = DataPageLogSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageLogSchema.to_json())

# convert the object into a dict
data_page_log_schema_dict = data_page_log_schema_instance.to_dict()
# create an instance of DataPageLogSchema from a dict
data_page_log_schema_from_dict = DataPageLogSchema.from_dict(data_page_log_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


