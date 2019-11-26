# qualys_cs_api.ContainerApi

All URIs are relative to *http://qualysapi.qg2.apps.qualys.com/csapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_containers_using_delete**](ContainerApi.md#delete_containers_using_delete) | **DELETE** /v1.1/containers | Delete containers in your account
[**get_container_details_using_get**](ContainerApi.md#get_container_details_using_get) | **GET** /v1.1/containers/{containerId} | Show details of a container
[**get_container_installed_software_details_using_get**](ContainerApi.md#get_container_installed_software_details_using_get) | **GET** /v1.1/containers/{containerId}/software | Show software installed on a container
[**get_container_vuln_count_using_get**](ContainerApi.md#get_container_vuln_count_using_get) | **GET** /v1.1/containers/{containerId}/vuln/count | Show vulnerability count for a container
[**get_container_vuln_details_using_get**](ContainerApi.md#get_container_vuln_details_using_get) | **GET** /v1.1/containers/{containerId}/vuln | Show vulnerability details for a container
[**get_containers_pivot_data_with_list_using_get**](ContainerApi.md#get_containers_pivot_data_with_list_using_get) | **GET** /v1.1/containers | Show a list of containers in your account


# **delete_containers_using_delete**
> str delete_containers_using_delete(container_delete_request)

Delete containers in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
container_delete_request = qualys_cs_api.ContainerDeleteRequest() # ContainerDeleteRequest | Provide one or more container Ids or filters in the format shown under Example Value.

try:
    # Delete containers in your account
    api_response = api_instance.delete_containers_using_delete(container_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->delete_containers_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_delete_request** | [**ContainerDeleteRequest**](ContainerDeleteRequest.md)| Provide one or more container Ids or filters in the format shown under Example Value. | 

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

# **get_container_details_using_get**
> ContainerDetails get_container_details_using_get(container_id)

Show details of a container

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
container_id = 'container_id_example' # str | Specify the ID or SHA value of a specific container in the user’s scope.

try:
    # Show details of a container
    api_response = api_instance.get_container_details_using_get(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Specify the ID or SHA value of a specific container in the user’s scope. | 

### Return type

[**ContainerDetails**](ContainerDetails.md)

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

# **get_container_installed_software_details_using_get**
> SoftwarePivotListFacade get_container_installed_software_details_using_get(container_id, filter=filter, sort=sort, is_drift=is_drift)

Show software installed on a container

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
container_id = 'container_id_example' # str | Specify the ID or SHA value of a specific container in the user’s scope.
filter = 'filter_example' # str | Filter the container vulnerability details by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. For example created:desc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional)
is_drift = False # bool | isDrift (optional) (default to False)

try:
    # Show software installed on a container
    api_response = api_instance.get_container_installed_software_details_using_get(container_id, filter=filter, sort=sort, is_drift=is_drift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_installed_software_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Specify the ID or SHA value of a specific container in the user’s scope. | 
 **filter** | **str**| Filter the container vulnerability details by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example created:desc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] 
 **is_drift** | **bool**| isDrift | [optional] [default to False]

### Return type

[**SoftwarePivotListFacade**](SoftwarePivotListFacade.md)

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

# **get_container_vuln_count_using_get**
> dict(str, int) get_container_vuln_count_using_get(container_id)

Show vulnerability count for a container

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
container_id = 'container_id_example' # str | Specify the ID or SHA value of a specific container in the user’s scope.

try:
    # Show vulnerability count for a container
    api_response = api_instance.get_container_vuln_count_using_get(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_vuln_count_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Specify the ID or SHA value of a specific container in the user’s scope. | 

### Return type

**dict(str, int)**

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

# **get_container_vuln_details_using_get**
> ContainerVulnResponseFacade get_container_vuln_details_using_get(container_id, filter=filter, type=type, is_drift=is_drift)

Show vulnerability details for a container

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
container_id = 'container_id_example' # str | Specify the ID or SHA value of a specific container in the user’s scope.
filter = 'filter_example' # str | Filter the container vulnerability details by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
type = 'ALL' # str | Specify the type of information to be fetched: Summary, Details, All. (optional) (default to 'ALL')
is_drift = False # bool | isDrift (optional) (default to False)

try:
    # Show vulnerability details for a container
    api_response = api_instance.get_container_vuln_details_using_get(container_id, filter=filter, type=type, is_drift=is_drift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_vuln_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Specify the ID or SHA value of a specific container in the user’s scope. | 
 **filter** | **str**| Filter the container vulnerability details by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **type** | **str**| Specify the type of information to be fetched: Summary, Details, All. | [optional] [default to &#39;ALL&#39;]
 **is_drift** | **bool**| isDrift | [optional] [default to False]

### Return type

[**ContainerVulnResponseFacade**](ContainerVulnResponseFacade.md)

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

# **get_containers_pivot_data_with_list_using_get**
> PivotListResponseContainer get_containers_pivot_data_with_list_using_get(page_no, page_size, filter=filter, sort=sort)

Show a list of containers in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi()
page_no = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the containers list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'created:desc' # str | Sort the results using a Qualys token. For example created:desc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional) (default to 'created:desc')

try:
    # Show a list of containers in your account
    api_response = api_instance.get_containers_pivot_data_with_list_using_get(page_no, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_containers_pivot_data_with_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example created:desc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] [default to &#39;created:desc&#39;]

### Return type

[**PivotListResponseContainer**](PivotListResponseContainer.md)

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

