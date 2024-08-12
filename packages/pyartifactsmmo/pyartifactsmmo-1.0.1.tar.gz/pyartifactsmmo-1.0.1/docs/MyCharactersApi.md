# pyartifactsmmo.MyCharactersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_accept_new_task_my_name_action_task_new_post**](MyCharactersApi.md#action_accept_new_task_my_name_action_task_new_post) | **POST** /my/{name}/action/task/new | Action Accept New Task
[**action_complete_task_my_name_action_task_complete_post**](MyCharactersApi.md#action_complete_task_my_name_action_task_complete_post) | **POST** /my/{name}/action/task/complete | Action Complete Task
[**action_crafting_my_name_action_crafting_post**](MyCharactersApi.md#action_crafting_my_name_action_crafting_post) | **POST** /my/{name}/action/crafting | Action Crafting
[**action_delete_item_my_name_action_delete_post**](MyCharactersApi.md#action_delete_item_my_name_action_delete_post) | **POST** /my/{name}/action/delete | Action Delete Item
[**action_deposit_bank_gold_my_name_action_bank_deposit_gold_post**](MyCharactersApi.md#action_deposit_bank_gold_my_name_action_bank_deposit_gold_post) | **POST** /my/{name}/action/bank/deposit/gold | Action Deposit Bank Gold
[**action_deposit_bank_my_name_action_bank_deposit_post**](MyCharactersApi.md#action_deposit_bank_my_name_action_bank_deposit_post) | **POST** /my/{name}/action/bank/deposit | Action Deposit Bank
[**action_equip_item_my_name_action_equip_post**](MyCharactersApi.md#action_equip_item_my_name_action_equip_post) | **POST** /my/{name}/action/equip | Action Equip Item
[**action_fight_my_name_action_fight_post**](MyCharactersApi.md#action_fight_my_name_action_fight_post) | **POST** /my/{name}/action/fight | Action Fight
[**action_gathering_my_name_action_gathering_post**](MyCharactersApi.md#action_gathering_my_name_action_gathering_post) | **POST** /my/{name}/action/gathering | Action Gathering
[**action_ge_buy_item_my_name_action_ge_buy_post**](MyCharactersApi.md#action_ge_buy_item_my_name_action_ge_buy_post) | **POST** /my/{name}/action/ge/buy | Action Ge Buy Item
[**action_ge_sell_item_my_name_action_ge_sell_post**](MyCharactersApi.md#action_ge_sell_item_my_name_action_ge_sell_post) | **POST** /my/{name}/action/ge/sell | Action Ge Sell Item
[**action_move_my_name_action_move_post**](MyCharactersApi.md#action_move_my_name_action_move_post) | **POST** /my/{name}/action/move | Action Move
[**action_recycling_my_name_action_recycling_post**](MyCharactersApi.md#action_recycling_my_name_action_recycling_post) | **POST** /my/{name}/action/recycling | Action Recycling
[**action_task_exchange_my_name_action_task_exchange_post**](MyCharactersApi.md#action_task_exchange_my_name_action_task_exchange_post) | **POST** /my/{name}/action/task/exchange | Action Task Exchange
[**action_unequip_item_my_name_action_unequip_post**](MyCharactersApi.md#action_unequip_item_my_name_action_unequip_post) | **POST** /my/{name}/action/unequip | Action Unequip Item
[**action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post**](MyCharactersApi.md#action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post) | **POST** /my/{name}/action/bank/withdraw/gold | Action Withdraw Bank Gold
[**action_withdraw_bank_my_name_action_bank_withdraw_post**](MyCharactersApi.md#action_withdraw_bank_my_name_action_bank_withdraw_post) | **POST** /my/{name}/action/bank/withdraw | Action Withdraw Bank
[**get_all_characters_logs_my_logs_get**](MyCharactersApi.md#get_all_characters_logs_my_logs_get) | **GET** /my/logs | Get All Characters Logs
[**get_my_characters_my_characters_get**](MyCharactersApi.md#get_my_characters_my_characters_get) | **GET** /my/characters | Get My Characters


# **action_accept_new_task_my_name_action_task_new_post**
> TaskResponseSchema action_accept_new_task_my_name_action_task_new_post(name)

Action Accept New Task

Accepting a new task.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.task_response_schema import TaskResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.

    try:
        # Action Accept New Task
        api_response = await api_instance.action_accept_new_task_my_name_action_task_new_post(name)
        print("The response of MyCharactersApi->action_accept_new_task_my_name_action_task_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_accept_new_task_my_name_action_task_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 

### Return type

[**TaskResponseSchema**](TaskResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New task successfully accepted. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**598** | Tasks Master not found on this map. |  -  |
**489** | Character already has a task. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_complete_task_my_name_action_task_complete_post**
> TaskRewardResponseSchema action_complete_task_my_name_action_task_complete_post(name)

Action Complete Task

Complete a task.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.task_reward_response_schema import TaskRewardResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.

    try:
        # Action Complete Task
        api_response = await api_instance.action_complete_task_my_name_action_task_complete_post(name)
        print("The response of MyCharactersApi->action_complete_task_my_name_action_task_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_complete_task_my_name_action_task_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 

### Return type

[**TaskRewardResponseSchema**](TaskRewardResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The task has been successfully completed. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**598** | Tasks Master not found on this map. |  -  |
**488** | Character has not completed the task. |  -  |
**487** | Character has no task. |  -  |
**497** | Character inventory is full. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_crafting_my_name_action_crafting_post**
> SkillResponseSchema action_crafting_my_name_action_crafting_post(name, crafting_schema)

Action Crafting

Crafting an item. The character must be on a map with a workshop.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.crafting_schema import CraftingSchema
from pyartifactsmmo.models.skill_response_schema import SkillResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    crafting_schema = pyartifactsmmo.CraftingSchema() # CraftingSchema | 

    try:
        # Action Crafting
        api_response = await api_instance.action_crafting_my_name_action_crafting_post(name, crafting_schema)
        print("The response of MyCharactersApi->action_crafting_my_name_action_crafting_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_crafting_my_name_action_crafting_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **crafting_schema** | [**CraftingSchema**](CraftingSchema.md)|  | 

### Return type

[**SkillResponseSchema**](SkillResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The item was successfully crafted. |  -  |
**404** | Craft not found. |  -  |
**598** | Workshop not found on this map. |  -  |
**498** | Character not found. |  -  |
**497** | Character inventory is full. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**493** | Not skill level required. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_delete_item_my_name_action_delete_post**
> DeleteItemResponseSchema action_delete_item_my_name_action_delete_post(name, simple_item_schema)

Action Delete Item

Delete an item from your character's inventory.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.delete_item_response_schema import DeleteItemResponseSchema
from pyartifactsmmo.models.simple_item_schema import SimpleItemSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    simple_item_schema = pyartifactsmmo.SimpleItemSchema() # SimpleItemSchema | 

    try:
        # Action Delete Item
        api_response = await api_instance.action_delete_item_my_name_action_delete_post(name, simple_item_schema)
        print("The response of MyCharactersApi->action_delete_item_my_name_action_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_delete_item_my_name_action_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **simple_item_schema** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 

### Return type

[**DeleteItemResponseSchema**](DeleteItemResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item successfully deleted from your character. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_deposit_bank_gold_my_name_action_bank_deposit_gold_post**
> GoldResponseSchema action_deposit_bank_gold_my_name_action_bank_deposit_gold_post(name, deposit_withdraw_gold_schema)

Action Deposit Bank Gold

Deposit golds in a bank on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.deposit_withdraw_gold_schema import DepositWithdrawGoldSchema
from pyartifactsmmo.models.gold_response_schema import GoldResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    deposit_withdraw_gold_schema = pyartifactsmmo.DepositWithdrawGoldSchema() # DepositWithdrawGoldSchema | 

    try:
        # Action Deposit Bank Gold
        api_response = await api_instance.action_deposit_bank_gold_my_name_action_bank_deposit_gold_post(name, deposit_withdraw_gold_schema)
        print("The response of MyCharactersApi->action_deposit_bank_gold_my_name_action_bank_deposit_gold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_deposit_bank_gold_my_name_action_bank_deposit_gold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **deposit_withdraw_gold_schema** | [**DepositWithdrawGoldSchema**](DepositWithdrawGoldSchema.md)|  | 

### Return type

[**GoldResponseSchema**](GoldResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Golds successfully deposited in your bank. |  -  |
**598** | Bank not found on this map. |  -  |
**492** | Insufficient golds on your character. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**461** | A transaction is already in progress with this item/your golds in your bank. |  -  |
**486** | An action is already in progress by your character. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_deposit_bank_my_name_action_bank_deposit_post**
> ActionItemBankResponseSchema action_deposit_bank_my_name_action_bank_deposit_post(name, simple_item_schema)

Action Deposit Bank

Deposit an item in a bank on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.action_item_bank_response_schema import ActionItemBankResponseSchema
from pyartifactsmmo.models.simple_item_schema import SimpleItemSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    simple_item_schema = pyartifactsmmo.SimpleItemSchema() # SimpleItemSchema | 

    try:
        # Action Deposit Bank
        api_response = await api_instance.action_deposit_bank_my_name_action_bank_deposit_post(name, simple_item_schema)
        print("The response of MyCharactersApi->action_deposit_bank_my_name_action_bank_deposit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_deposit_bank_my_name_action_bank_deposit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **simple_item_schema** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 

### Return type

[**ActionItemBankResponseSchema**](ActionItemBankResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item successfully deposited in your bank. |  -  |
**598** | Bank not found on this map. |  -  |
**404** | Item not found. |  -  |
**461** | A transaction is already in progress with this item/your golds in your bank. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_equip_item_my_name_action_equip_post**
> EquipmentResponseSchema action_equip_item_my_name_action_equip_post(name, equip_schema)

Action Equip Item

Equip an item on your character.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.equip_schema import EquipSchema
from pyartifactsmmo.models.equipment_response_schema import EquipmentResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    equip_schema = pyartifactsmmo.EquipSchema() # EquipSchema | 

    try:
        # Action Equip Item
        api_response = await api_instance.action_equip_item_my_name_action_equip_post(name, equip_schema)
        print("The response of MyCharactersApi->action_equip_item_my_name_action_equip_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_equip_item_my_name_action_equip_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **equip_schema** | [**EquipSchema**](EquipSchema.md)|  | 

### Return type

[**EquipmentResponseSchema**](EquipmentResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The item has been successfully equipped on your character. |  -  |
**404** | Item not found. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |
**496** | Character level is insufficient. |  -  |
**491** | Slot is not empty. |  -  |
**485** | This item is already equipped. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_fight_my_name_action_fight_post**
> CharacterFightResponseSchema action_fight_my_name_action_fight_post(name)

Action Fight

Start a fight against a monster on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.character_fight_response_schema import CharacterFightResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.

    try:
        # Action Fight
        api_response = await api_instance.action_fight_my_name_action_fight_post(name)
        print("The response of MyCharactersApi->action_fight_my_name_action_fight_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_fight_my_name_action_fight_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 

### Return type

[**CharacterFightResponseSchema**](CharacterFightResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fight ended successfully. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**598** | Monster not found on this map. |  -  |
**486** | An action is already in progress by your character. |  -  |
**497** | Character inventory is full. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_gathering_my_name_action_gathering_post**
> SkillResponseSchema action_gathering_my_name_action_gathering_post(name)

Action Gathering

Harvest a resource on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.skill_response_schema import SkillResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.

    try:
        # Action Gathering
        api_response = await api_instance.action_gathering_my_name_action_gathering_post(name)
        print("The response of MyCharactersApi->action_gathering_my_name_action_gathering_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_gathering_my_name_action_gathering_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 

### Return type

[**SkillResponseSchema**](SkillResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resource has been successfully gathered. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**598** | Resource not found on this map. |  -  |
**486** | An action is already in progress by your character. |  -  |
**493** | Not skill level required. |  -  |
**497** | Character inventory is full. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_ge_buy_item_my_name_action_ge_buy_post**
> GETransactionResponseSchema action_ge_buy_item_my_name_action_ge_buy_post(name, ge_transaction_item_schema)

Action Ge Buy Item

Buy an item at the Grand Exchange on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.ge_transaction_item_schema import GETransactionItemSchema
from pyartifactsmmo.models.ge_transaction_response_schema import GETransactionResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    ge_transaction_item_schema = pyartifactsmmo.GETransactionItemSchema() # GETransactionItemSchema | 

    try:
        # Action Ge Buy Item
        api_response = await api_instance.action_ge_buy_item_my_name_action_ge_buy_post(name, ge_transaction_item_schema)
        print("The response of MyCharactersApi->action_ge_buy_item_my_name_action_ge_buy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_ge_buy_item_my_name_action_ge_buy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **ge_transaction_item_schema** | [**GETransactionItemSchema**](GETransactionItemSchema.md)|  | 

### Return type

[**GETransactionResponseSchema**](GETransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item successfully buy from the Grand Exchange. |  -  |
**598** | Grand Exchange not found on this map. |  -  |
**498** | Character not found. |  -  |
**497** | Character inventory is full. |  -  |
**499** | Character in cooldown. |  -  |
**483** | A transaction is already in progress on this item by a another character. |  -  |
**486** | An action is already in progress by your character. |  -  |
**492** | Insufficient golds on your character. |  -  |
**480** | No stock for this item. |  -  |
**482** | No item at this price. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_ge_sell_item_my_name_action_ge_sell_post**
> GETransactionResponseSchema action_ge_sell_item_my_name_action_ge_sell_post(name, ge_transaction_item_schema)

Action Ge Sell Item

Sell an item at the Grand Exchange on the character's map.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.ge_transaction_item_schema import GETransactionItemSchema
from pyartifactsmmo.models.ge_transaction_response_schema import GETransactionResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    ge_transaction_item_schema = pyartifactsmmo.GETransactionItemSchema() # GETransactionItemSchema | 

    try:
        # Action Ge Sell Item
        api_response = await api_instance.action_ge_sell_item_my_name_action_ge_sell_post(name, ge_transaction_item_schema)
        print("The response of MyCharactersApi->action_ge_sell_item_my_name_action_ge_sell_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_ge_sell_item_my_name_action_ge_sell_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **ge_transaction_item_schema** | [**GETransactionItemSchema**](GETransactionItemSchema.md)|  | 

### Return type

[**GETransactionResponseSchema**](GETransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item successfully sell at the Grand Exchange. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**404** | Item not found. |  -  |
**483** | A transaction is already in progress on this item by a another character. |  -  |
**486** | An action is already in progress by your character. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |
**482** | No item at this price. |  -  |
**598** | Grand Exchange not found on this map. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_move_my_name_action_move_post**
> CharacterMovementResponseSchema action_move_my_name_action_move_post(name, destination_schema)

Action Move

Moves a character on the map using the map's X and Y position.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.character_movement_response_schema import CharacterMovementResponseSchema
from pyartifactsmmo.models.destination_schema import DestinationSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    destination_schema = pyartifactsmmo.DestinationSchema() # DestinationSchema | 

    try:
        # Action Move
        api_response = await api_instance.action_move_my_name_action_move_post(name, destination_schema)
        print("The response of MyCharactersApi->action_move_my_name_action_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_move_my_name_action_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **destination_schema** | [**DestinationSchema**](DestinationSchema.md)|  | 

### Return type

[**CharacterMovementResponseSchema**](CharacterMovementResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The character has moved successfully. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**490** | Character already at destination. |  -  |
**404** | Map not found. |  -  |
**486** | An action is already in progress by your character. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_recycling_my_name_action_recycling_post**
> RecyclingResponseSchema action_recycling_my_name_action_recycling_post(name, recycling_schema)

Action Recycling

Recyling an item. The character must be on a map with a workshop (only for equipments and weapons).

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.recycling_response_schema import RecyclingResponseSchema
from pyartifactsmmo.models.recycling_schema import RecyclingSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    recycling_schema = pyartifactsmmo.RecyclingSchema() # RecyclingSchema | 

    try:
        # Action Recycling
        api_response = await api_instance.action_recycling_my_name_action_recycling_post(name, recycling_schema)
        print("The response of MyCharactersApi->action_recycling_my_name_action_recycling_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_recycling_my_name_action_recycling_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **recycling_schema** | [**RecyclingSchema**](RecyclingSchema.md)|  | 

### Return type

[**RecyclingResponseSchema**](RecyclingResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The items were successfully recycled. |  -  |
**404** | Item not found. |  -  |
**598** | Workshop not found on this map. |  -  |
**498** | Character not found. |  -  |
**497** | Character inventory is full. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**493** | Not skill level required. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |
**473** | This item cannot be recycled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_task_exchange_my_name_action_task_exchange_post**
> TaskRewardResponseSchema action_task_exchange_my_name_action_task_exchange_post(name)

Action Task Exchange

Exchange 3 tasks coins for a random reward. Rewards are exclusive resources for crafting  items.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.task_reward_response_schema import TaskRewardResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.

    try:
        # Action Task Exchange
        api_response = await api_instance.action_task_exchange_my_name_action_task_exchange_post(name)
        print("The response of MyCharactersApi->action_task_exchange_my_name_action_task_exchange_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_task_exchange_my_name_action_task_exchange_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 

### Return type

[**TaskRewardResponseSchema**](TaskRewardResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tasks coins have been successfully exchanged. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**598** | Tasks Master not found on this map. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |
**497** | Character inventory is full. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_unequip_item_my_name_action_unequip_post**
> EquipmentResponseSchema action_unequip_item_my_name_action_unequip_post(name, unequip_schema)

Action Unequip Item

Unequip an item on your character.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.equipment_response_schema import EquipmentResponseSchema
from pyartifactsmmo.models.unequip_schema import UnequipSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    unequip_schema = pyartifactsmmo.UnequipSchema() # UnequipSchema | 

    try:
        # Action Unequip Item
        api_response = await api_instance.action_unequip_item_my_name_action_unequip_post(name, unequip_schema)
        print("The response of MyCharactersApi->action_unequip_item_my_name_action_unequip_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_unequip_item_my_name_action_unequip_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **unequip_schema** | [**UnequipSchema**](UnequipSchema.md)|  | 

### Return type

[**EquipmentResponseSchema**](EquipmentResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The item has been successfully unequipped and added in his inventory. |  -  |
**404** | Item not found. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**486** | An action is already in progress by your character. |  -  |
**491** | Slot is empty. |  -  |
**497** | Character inventory is full. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post**
> GoldResponseSchema action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post(name, deposit_withdraw_gold_schema)

Action Withdraw Bank Gold

Withdraw gold from your bank.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.deposit_withdraw_gold_schema import DepositWithdrawGoldSchema
from pyartifactsmmo.models.gold_response_schema import GoldResponseSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    deposit_withdraw_gold_schema = pyartifactsmmo.DepositWithdrawGoldSchema() # DepositWithdrawGoldSchema | 

    try:
        # Action Withdraw Bank Gold
        api_response = await api_instance.action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post(name, deposit_withdraw_gold_schema)
        print("The response of MyCharactersApi->action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **deposit_withdraw_gold_schema** | [**DepositWithdrawGoldSchema**](DepositWithdrawGoldSchema.md)|  | 

### Return type

[**GoldResponseSchema**](GoldResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Golds successfully withdraw from your bank. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**461** | A transaction is already in progress with this item/your golds in your bank. |  -  |
**486** | An action is already in progress by your character. |  -  |
**598** | Bank not found on this map. |  -  |
**460** | Insufficient golds in your bank. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_withdraw_bank_my_name_action_bank_withdraw_post**
> ActionItemBankResponseSchema action_withdraw_bank_my_name_action_bank_withdraw_post(name, simple_item_schema)

Action Withdraw Bank

Take an item from your bank and put it in the character's inventory.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.action_item_bank_response_schema import ActionItemBankResponseSchema
from pyartifactsmmo.models.simple_item_schema import SimpleItemSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    name = 'name_example' # str | Name of your character.
    simple_item_schema = pyartifactsmmo.SimpleItemSchema() # SimpleItemSchema | 

    try:
        # Action Withdraw Bank
        api_response = await api_instance.action_withdraw_bank_my_name_action_bank_withdraw_post(name, simple_item_schema)
        print("The response of MyCharactersApi->action_withdraw_bank_my_name_action_bank_withdraw_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->action_withdraw_bank_my_name_action_bank_withdraw_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of your character. | 
 **simple_item_schema** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 

### Return type

[**ActionItemBankResponseSchema**](ActionItemBankResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Item successfully withdraw from your bank. |  -  |
**404** | Item not found. |  -  |
**498** | Character not found. |  -  |
**499** | Character in cooldown. |  -  |
**461** | A transaction is already in progress with this item/your golds in your bank. |  -  |
**486** | An action is already in progress by your character. |  -  |
**497** | Character inventory is full. |  -  |
**598** | Bank not found on this map. |  -  |
**478** | Missing item or insufficient quantity in your inventory. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_characters_logs_my_logs_get**
> DataPageLogSchema get_all_characters_logs_my_logs_get(page=page, size=size)

Get All Characters Logs

History of the last 100 actions of all your characters.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.data_page_log_schema import DataPageLogSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 50 # int | Page size (optional) (default to 50)

    try:
        # Get All Characters Logs
        api_response = await api_instance.get_all_characters_logs_my_logs_get(page=page, size=size)
        print("The response of MyCharactersApi->get_all_characters_logs_my_logs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->get_all_characters_logs_my_logs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 50]

### Return type

[**DataPageLogSchema**](DataPageLogSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched logs. |  -  |
**404** | Logs not found. |  -  |
**498** | Character not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_characters_my_characters_get**
> MyCharactersListSchema get_my_characters_my_characters_get()

Get My Characters

List of your characters.

### Example

* Bearer Authentication (JWTBearer):

```python
import pyartifactsmmo
from pyartifactsmmo.models.my_characters_list_schema import MyCharactersListSchema
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
    api_instance = pyartifactsmmo.MyCharactersApi(api_client)

    try:
        # Get My Characters
        api_response = await api_instance.get_my_characters_my_characters_get()
        print("The response of MyCharactersApi->get_my_characters_my_characters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCharactersApi->get_my_characters_my_characters_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MyCharactersListSchema**](MyCharactersListSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched characters. |  -  |
**404** | Characters not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

