# UnequipSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **str** | Item slot. | 

## Example

```python
from pyartifactsmmo.models.unequip_schema import UnequipSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnequipSchema from a JSON string
unequip_schema_instance = UnequipSchema.from_json(json)
# print the JSON string representation of the object
print(UnequipSchema.to_json())

# convert the object into a dict
unequip_schema_dict = unequip_schema_instance.to_dict()
# create an instance of UnequipSchema from a dict
unequip_schema_from_dict = UnequipSchema.from_dict(unequip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


