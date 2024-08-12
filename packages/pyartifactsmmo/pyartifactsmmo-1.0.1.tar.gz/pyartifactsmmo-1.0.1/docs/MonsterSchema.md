# MonsterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the monster. | 
**code** | **str** | The code of the monster. This is the monster&#39;s unique identifier (ID). | 
**level** | **int** | Monster level. | 
**hp** | **int** | Monster hit points. | 
**attack_fire** | **int** | Monster fire attack. | 
**attack_earth** | **int** | Monster earth attack. | 
**attack_water** | **int** | Monster water attack. | 
**attack_air** | **int** | Monster air attack. | 
**res_fire** | **int** | Monster % fire resistance. | 
**res_earth** | **int** | Monster % earth resistance. | 
**res_water** | **int** | Monster % water resistance. | 
**res_air** | **int** | Monster % air resistance. | 
**min_gold** | **int** | Monster minimum gold drop.  | 
**max_gold** | **int** | Monster maximum gold drop.  | 
**drops** | [**List[DropRateSchema]**](DropRateSchema.md) | Monster drops. This is a list of items that the monster drops after killing the monster.  | 

## Example

```python
from pyartifactsmmo.models.monster_schema import MonsterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MonsterSchema from a JSON string
monster_schema_instance = MonsterSchema.from_json(json)
# print the JSON string representation of the object
print(MonsterSchema.to_json())

# convert the object into a dict
monster_schema_dict = monster_schema_instance.to_dict()
# create an instance of MonsterSchema from a dict
monster_schema_from_dict = MonsterSchema.from_dict(monster_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


