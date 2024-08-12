# pyartifactsmmo.MyAccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_my_change_password_post**](MyAccountApi.md#change_password_my_change_password_post) | **POST** /my/change_password | Change Password
[**get_bank_golds_my_bank_gold_get**](MyAccountApi.md#get_bank_golds_my_bank_gold_get) | **GET** /my/bank/gold | Get Bank Golds
[**get_bank_items_my_bank_items_get**](MyAccountApi.md#get_bank_items_my_bank_items_get) | **GET** /my/bank/items | Get Bank Items


# **change_password_my_change_password_post**
> ResponseSchema change_password_my_change_password_post(change_password)

Change Password

Change your account password. Changing the password reset the account token.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.change_password import ChangePassword
from pyartifactsmmo.models.response_schema import ResponseSchema
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
    api_instance = pyartifactsmmo.MyAccountApi(api_client)
    change_password = pyartifactsmmo.ChangePassword() # ChangePassword | 

    try:
        # Change Password
        api_response = await api_instance.change_password_my_change_password_post(change_password)
        print("The response of MyAccountApi->change_password_my_change_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->change_password_my_change_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password** | [**ChangePassword**](ChangePassword.md)|  | 

### Return type

[**ResponseSchema**](ResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully. |  -  |
**458** | Use a different password. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_golds_my_bank_gold_get**
> GoldBankResponseSchema get_bank_golds_my_bank_gold_get()

Get Bank Golds

Fetch golds in your bank.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.gold_bank_response_schema import GoldBankResponseSchema
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
    api_instance = pyartifactsmmo.MyAccountApi(api_client)

    try:
        # Get Bank Golds
        api_response = await api_instance.get_bank_golds_my_bank_gold_get()
        print("The response of MyAccountApi->get_bank_golds_my_bank_gold_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_bank_golds_my_bank_gold_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GoldBankResponseSchema**](GoldBankResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched golds. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_items_my_bank_items_get**
> DataPageSimpleItemSchema get_bank_items_my_bank_items_get(item_code=item_code, page=page, size=size)

Get Bank Items

Fetch all items in your bank.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_simple_item_schema import DataPageSimpleItemSchema
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
    api_instance = pyartifactsmmo.MyAccountApi(api_client)
    item_code = 'item_code_example' # str | Item to search in your bank. (optional)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get Bank Items
        api_response = await api_instance.get_bank_items_my_bank_items_get(item_code=item_code, page=page, size=size)
        print("The response of MyAccountApi->get_bank_items_my_bank_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountApi->get_bank_items_my_bank_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_code** | **str**| Item to search in your bank. | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageSimpleItemSchema**](DataPageSimpleItemSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched items. |  -  |
**404** | Items not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

