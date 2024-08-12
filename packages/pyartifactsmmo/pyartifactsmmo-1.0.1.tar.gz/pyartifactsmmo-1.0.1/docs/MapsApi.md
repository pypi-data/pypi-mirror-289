# pyartifactsmmo.MapsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_maps_maps_get**](MapsApi.md#get_all_maps_maps_get) | **GET** /maps/ | Get All Maps
[**get_map_maps_xy_get**](MapsApi.md#get_map_maps_xy_get) | **GET** /maps/{x}/{y} | Get Map


# **get_all_maps_maps_get**
> DataPageMapSchema get_all_maps_maps_get(content_type=content_type, content_code=content_code, page=page, size=size)

Get All Maps

Fetch maps details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_map_schema import DataPageMapSchema
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
    api_instance = pyartifactsmmo.MapsApi(api_client)
    content_type = 'content_type_example' # str | Type of content on the map. (optional)
    content_code = 'content_code_example' # str | Content code on the map. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Maps
        api_response = await api_instance.get_all_maps_maps_get(content_type=content_type, content_code=content_code, page=page, size=size)
        print("The response of MapsApi->get_all_maps_maps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_all_maps_maps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Type of content on the map. | [optional] 
 **content_code** | **str**| Content code on the map. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageMapSchema**](DataPageMapSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched maps details. |  -  |
**404** | Maps not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_maps_xy_get**
> MapResponseSchema get_map_maps_xy_get(x, y)

Get Map

Retrieve the details of a map.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.map_response_schema import MapResponseSchema
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
    api_instance = pyartifactsmmo.MapsApi(api_client)
    x = 56 # int | The position x of the map.
    y = 56 # int | The position X of the map.

    try:
        # Get Map
        api_response = await api_instance.get_map_maps_xy_get(x, y)
        print("The response of MapsApi->get_map_maps_xy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MapsApi->get_map_maps_xy_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **int**| The position x of the map. | 
 **y** | **int**| The position X of the map. | 

### Return type

[**MapResponseSchema**](MapResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched map. |  -  |
**404** | Map not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

