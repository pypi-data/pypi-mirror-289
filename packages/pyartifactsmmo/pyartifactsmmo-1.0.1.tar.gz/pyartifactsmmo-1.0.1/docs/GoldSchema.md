# GoldSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Quantity of gold. | 

## Example

```python
from pyartifactsmmo.models.gold_schema import GoldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GoldSchema from a JSON string
gold_schema_instance = GoldSchema.from_json(json)
# print the JSON string representation of the object
print(GoldSchema.to_json())

# convert the object into a dict
gold_schema_dict = gold_schema_instance.to_dict()
# create an instance of GoldSchema from a dict
gold_schema_from_dict = GoldSchema.from_dict(gold_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


