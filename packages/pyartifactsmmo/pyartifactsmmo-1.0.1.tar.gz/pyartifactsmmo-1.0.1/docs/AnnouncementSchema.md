# AnnouncementSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Announcement text. | 
**created_at** | **datetime** | Datetime of the announcement. | [optional] 

## Example

```python
from pyartifactsmmo.models.announcement_schema import AnnouncementSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementSchema from a JSON string
announcement_schema_instance = AnnouncementSchema.from_json(json)
# print the JSON string representation of the object
print(AnnouncementSchema.to_json())

# convert the object into a dict
announcement_schema_dict = announcement_schema_instance.to_dict()
# create an instance of AnnouncementSchema from a dict
announcement_schema_from_dict = AnnouncementSchema.from_dict(announcement_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


