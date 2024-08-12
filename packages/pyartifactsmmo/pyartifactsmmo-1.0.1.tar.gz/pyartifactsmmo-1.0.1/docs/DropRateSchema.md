# DropRateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Item code. | 
**rate** | **int** | Chance rate. | 
**min_quantity** | **int** | Minimum quantity. | 
**max_quantity** | **int** | Maximum quantity. | 

## Example

```python
from pyartifactsmmo.models.drop_rate_schema import DropRateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DropRateSchema from a JSON string
drop_rate_schema_instance = DropRateSchema.from_json(json)
# print the JSON string representation of the object
print(DropRateSchema.to_json())

# convert the object into a dict
drop_rate_schema_dict = drop_rate_schema_instance.to_dict()
# create an instance of DropRateSchema from a dict
drop_rate_schema_from_dict = DropRateSchema.from_dict(drop_rate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


