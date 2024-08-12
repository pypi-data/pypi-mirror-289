# EquipmentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EquipRequestSchema**](EquipRequestSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.equipment_response_schema import EquipmentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EquipmentResponseSchema from a JSON string
equipment_response_schema_instance = EquipmentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EquipmentResponseSchema.to_json())

# convert the object into a dict
equipment_response_schema_dict = equipment_response_schema_instance.to_dict()
# create an instance of EquipmentResponseSchema from a dict
equipment_response_schema_from_dict = EquipmentResponseSchema.from_dict(equipment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


