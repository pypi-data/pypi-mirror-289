# pyartifactsmmo.GrandExchangeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ge_items_ge_get**](GrandExchangeApi.md#get_all_ge_items_ge_get) | **GET** /ge/ | Get All Ge Items
[**get_ge_item_ge_code_get**](GrandExchangeApi.md#get_ge_item_ge_code_get) | **GET** /ge/{code} | Get Ge Item


# **get_all_ge_items_ge_get**
> DataPageGEItemSchema get_all_ge_items_ge_get(page=page, size=size)

Get All Ge Items

Fetch Grand Exchange items details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_ge_item_schema import DataPageGEItemSchema
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
    api_instance = pyartifactsmmo.GrandExchangeApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Ge Items
        api_response = await api_instance.get_all_ge_items_ge_get(page=page, size=size)
        print("The response of GrandExchangeApi->get_all_ge_items_ge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrandExchangeApi->get_all_ge_items_ge_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageGEItemSchema**](DataPageGEItemSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetch Grand Exchange items details. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ge_item_ge_code_get**
> GEItemResponseSchema get_ge_item_ge_code_get(code)

Get Ge Item

Retrieve the details of a Grand Exchange item.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.ge_item_response_schema import GEItemResponseSchema
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
    api_instance = pyartifactsmmo.GrandExchangeApi(api_client)
    code = 'code_example' # str | The code of the item.

    try:
        # Get Ge Item
        api_response = await api_instance.get_ge_item_ge_code_get(code)
        print("The response of GrandExchangeApi->get_ge_item_ge_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrandExchangeApi->get_ge_item_ge_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the item. | 

### Return type

[**GEItemResponseSchema**](GEItemResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Grand Exchange item. |  -  |
**404** | Item not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

