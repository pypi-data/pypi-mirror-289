# EquipSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**slot** | **str** | Item slot. | 

## Example

```python
from pyartifactsmmo.models.equip_schema import EquipSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EquipSchema from a JSON string
equip_schema_instance = EquipSchema.from_json(json)
# print the JSON string representation of the object
print(EquipSchema.to_json())

# convert the object into a dict
equip_schema_dict = equip_schema_instance.to_dict()
# create an instance of EquipSchema from a dict
equip_schema_from_dict = EquipSchema.from_dict(equip_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


