# CharacterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the character. | 
**skin** | **str** | Character skin code. | 
**level** | **int** | Combat level. | 
**xp** | **int** | The current xp level of the combat level. | 
**max_xp** | **int** | XP required to level up the character. | 
**total_xp** | **int** | Total XP of your character. | 
**gold** | **int** | The numbers of golds on this character. | 
**speed** | **int** | *Not available, on the roadmap. Character movement speed. | 
**mining_level** | **int** | Mining level. | 
**mining_xp** | **int** | The current xp level of the Mining skill. | 
**mining_max_xp** | **int** | Mining XP required to level up the skill. | 
**woodcutting_level** | **int** | Woodcutting level. | 
**woodcutting_xp** | **int** | The current xp level of the Woodcutting skill. | 
**woodcutting_max_xp** | **int** | Woodcutting XP required to level up the skill. | 
**fishing_level** | **int** | Fishing level. | 
**fishing_xp** | **int** | The current xp level of the Fishing skill. | 
**fishing_max_xp** | **int** | Fishing XP required to level up the skill. | 
**weaponcrafting_level** | **int** | Weaponcrafting level. | 
**weaponcrafting_xp** | **int** | The current xp level of the Weaponcrafting skill. | 
**weaponcrafting_max_xp** | **int** | Weaponcrafting XP required to level up the skill. | 
**gearcrafting_level** | **int** | Gearcrafting level. | 
**gearcrafting_xp** | **int** | The current xp level of the Gearcrafting skill. | 
**gearcrafting_max_xp** | **int** | Gearcrafting XP required to level up the skill. | 
**jewelrycrafting_level** | **int** | Jewelrycrafting level. | 
**jewelrycrafting_xp** | **int** | The current xp level of the Jewelrycrafting skill. | 
**jewelrycrafting_max_xp** | **int** | Jewelrycrafting XP required to level up the skill. | 
**cooking_level** | **int** | The current xp level of the Cooking skill. | 
**cooking_xp** | **int** | Cooking XP. | 
**cooking_max_xp** | **int** | Cooking XP required to level up the skill. | 
**hp** | **int** | Character HP. | 
**haste** | **int** | *Character Haste. Increase speed attack (reduce fight cooldown) | 
**critical_strike** | **int** | *Not available, on the roadmap. Character Critical   Strike. Critical strikes increase the attack&#39;s damage. | 
**stamina** | **int** | *Not available, on the roadmap. Regenerates life at the start of each turn. | 
**attack_fire** | **int** | Fire attack. | 
**attack_earth** | **int** | Earth attack. | 
**attack_water** | **int** | Water attack. | 
**attack_air** | **int** | Air attack. | 
**dmg_fire** | **int** | % Fire damage. | 
**dmg_earth** | **int** | % Earth damage. | 
**dmg_water** | **int** | % Water damage. | 
**dmg_air** | **int** | % Air damage. | 
**res_fire** | **int** | % Fire resistance. | 
**res_earth** | **int** | % Earth resistance. | 
**res_water** | **int** | % Water resistance. | 
**res_air** | **int** | % Air resistance. | 
**x** | **int** | Character x coordinate. | 
**y** | **int** | Character y coordinate. | 
**cooldown** | **int** | Cooldown in seconds. | 
**cooldown_expiration** | **datetime** | Datetime Cooldown expiration. | [optional] 
**weapon_slot** | **str** | Weapon slot. | 
**shield_slot** | **str** | Shield slot. | 
**helmet_slot** | **str** | Helmet slot. | 
**body_armor_slot** | **str** | Body armor slot. | 
**leg_armor_slot** | **str** | Leg armor slot. | 
**boots_slot** | **str** | Boots slot. | 
**ring1_slot** | **str** | Ring 1 slot. | 
**ring2_slot** | **str** | Ring 2 slot. | 
**amulet_slot** | **str** | Amulet slot. | 
**artifact1_slot** | **str** | Artifact 1 slot. | 
**artifact2_slot** | **str** | Artifact 2 slot. | 
**artifact3_slot** | **str** | Artifact 3 slot. | 
**consumable1_slot** | **str** | Consumable 1 slot. | 
**consumable1_slot_quantity** | **int** | Consumable 1 quantity. | 
**consumable2_slot** | **str** | Consumable 2 slot. | 
**consumable2_slot_quantity** | **int** | Consumable 2 quantity. | 
**task** | **str** | Task in progress. | 
**task_type** | **str** | Task type. | 
**task_progress** | **int** | Task progression. | 
**task_total** | **int** | Task total objective. | 
**inventory_max_items** | **int** | Inventory max items. | 
**inventory** | [**List[InventorySlot]**](InventorySlot.md) | List of inventory slots. | [optional] 

## Example

```python
from pyartifactsmmo.models.character_schema import CharacterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterSchema from a JSON string
character_schema_instance = CharacterSchema.from_json(json)
# print the JSON string representation of the object
print(CharacterSchema.to_json())

# convert the object into a dict
character_schema_dict = character_schema_instance.to_dict()
# create an instance of CharacterSchema from a dict
character_schema_from_dict = CharacterSchema.from_dict(character_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


