# DataPageMonsterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MonsterSchema]**](MonsterSchema.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**size** | **int** |  | 
**pages** | **int** |  | [optional] 

## Example

```python
from pyartifactsmmo.models.data_page_monster_schema import DataPageMonsterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataPageMonsterSchema from a JSON string
data_page_monster_schema_instance = DataPageMonsterSchema.from_json(json)
# print the JSON string representation of the object
print(DataPageMonsterSchema.to_json())

# convert the object into a dict
data_page_monster_schema_dict = data_page_monster_schema_instance.to_dict()
# create an instance of DataPageMonsterSchema from a dict
data_page_monster_schema_from_dict = DataPageMonsterSchema.from_dict(data_page_monster_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


