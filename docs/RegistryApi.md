# qualys_cs_api.RegistryApi

All URIs are relative to *http://qualysapi.qg2.apps.qualys.com/csapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_schedule_using_post**](RegistryApi.md#cancel_schedule_using_post) | **POST** /v1.1/registry/{registryId}/schedule/{scheduleId}/cancel | Cancel registry schedule in your account
[**create_aws_connector_using_post**](RegistryApi.md#create_aws_connector_using_post) | **POST** /v1.1/registry/aws/connector | Create new AWS connector
[**create_registry_using_post**](RegistryApi.md#create_registry_using_post) | **POST** /v1.1/registry | Create a new registry
[**create_schedule_using_post**](RegistryApi.md#create_schedule_using_post) | **POST** /v1.1/registry/{registryId}/schedule | Create a new registry scan schedule
[**delete_registries_using_delete**](RegistryApi.md#delete_registries_using_delete) | **DELETE** /v1.1/registry | Delete multiple registries in your account
[**delete_registry_using_delete**](RegistryApi.md#delete_registry_using_delete) | **DELETE** /v1.1/registry/{registryId} | Delete registry in your account
[**delete_schedule_using_delete**](RegistryApi.md#delete_schedule_using_delete) | **DELETE** /v1.1/registry/{registryId}/schedule/{scheduleId} | Delete registry schedule in your account
[**delete_schedules_using_delete**](RegistryApi.md#delete_schedules_using_delete) | **DELETE** /v1.1/registry/{registryId}/schedule/ | Delete multiple registry schedules in your account
[**get_aws_base_using_get**](RegistryApi.md#get_aws_base_using_get) | **GET** /v1.1/registry/aws-base | Fetch AWS account ID and External ID for your account
[**get_aws_connectors_list_using_get**](RegistryApi.md#get_aws_connectors_list_using_get) | **GET** /v1.1/registry/aws/connectors | Show a list of AWS connectors in your account
[**get_aws_connectors_via_customer_account_id_using_get**](RegistryApi.md#get_aws_connectors_via_customer_account_id_using_get) | **GET** /v1.1/registry/aws/connectors/{accountId} | Show a list of AWS connectors for an AWS account ID
[**get_registry_details_using_get**](RegistryApi.md#get_registry_details_using_get) | **GET** /v1.1/registry/{registryId} | Show details of a registry
[**get_registry_pivot_data_with_list_using_get**](RegistryApi.md#get_registry_pivot_data_with_list_using_get) | **GET** /v1.1/registry | Show a list of registries in your account
[**get_registry_repo_pivot_list_using_get**](RegistryApi.md#get_registry_repo_pivot_list_using_get) | **GET** /v1.1/registry/{registryId}/repository | Show a list of repositories in a registry
[**get_schedule_pivot_list_using_get**](RegistryApi.md#get_schedule_pivot_list_using_get) | **GET** /v1.1/registry/{registryId}/schedule | Show a list of schedules created for a registry
[**update_registry_using_put**](RegistryApi.md#update_registry_using_put) | **PUT** /v1.1/registry/{registryId} | Update existing registry in your account
[**update_schedule_using_put**](RegistryApi.md#update_schedule_using_put) | **PUT** /v1.1/registry/{registryId}/schedule/{scheduleId} | Update existing registry schedule in your account
[**validate_registry_using_post**](RegistryApi.md#validate_registry_using_post) | **POST** /v1.1/registry/validate | Validate information for new registry


# **cancel_schedule_using_post**
> str cancel_schedule_using_post(registry_id, schedule_id)

Cancel registry schedule in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to cancel the schedule for.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BasinelineRunning  

try:
    # Cancel registry schedule in your account
    api_response = api_instance.cancel_schedule_using_post(registry_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->cancel_schedule_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to cancel the schedule for. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BasinelineRunning   | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aws_connector_using_post**
> create_aws_connector_using_post(aws_connector_request)

Create new AWS connector

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
aws_connector_request = qualys_cs_api.AWSConnectorRequest() # AWSConnectorRequest | Provide parameter values in the format shown under Example Value.

try:
    # Create new AWS connector
    api_instance.create_aws_connector_using_post(aws_connector_request)
except ApiException as e:
    print("Exception when calling RegistryApi->create_aws_connector_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_connector_request** | [**AWSConnectorRequest**](AWSConnectorRequest.md)| Provide parameter values in the format shown under Example Value. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_registry_using_post**
> str create_registry_using_post(registry_request)

Create a new registry

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_request = qualys_cs_api.RegistryRequest() # RegistryRequest | Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional.

try:
    # Create a new registry
    api_response = api_instance.create_registry_using_post(registry_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_registry_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_request** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_schedule_using_post**
> str create_schedule_using_post(registry_id, schedule_request)

Create a new registry scan schedule

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID of the registry you want to scan.
schedule_request = qualys_cs_api.ScheduleRequest() # ScheduleRequest | Provide parameter values in the format shown under Example Value. Specify \"onDemand\": true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30.

try:
    # Create a new registry scan schedule
    api_response = api_instance.create_schedule_using_post(registry_id, schedule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_schedule_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry you want to scan. | 
 **schedule_request** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify \&quot;onDemand\&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registries_using_delete**
> str delete_registries_using_delete(registry_ids)

Delete multiple registries in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_ids = ['registry_ids_example'] # list[str] | Provide ID/UUIDs of the registries you want to delete. Should be in the form of an array, [\"regID1\",\"regID2\",\"regID3\"]. Note: You cannot delete registries whose schedules are in “Running” state.

try:
    # Delete multiple registries in your account
    api_response = api_instance.delete_registries_using_delete(registry_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registries_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_ids** | [**list[str]**](str.md)| Provide ID/UUIDs of the registries you want to delete. Should be in the form of an array, [\&quot;regID1\&quot;,\&quot;regID2\&quot;,\&quot;regID3\&quot;]. Note: You cannot delete registries whose schedules are in “Running” state. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry_using_delete**
> str delete_registry_using_delete(registry_id)

Delete registry in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to delete. Note: You cannot delete a registry whose schedules are in “Running” state.

try:
    # Delete registry in your account
    api_response = api_instance.delete_registry_using_delete(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_registry_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to delete. Note: You cannot delete a registry whose schedules are in “Running” state. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule_using_delete**
> str delete_schedule_using_delete(registry_id, schedule_id)

Delete registry schedule in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to delete.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to delete. Note: You cannot delete a schedule which is in “Running” state.

try:
    # Delete registry schedule in your account
    api_response = api_instance.delete_schedule_using_delete(registry_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_schedule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to delete. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to delete. Note: You cannot delete a schedule which is in “Running” state. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedules_using_delete**
> str delete_schedules_using_delete(registry_id, schedule_ids)

Delete multiple registry schedules in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to delete.
schedule_ids = ['schedule_ids_example'] # list[str] | Provide the ID/UUIDs of the schedules you want to delete. Should be in the form of an array, [\"schID1\",\"schID2\",\"schID3\"]. Note: You cannot delete schedules that are in “Running” state

try:
    # Delete multiple registry schedules in your account
    api_response = api_instance.delete_schedules_using_delete(registry_id, schedule_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_schedules_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to delete. | 
 **schedule_ids** | [**list[str]**](str.md)| Provide the ID/UUIDs of the schedules you want to delete. Should be in the form of an array, [\&quot;schID1\&quot;,\&quot;schID2\&quot;,\&quot;schID3\&quot;]. Note: You cannot delete schedules that are in “Running” state | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_base_using_get**
> AWSBase get_aws_base_using_get()

Fetch AWS account ID and External ID for your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()

try:
    # Fetch AWS account ID and External ID for your account
    api_response = api_instance.get_aws_base_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_aws_base_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AWSBase**](AWSBase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_connectors_list_using_get**
> list[AWSConnector] get_aws_connectors_list_using_get()

Show a list of AWS connectors in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()

try:
    # Show a list of AWS connectors in your account
    api_response = api_instance.get_aws_connectors_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_aws_connectors_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AWSConnector]**](AWSConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_connectors_via_customer_account_id_using_get**
> list[AWSConnector] get_aws_connectors_via_customer_account_id_using_get(account_id)

Show a list of AWS connectors for an AWS account ID

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
account_id = 'account_id_example' # str | Provide the AWS account Id to get a list of connectors.

try:
    # Show a list of AWS connectors for an AWS account ID
    api_response = api_instance.get_aws_connectors_via_customer_account_id_using_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_aws_connectors_via_customer_account_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Provide the AWS account Id to get a list of connectors. | 

### Return type

[**list[AWSConnector]**](AWSConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_details_using_get**
> RegistryDetails get_registry_details_using_get(registry_id)

Show details of a registry

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to fetch the details for.

try:
    # Show details of a registry
    api_response = api_instance.get_registry_details_using_get(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to fetch the details for. | 

### Return type

[**RegistryDetails**](RegistryDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_pivot_data_with_list_using_get**
> PivotListResponseRegistryResponse get_registry_pivot_data_with_list_using_get(page_no, page_size, filter=filter, sort=sort)

Show a list of registries in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
page_no = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the registries list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. For example <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional)

try:
    # Show a list of registries in your account
    api_response = api_instance.get_registry_pivot_data_with_list_using_get(page_no, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_pivot_data_with_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the registries list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] 

### Return type

[**PivotListResponseRegistryResponse**](PivotListResponseRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_repo_pivot_list_using_get**
> PivotListResponseRegistryRepoResponse get_registry_repo_pivot_list_using_get(registry_id, page_no, page_size, filter=filter, sort=sort)

Show a list of repositories in a registry

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to list the repositories.
page_no = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the repository list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. For example <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional)

try:
    # Show a list of repositories in a registry
    api_response = api_instance.get_registry_repo_pivot_list_using_get(registry_id, page_no, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_registry_repo_pivot_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry for which you want to list the repositories. | 
 **page_no** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the repository list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] 

### Return type

[**PivotListResponseRegistryRepoResponse**](PivotListResponseRegistryRepoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_pivot_list_using_get**
> PivotListResponseScheduleResponse get_schedule_pivot_list_using_get(registry_id, page_no, page_size, filter=filter, sort=sort)

Show a list of schedules created for a registry

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to list the schedules.
page_no = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the repository list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. For example <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional)

try:
    # Show a list of schedules created for a registry
    api_response = api_instance.get_schedule_pivot_list_using_get(registry_id, page_no, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_schedule_pivot_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry for which you want to list the schedules. | 
 **page_no** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the repository list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] 

### Return type

[**PivotListResponseScheduleResponse**](PivotListResponseScheduleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry_using_put**
> str update_registry_using_put(registry_id, registry_request)

Update existing registry in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to update.
registry_request = qualys_cs_api.RegistryRequest() # RegistryRequest | Provide parameter values in the format shown under Example Value.  registryType and registryUri are required even though they are not updatable.

try:
    # Update existing registry in your account
    api_response = api_instance.update_registry_using_put(registry_id, registry_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_registry_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to update. | 
 **registry_request** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value.  registryType and registryUri are required even though they are not updatable. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule_using_put**
> str update_schedule_using_put(registry_id, schedule_id, schedule_request)

Update existing registry schedule in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to update.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to update.
schedule_request = qualys_cs_api.ScheduleRequest() # ScheduleRequest | Provide parameter values in the format shown under Example Value. Specify \"onDemand\": true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30.

try:
    # Update existing registry schedule in your account
    api_response = api_instance.update_schedule_using_put(registry_id, schedule_id, schedule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_schedule_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to update. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to update. | 
 **schedule_request** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify \&quot;onDemand\&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered everyday at a set time. For days, specify 1 to 7 days / 14 (for last two weeks). For schedule, specify time in UTC, e.g., 19:30. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_registry_using_post**
> bool validate_registry_using_post(registry_request)

Validate information for new registry

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.RegistryApi()
registry_request = qualys_cs_api.RegistryRequest() # RegistryRequest | Validate parameters for a registry you intend to create. Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional.

try:
    # Validate information for new registry
    api_response = api_instance.validate_registry_using_post(registry_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->validate_registry_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_request** | [**RegistryRequest**](RegistryRequest.md)| Validate parameters for a registry you intend to create. Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized user |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

