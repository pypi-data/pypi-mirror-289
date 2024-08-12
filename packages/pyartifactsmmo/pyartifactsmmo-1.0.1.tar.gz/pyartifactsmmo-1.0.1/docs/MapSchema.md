# MapSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the map. | 
**skin** | **str** | Skin of the map. | 
**x** | **int** | Position X of the map. | 
**y** | **int** | Position Y of the map. | 
**content** | [**MapContentSchema**](MapContentSchema.md) |  | 

## Example

```python
from pyartifactsmmo.models.map_schema import MapSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MapSchema from a JSON string
map_schema_instance = MapSchema.from_json(json)
# print the JSON string representation of the object
print(MapSchema.to_json())

# convert the object into a dict
map_schema_dict = map_schema_instance.to_dict()
# create an instance of MapSchema from a dict
map_schema_from_dict = MapSchema.from_dict(map_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


