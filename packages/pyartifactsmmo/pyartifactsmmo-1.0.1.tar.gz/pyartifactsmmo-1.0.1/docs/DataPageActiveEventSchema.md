# DataPageActiveEventSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActiveEventSchema]**](ActiveEventSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_active_event_schema import DataPageActiveEventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageActiveEventSchema from a JSON string
data_page_active_event_schema_instance = DataPageActiveEventSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageActiveEventSchema.to_json())

# convert the object into a dict
data_page_active_event_schema_dict = data_page_active_event_schema_instance.to_dict()
# create an instance of DataPageActiveEventSchema from a dict
data_page_active_event_schema_from_dict = DataPageActiveEventSchema.from_dict(data_page_active_event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


