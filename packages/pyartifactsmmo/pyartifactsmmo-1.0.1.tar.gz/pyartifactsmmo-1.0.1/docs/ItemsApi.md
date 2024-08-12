# pyartifactsmmo.ItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_items_get**](ItemsApi.md#get_all_items_items_get) | **GET** /items/ | Get All Items
[**get_item_items_code_get**](ItemsApi.md#get_item_items_code_get) | **GET** /items/{code} | Get Item


# **get_all_items_items_get**
> DataPageItemSchema get_all_items_items_get(min_level=min_level, max_level=max_level, name=name, type=type, craft_skill=craft_skill, craft_material=craft_material, page=page, size=size)

Get All Items

Fetch items details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_item_schema import DataPageItemSchema
from pyartifactsmmo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyartifactsmmo.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyartifactsmmo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyartifactsmmo.ItemsApi(api_client)
    min_level = 56 # int | Minimum level items. (optional)
    max_level = 56 # int | Maximum level items. (optional)
    name = 'name_example' # str | Name of the item. (optional)
    type = 'type_example' # str | Type of items. (optional)
    craft_skill = 'craft_skill_example' # str | Skill to craft items. (optional)
    craft_material = 'craft_material_example' # str | Item code of items used as material for crafting. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Items
        api_response = await api_instance.get_all_items_items_get(min_level=min_level, max_level=max_level, name=name, type=type, craft_skill=craft_skill, craft_material=craft_material, page=page, size=size)
        print("The response of ItemsApi->get_all_items_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_all_items_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | **int**| Minimum level items. | [optional] 
 **max_level** | **int**| Maximum level items. | [optional] 
 **name** | **str**| Name of the item. | [optional] 
 **type** | **str**| Type of items. | [optional] 
 **craft_skill** | **str**| Skill to craft items. | [optional] 
 **craft_material** | **str**| Item code of items used as material for crafting. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageItemSchema**](DataPageItemSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetch items details. |  -  |
**404** | Items not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_items_code_get**
> ItemResponseSchema get_item_items_code_get(code)

Get Item

Retrieve the details of a item.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.item_response_schema import ItemResponseSchema
from pyartifactsmmo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyartifactsmmo.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyartifactsmmo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyartifactsmmo.ItemsApi(api_client)
    code = 'code_example' # str | The code of the item.

    try:
        # Get Item
        api_response = await api_instance.get_item_items_code_get(code)
        print("The response of ItemsApi->get_item_items_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->get_item_items_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the item. | 

### Return type

[**ItemResponseSchema**](ItemResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched item. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

