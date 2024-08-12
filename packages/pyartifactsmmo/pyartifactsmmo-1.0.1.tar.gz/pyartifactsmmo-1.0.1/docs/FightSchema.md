# FightSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xp** | **int** | The amount of xp gained by the fight. | 
**gold** | **int** | The amount of gold gained by the fight. | 
**drops** | [**List[DropSchema]**](DropSchema.md) | The items dropped by the fight. | 
**turns** | **int** | Numbers of the turns of the combat. | 
**monster_blocked_hits** | [**BlockedHitsSchema**](BlockedHitsSchema.md) | The amount of blocked hits by the monster. | 
**player_blocked_hits** | [**BlockedHitsSchema**](BlockedHitsSchema.md) | The amount of blocked hits by the player. | 
**logs** | **List[str]** | The fight logs. | 
**result** | **str** | The result of the fight. | 

## Example

```python
from pyartifactsmmo.models.fight_schema import FightSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FightSchema from a JSON string
fight_schema_instance = FightSchema.from_json(json)
# print the JSON string representation of the object
print(FightSchema.to_json())

# convert the object into a dict
fight_schema_dict = fight_schema_instance.to_dict()
# create an instance of FightSchema from a dict
fight_schema_from_dict = FightSchema.from_dict(fight_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


