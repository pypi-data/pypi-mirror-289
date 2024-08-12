# pyartifactsmmo.MonstersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_monsters_monsters_get**](MonstersApi.md#get_all_monsters_monsters_get) | **GET** /monsters/ | Get All Monsters
[**get_monster_monsters_code_get**](MonstersApi.md#get_monster_monsters_code_get) | **GET** /monsters/{code} | Get Monster


# **get_all_monsters_monsters_get**
> DataPageMonsterSchema get_all_monsters_monsters_get(min_level=min_level, max_level=max_level, drop=drop, page=page, size=size)

Get All Monsters

Fetch monsters details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_monster_schema import DataPageMonsterSchema
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
    api_instance = pyartifactsmmo.MonstersApi(api_client)
    min_level = 56 # int | Monster minimum level. (optional)
    max_level = 56 # int | Monster maximum level. (optional)
    drop = 'green_slimeball' # str | Item code of the drop. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Monsters
        api_response = await api_instance.get_all_monsters_monsters_get(min_level=min_level, max_level=max_level, drop=drop, page=page, size=size)
        print("The response of MonstersApi->get_all_monsters_monsters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonstersApi->get_all_monsters_monsters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | **int**| Monster minimum level. | [optional] 
 **max_level** | **int**| Monster maximum level. | [optional] 
 **drop** | **str**| Item code of the drop. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageMonsterSchema**](DataPageMonsterSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched monsters details. |  -  |
**404** | Monsters not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monster_monsters_code_get**
> MonsterResponseSchema get_monster_monsters_code_get(code)

Get Monster

Retrieve the details of a monster.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.monster_response_schema import MonsterResponseSchema
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
    api_instance = pyartifactsmmo.MonstersApi(api_client)
    code = 'red_slime' # str | The code of the monster.

    try:
        # Get Monster
        api_response = await api_instance.get_monster_monsters_code_get(code)
        print("The response of MonstersApi->get_monster_monsters_code_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonstersApi->get_monster_monsters_code_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the monster. | 

### Return type

[**MonsterResponseSchema**](MonsterResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched monster. |  -  |
**404** | Monster not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

