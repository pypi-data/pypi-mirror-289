# RecyclingDataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**details** | [**RecyclingItemsSchema**](RecyclingItemsSchema.md) | Craft details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.recycling_data_schema import RecyclingDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RecyclingDataSchema from a JSON string
recycling_data_schema_instance = RecyclingDataSchema.from_json(json)
# print the JSON string representation of the object
print(RecyclingDataSchema.to_json())

# convert the object into a dict
recycling_data_schema_dict = recycling_data_schema_instance.to_dict()
# create an instance of RecyclingDataSchema from a dict
recycling_data_schema_from_dict = RecyclingDataSchema.from_dict(recycling_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


