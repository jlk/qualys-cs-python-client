# qualys_cs_api.SensorApi

All URIs are relative to *http://qualysapi.qg2.apps.qualys.com/csapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sensors_using_delete**](SensorApi.md#delete_sensors_using_delete) | **DELETE** /v1.1/sensors | Delete sensors in your account
[**get_sensor_details_using_get**](SensorApi.md#get_sensor_details_using_get) | **GET** /v1.1/sensors/{sensorId} | Show details of a sensor
[**get_sensors_list_using_get**](SensorApi.md#get_sensors_list_using_get) | **GET** /v1.1/sensors | Show a list of sensors in your account


# **delete_sensors_using_delete**
> str delete_sensors_using_delete(sensor_delete_request)

Delete sensors in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.SensorApi()
sensor_delete_request = qualys_cs_api.SensorDeleteRequest() # SensorDeleteRequest | Provide one or more sensor Ids or filters in the format shown under Example Value.

try:
    # Delete sensors in your account
    api_response = api_instance.delete_sensors_using_delete(sensor_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->delete_sensors_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_delete_request** | [**SensorDeleteRequest**](SensorDeleteRequest.md)| Provide one or more sensor Ids or filters in the format shown under Example Value. | 

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

# **get_sensor_details_using_get**
> Sensor get_sensor_details_using_get(sensor_id)

Show details of a sensor

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.SensorApi()
sensor_id = 'sensor_id_example' # str | Specify the sensor ID of a specific sensor in the user’s scope

try:
    # Show details of a sensor
    api_response = api_instance.get_sensor_details_using_get(sensor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->get_sensor_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**| Specify the sensor ID of a specific sensor in the user’s scope | 

### Return type

[**Sensor**](Sensor.md)

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

# **get_sensors_list_using_get**
> PivotListResponseSensor get_sensors_list_using_get(page_no, page_size, filter=filter, sort=sort)

Show a list of sensors in your account

### Example

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = qualys_cs_api.SensorApi()
page_no = 1 # int | The page to be returned. (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (default to 50)
filter = 'filter_example' # str | Filter the sensors list by providing a query using Qualys syntax. <a href='/cs/help/search/language.htm' target='_blank'>Click here</a> for help with creating your query. (optional)
sort = 'created:desc' # str | Sort the results using a Qualys token. For example created:desc. <a href='/cs/help/search_tips/sortable_tokens.htm'>Click here</a> for a listing of tokens. (optional) (default to 'created:desc')

try:
    # Show a list of sensors in your account
    api_response = api_instance.get_sensors_list_using_get(page_no, page_size, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->get_sensors_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_no** | **int**| The page to be returned. | [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [default to 50]
 **filter** | **str**| Filter the sensors list by providing a query using Qualys syntax. &lt;a href&#x3D;&#39;/cs/help/search/language.htm&#39; target&#x3D;&#39;_blank&#39;&gt;Click here&lt;/a&gt; for help with creating your query. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example created:desc. &lt;a href&#x3D;&#39;/cs/help/search_tips/sortable_tokens.htm&#39;&gt;Click here&lt;/a&gt; for a listing of tokens. | [optional] [default to &#39;created:desc&#39;]

### Return type

[**PivotListResponseSensor**](PivotListResponseSensor.md)

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

