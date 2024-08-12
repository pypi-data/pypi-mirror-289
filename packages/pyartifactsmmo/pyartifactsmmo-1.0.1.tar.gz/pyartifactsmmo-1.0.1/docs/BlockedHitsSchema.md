# BlockedHitsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fire** | **int** | The amount of fire hits blocked. | 
**earth** | **int** | The amount of earth hits blocked. | 
**water** | **int** | The amount of water hits blocked. | 
**air** | **int** | The amount of air hits blocked. | 
**total** | **int** | The amount of total hits blocked. | 

## Example

```python
from pyartifactsmmo.models.blocked_hits_schema import BlockedHitsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BlockedHitsSchema from a JSON string
blocked_hits_schema_instance = BlockedHitsSchema.from_json(json)
# print the JSON string representation of the object
print(BlockedHitsSchema.to_json())

# convert the object into a dict
blocked_hits_schema_dict = blocked_hits_schema_instance.to_dict()
# create an instance of BlockedHitsSchema from a dict
blocked_hits_schema_from_dict = BlockedHitsSchema.from_dict(blocked_hits_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


