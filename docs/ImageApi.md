# qualys_cs_api.ImageApi

All URIs are relative to *http://qualysapi.qg2.apps.qualys.com/csapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_images_using_delete**](ImageApi.md#delete_images_using_delete) | **DELETE** /v1.1/images | Delete images in your account
[**get_image_association_using_get**](ImageApi.md#get_image_association_using_get) | **GET** /v1.1/images/{imageId}/association | Show associations for an image
[**get_image_details_using_get**](ImageApi.md#get_image_details_using_get) | **GET** /v1.1/images/{imageId} | Show details of an image
[**get_image_installed_software_using_get**](ImageApi.md#get_image_installed_software_using_get) | **GET** /v1.1/images/{imageId}/software | Show software installed on an image
[**get_image_pivot_data_with_list_using_get**](ImageApi.md#get_image_pivot_data_with_list_using_get) | **GET** /v1.1/images | Show a list of images in your account
[**get_image_vuln_count_using_get**](ImageApi.md#get_image_vuln_count_using_get) | **GET** /v1.1/images/{imageId}/vuln/count | Show vulnerability count for an image
[**get_image_vuln_details_using_get**](ImageApi.md#get_image_vuln_details_using_get) | **GET** /v1.1/images/{imageId}/vuln | Show vulnerability details for an image


# **delete_images_using_delete**
> str delete_images_using_delete(image_delete_request)

Delete images in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_delete_request = qualys_cs_api.ImageDeleteRequest() # ImageDeleteRequest | Provide one or more image Ids or filters in the format shown under Example Value.

try:
    # Delete images in your account
    api_response = api_instance.delete_images_using_delete(image_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->delete_images_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_delete_request** | [**ImageDeleteRequest**](ImageDeleteRequest.md)| Provide one or more image Ids or filters in the format shown under Example Value. | 

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

# **get_image_association_using_get**
> ImageAssociation get_image_association_using_get(image_id, filter=filter, type=type)

Show associations for an image

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_id = 'image_id_example' # str | imageId
filter = 'filter_example' # str | filter (optional)
type = 'type_example' # str | type (optional)

try:
    # Show associations for an image
    api_response = api_instance.get_image_association_using_get(image_id, filter=filter, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_association_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| imageId | 
 **filter** | **str**| filter | [optional] 
 **type** | **str**| type | [optional] 

### Return type

[**ImageAssociation**](ImageAssociation.md)

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

# **get_image_details_using_get**
> ImageDetails get_image_details_using_get(image_id)

Show details of an image

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_id = 'image_id_example' # str | Specify the ID or SHA value of a specific image in the user’s scope.

try:
    # Show details of an image
    api_response = api_instance.get_image_details_using_get(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Specify the ID or SHA value of a specific image in the user’s scope. | 

### Return type

[**ImageDetails**](ImageDetails.md)

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

# **get_image_installed_software_using_get**
> SoftwarePivotListResponse get_image_installed_software_using_get(image_id, filter=filter, sort=sort)

Show software installed on an image

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_id = 'image_id_example' # str | Specify the ID or SHA value of a specific image in the user’s scope.
filter = 'filter_example' # str | Filter the image vulnerability details by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. For example qid:asc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional)

try:
    # Show software installed on an image
    api_response = api_instance.get_image_installed_software_using_get(image_id, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_installed_software_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Specify the ID or SHA value of a specific image in the user’s scope. | 
 **filter** | **str**| Filter the image vulnerability details by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example qid:asc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] 

### Return type

[**SoftwarePivotListResponse**](SoftwarePivotListResponse.md)

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

# **get_image_pivot_data_with_list_using_get**
> PivotListResponseAbstractImage get_image_pivot_data_with_list_using_get(page_number, page_size, filter=filter, sort=sort)

Show a list of images in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
page_number = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the images list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'created:desc' # str | Sort the results using a Qualys token. For example created:desc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional) (default to 'created:desc')

try:
    # Show a list of images in your account
    api_response = api_instance.get_image_pivot_data_with_list_using_get(page_number, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_pivot_data_with_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the images list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example created:desc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] [default to &#39;created:desc&#39;]

### Return type

[**PivotListResponseAbstractImage**](PivotListResponseAbstractImage.md)

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

# **get_image_vuln_count_using_get**
> dict(str, int) get_image_vuln_count_using_get(image_id)

Show vulnerability count for an image

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_id = 'image_id_example' # str | Specify the ID or SHA value of a specific image in the user’s scope.

try:
    # Show vulnerability count for an image
    api_response = api_instance.get_image_vuln_count_using_get(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_vuln_count_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Specify the ID or SHA value of a specific image in the user’s scope. | 

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

# **get_image_vuln_details_using_get**
> ImageVulnResponseFacade get_image_vuln_details_using_get(image_id, filter=filter, type=type, sort=sort)

Show vulnerability details for an image

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.ImageApi()
image_id = 'image_id_example' # str | Specify the ID or SHA value of a specific image in the user’s scope.
filter = 'filter_example' # str | Filter the image vulnerability details by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
type = 'ALL' # str | Specify the type of information to be fetched: Summary, Details, All (optional) (default to 'ALL')
sort = 'qid:asc' # str | Sort the results using a Qualys token. For example qid:asc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional) (default to 'qid:asc')

try:
    # Show vulnerability details for an image
    api_response = api_instance.get_image_vuln_details_using_get(image_id, filter=filter, type=type, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_vuln_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Specify the ID or SHA value of a specific image in the user’s scope. | 
 **filter** | **str**| Filter the image vulnerability details by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **type** | **str**| Specify the type of information to be fetched: Summary, Details, All | [optional] [default to &#39;ALL&#39;]
 **sort** | **str**| Sort the results using a Qualys token. For example qid:asc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] [default to &#39;qid:asc&#39;]

### Return type

[**ImageVulnResponseFacade**](ImageVulnResponseFacade.md)

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

