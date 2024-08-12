# pyartifactsmmo.CharactersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_character_characters_create_post**](CharactersApi.md#create_character_characters_create_post) | **POST** /characters/create | Create Character
[**delete_character_characters_delete_post**](CharactersApi.md#delete_character_characters_delete_post) | **POST** /characters/delete | Delete Character
[**get_all_characters_characters_get**](CharactersApi.md#get_all_characters_characters_get) | **GET** /characters/ | Get All Characters
[**get_character_characters_name_get**](CharactersApi.md#get_character_characters_name_get) | **GET** /characters/{name} | Get Character


# **create_character_characters_create_post**
> CharacterResponseSchema create_character_characters_create_post(add_character_schema)

Create Character

Create new character on your account. You can create up to 5 characters.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.add_character_schema import AddCharacterSchema
from pyartifactsmmo.models.character_response_schema import CharacterResponseSchema
from pyartifactsmmo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyartifactsmmo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = pyartifactsmmo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyartifactsmmo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyartifactsmmo.CharactersApi(api_client)
    add_character_schema = pyartifactsmmo.AddCharacterSchema() # AddCharacterSchema | 

    try:
        # Create Character
        api_response = await api_instance.create_character_characters_create_post(add_character_schema)
        print("The response of CharactersApi->create_character_characters_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->create_character_characters_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_character_schema** | [**AddCharacterSchema**](AddCharacterSchema.md)|  | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created character. |  -  |
**494** | Name already used. |  -  |
**495** | Maximum characters reached on your account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_character_characters_delete_post**
> CharacterResponseSchema delete_character_characters_delete_post(delete_character_schema)

Delete Character

Delete character on your account.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.character_response_schema import CharacterResponseSchema
from pyartifactsmmo.models.delete_character_schema import DeleteCharacterSchema
from pyartifactsmmo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyartifactsmmo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = pyartifactsmmo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with pyartifactsmmo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyartifactsmmo.CharactersApi(api_client)
    delete_character_schema = pyartifactsmmo.DeleteCharacterSchema() # DeleteCharacterSchema | 

    try:
        # Delete Character
        api_response = await api_instance.delete_character_characters_delete_post(delete_character_schema)
        print("The response of CharactersApi->delete_character_characters_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->delete_character_characters_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_character_schema** | [**DeleteCharacterSchema**](DeleteCharacterSchema.md)|  | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted character. |  -  |
**498** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_characters_characters_get**
> DataPageCharacterSchema get_all_characters_characters_get(sort=sort, page=page, size=size)

Get All Characters

Fetch characters details.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_character_schema import DataPageCharacterSchema
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
    api_instance = pyartifactsmmo.CharactersApi(api_client)
    sort = 'sort_example' # str | Default sort by combat total XP. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Characters
        api_response = await api_instance.get_all_characters_characters_get(sort=sort, page=page, size=size)
        print("The response of CharactersApi->get_all_characters_characters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_all_characters_characters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Default sort by combat total XP. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageCharacterSchema**](DataPageCharacterSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched characters details. |  -  |
**404** | Characters not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_characters_name_get**
> CharacterResponseSchema get_character_characters_name_get(name)

Get Character

Retrieve the details of a character.

### Example


```python
import pyartifactsmmo
from pyartifactsmmo.models.character_response_schema import CharacterResponseSchema
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
    api_instance = pyartifactsmmo.CharactersApi(api_client)
    name = 'name_example' # str | The character name.

    try:
        # Get Character
        api_response = await api_instance.get_character_characters_name_get(name)
        print("The response of CharactersApi->get_character_characters_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CharactersApi->get_character_characters_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The character name. | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched character. |  -  |
**404** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

