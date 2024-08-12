# MyCharactersListSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CharacterSchema]**](CharacterSchema.md) | List of your characters. | 

## Example

```python
from pyartifactsmmo.models.my_characters_list_schema import MyCharactersListSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MyCharactersListSchema from a JSON string
my_characters_list_schema_instance = MyCharactersListSchema.from_json(json)
# print the JSON string representation of the object
print(MyCharactersListSchema.to_json())

# convert the object into a dict
my_characters_list_schema_dict = my_characters_list_schema_instance.to_dict()
# create an instance of MyCharactersListSchema from a dict
my_characters_list_schema_from_dict = MyCharactersListSchema.from_dict(my_characters_list_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


