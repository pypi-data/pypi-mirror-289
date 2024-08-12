# EquipRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**CooldownSchema**](CooldownSchema.md) | Cooldown details. | 
**slot** | **str** | Item slot. | 
**item** | [**ItemSchema**](ItemSchema.md) | Item details. | 
**character** | [**CharacterSchema**](CharacterSchema.md) | Player details. | 

## Example

```python
from pyartifactsmmo.models.equip_request_schema import EquipRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EquipRequestSchema from a JSON string
equip_request_schema_instance = EquipRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EquipRequestSchema.to_json())

# convert the object into a dict
equip_request_schema_dict = equip_request_schema_instance.to_dict()
# create an instance of EquipRequestSchema from a dict
equip_request_schema_from_dict = EquipRequestSchema.from_dict(equip_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


