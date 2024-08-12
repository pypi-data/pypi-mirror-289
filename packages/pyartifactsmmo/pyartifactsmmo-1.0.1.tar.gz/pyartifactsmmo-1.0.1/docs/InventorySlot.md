# InventorySlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot** | **int** | Inventory slot identifier. | 
**code** | **str** | Item code. | 
**quantity** | **int** | Quantity in the slot. | 

## Example

```python
from pyartifactsmmo.models.inventory_slot import InventorySlot

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySlot from a JSON string
inventory_slot_instance = InventorySlot.from_json(json)
# print the JSON string representation of the object
print(InventorySlot.to_json())

# convert the object into a dict
inventory_slot_dict = inventory_slot_instance.to_dict()
# create an instance of InventorySlot from a dict
inventory_slot_from_dict = InventorySlot.from_dict(inventory_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


