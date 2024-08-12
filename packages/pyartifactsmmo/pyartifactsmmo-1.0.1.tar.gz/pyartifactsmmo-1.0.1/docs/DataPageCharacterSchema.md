# DataPageCharacterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterSchema]**](CharacterSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_character_schema import DataPageCharacterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageCharacterSchema from a JSON string
data_page_character_schema_instance = DataPageCharacterSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageCharacterSchema.to_json())

# convert the object into a dict
data_page_character_schema_dict = data_page_character_schema_instance.to_dict()
# create an instance of DataPageCharacterSchema from a dict
data_page_character_schema_from_dict = DataPageCharacterSchema.from_dict(data_page_character_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


