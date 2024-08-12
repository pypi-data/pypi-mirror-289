# AddCharacterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Your desired character name. It&#39;s unique and all players can see it. | 
**skin** | **str** | Your desired skin. | 

## Example

```python
from pyartifactsmmo.models.add_character_schema import AddCharacterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddCharacterSchema from a JSON string
add_character_schema_instance = AddCharacterSchema.from_json(json)
# print the JSON string representation of the object
print(AddCharacterSchema.to_json())

# convert the object into a dict
add_character_schema_dict = add_character_schema_instance.to_dict()
# create an instance of AddCharacterSchema from a dict
add_character_schema_from_dict = AddCharacterSchema.from_dict(add_character_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


