# ResourceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the resource | 
**code** | **str** | The code of the resource. This is the resource&#39;s unique identifier (ID). | 
**skill** | **str** | The skill required to gather this resource. | 
**level** | **int** | The skill level required to gather this resource. | 
**drops** | [**List[DropRateSchema]**](DropRateSchema.md) | The drops of this resource. | 

## Example

```python
from pyartifactsmmo.models.resource_schema import ResourceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSchema from a JSON string
resource_schema_instance = ResourceSchema.from_json(json)
# print the JSON string representation of the object
print(ResourceSchema.to_json())

# convert the object into a dict
resource_schema_dict = resource_schema_instance.to_dict()
# create an instance of ResourceSchema from a dict
resource_schema_from_dict = ResourceSchema.from_dict(resource_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


