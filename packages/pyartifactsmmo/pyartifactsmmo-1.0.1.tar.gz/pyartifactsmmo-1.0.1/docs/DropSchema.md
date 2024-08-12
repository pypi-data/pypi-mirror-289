# DropSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the item. | 
**quantity** | **int** | The quantity of the item. | 

## Example

```python
from pyartifactsmmo.models.drop_schema import DropSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DropSchema from a JSON string
drop_schema_instance = DropSchema.from_json(json)
# print the JSON string representation of the object
print(DropSchema.to_json())

# convert the object into a dict
drop_schema_dict = drop_schema_instance.to_dict()
# create an instance of DropSchema from a dict
drop_schema_from_dict = DropSchema.from_dict(drop_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


