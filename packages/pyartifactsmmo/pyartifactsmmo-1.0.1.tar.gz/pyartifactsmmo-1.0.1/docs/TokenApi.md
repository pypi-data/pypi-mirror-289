# pyartifactsmmo.TokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token_token_post**](TokenApi.md#generate_token_token_post) | **POST** /token/ | Generate Token


# **generate_token_token_post**
> TokenResponseSchema generate_token_token_post()

Generate Token

Use your account as HTTPBasic Auth to generate your token to use the API. You can also generate your token directly on the website.

### Example

* Basic Authentication (HTTPBasic):

```python
import pyartifactsmmo
from pyartifactsmmo.models.token_response_schema import TokenResponseSchema
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

# Configure HTTP basic authorization: HTTPBasic
configuration = pyartifactsmmo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with pyartifactsmmo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyartifactsmmo.TokenApi(api_client)

    try:
        # Generate Token
        api_response = await api_instance.generate_token_token_post()
        print("The response of TokenApi->generate_token_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->generate_token_token_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenResponseSchema**](TokenResponseSchema.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token generated successfully |  -  |
**455** | Token generation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

