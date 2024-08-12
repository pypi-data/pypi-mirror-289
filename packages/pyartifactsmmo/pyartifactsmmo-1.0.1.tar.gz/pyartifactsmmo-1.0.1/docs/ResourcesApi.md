# pyartifactsmmo.ResourcesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_resources_resources_get**](ResourcesApi.md#get_all_resources_resources_get) | **GET** /resources/ | Get All Resources
[**get_resource_resources_code_get**](ResourcesApi.md#get_resource_resources_code_get) | **GET** /resources/{code} | Get Resource


# **get_all_resources_resources_get**
> DataPageResourceSchema get_all_resources_resources_get(min_level=min_level, max_level=max_level, skill=skill, drop=drop, page=page, size=size)

Get All Resources

Fetch resources details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_resource_schema import DataPageResourceSchema
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
    api_instance = pyartifactsmmo.ResourcesApi(api_client)
    min_level = 56 # int | Skill minimum level. (optional)
    max_level = 56 # int | Skill maximum level. (optional)
    skill = 'skill_example' # str | The code of the skill. (optional)
    drop = 'copper_ore' # str | Item code of the drop. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Resources
        api_response = await api_instance.get_all_resources_resources_get(min_level=min_level, max_level=max_level, skill=skill, drop=drop, page=page, size=size)
        print("The response of ResourcesApi->get_all_resources_resources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_all_resources_resources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | **int**| Skill minimum level. | [optional] 
 **max_level** | **int**| Skill maximum level. | [optional] 
 **skill** | **str**| The code of the skill. | [optional] 
 **drop** | **str**| Item code of the drop. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageResourceSchema**](DataPageResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched resources details. |  -  |
**404** | Resources not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_resources_code_get**
> ResourceResponseSchema get_resource_resources_code_get(code)

Get Resource

Retrieve the details of a resource.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.resource_response_schema import ResourceResponseSchema
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
    api_instance = pyartifactsmmo.ResourcesApi(api_client)
    code = 'copper_rocks' # str | The code of the resource.

    try:
        # Get Resource
        api_response = await api_instance.get_resource_resources_code_get(code)
        print("The response of ResourcesApi->get_resource_resources_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourcesApi->get_resource_resources_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the resource. | 

### Return type

[**ResourceResponseSchema**](ResourceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched resource. |  -  |
**404** | Ressource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

