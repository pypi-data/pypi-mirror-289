# pyartifactsmmo.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events_events_get**](EventsApi.md#get_all_events_events_get) | **GET** /events/ | Get All Events


# **get_all_events_events_get**
> DataPageActiveEventSchema get_all_events_events_get(page=page, size=size)

Get All Events

Fetch events details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_active_event_schema import DataPageActiveEventSchema
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
    api_instance = pyartifactsmmo.EventsApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Events
        api_response = await api_instance.get_all_events_events_get(page=page, size=size)
        print("The response of EventsApi->get_all_events_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_all_events_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageActiveEventSchema**](DataPageActiveEventSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched events details. |  -  |
**404** | Events not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

