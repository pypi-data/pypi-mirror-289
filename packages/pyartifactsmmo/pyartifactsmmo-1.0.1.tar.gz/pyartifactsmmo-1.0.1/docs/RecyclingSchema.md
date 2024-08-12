# RecyclingSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**quantity** | **int** | Quantity of items to recycle. | [optional] [default to 1]

## Example

```python
from pyartifactsmmo.models.recycling_schema import RecyclingSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RecyclingSchema from a JSON string
recycling_schema_instance = RecyclingSchema.from_json(json)
# print the JSON string representation of the object
print(RecyclingSchema.to_json())

# convert the object into a dict
recycling_schema_dict = recycling_schema_instance.to_dict()
# create an instance of RecyclingSchema from a dict
recycling_schema_from_dict = RecyclingSchema.from_dict(recycling_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


