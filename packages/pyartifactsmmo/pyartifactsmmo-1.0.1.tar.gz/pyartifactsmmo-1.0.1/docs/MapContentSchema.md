# MapContentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the content. | 
**code** | **str** | Code of the content. | 

## Example

```python
from pyartifactsmmo.models.map_content_schema import MapContentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MapContentSchema from a JSON string
map_content_schema_instance = MapContentSchema.from_json(json)
# print the JSON string representation of the object
print(MapContentSchema.to_json())

# convert the object into a dict
map_content_schema_dict = map_content_schema_instance.to_dict()
# create an instance of MapContentSchema from a dict
map_content_schema_from_dict = MapContentSchema.from_dict(map_content_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


