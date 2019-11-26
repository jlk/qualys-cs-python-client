# qualys-cs-api
All features of the Container Security are available through REST APIs.<br/>Access support information at www.qualys.com/support/<br/><br/><b>Permissions:</b><br/>User must have the Container module enabled<br/>User must have API ACCESS permission

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.6.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import qualys_cs_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import qualys_cs_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import qualys_cs_api
from qualys_cs_api.rest import ApiException
from pprint import pprint


# Defining host is optional and default to http://qualysapi.qg2.apps.qualys.com/csapi
configuration.host = "http://qualysapi.qg2.apps.qualys.com/csapi"
# Create an instance of the API class
api_instance = qualys_cs_api.ContainerApi(qualys_cs_api.ApiClient(configuration))
container_delete_request = qualys_cs_api.ContainerDeleteRequest() # ContainerDeleteRequest | Provide one or more container Ids or filters in the format shown under Example Value.

try:
    # Delete containers in your account
    api_response = api_instance.delete_containers_using_delete(container_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->delete_containers_using_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://qualysapi.qg2.apps.qualys.com/csapi*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContainerApi* | [**delete_containers_using_delete**](docs/ContainerApi.md#delete_containers_using_delete) | **DELETE** /v1.1/containers | Delete containers in your account
*ContainerApi* | [**get_container_details_using_get**](docs/ContainerApi.md#get_container_details_using_get) | **GET** /v1.1/containers/{containerId} | Show details of a container
*ContainerApi* | [**get_container_installed_software_details_using_get**](docs/ContainerApi.md#get_container_installed_software_details_using_get) | **GET** /v1.1/containers/{containerId}/software | Show software installed on a container
*ContainerApi* | [**get_container_vuln_count_using_get**](docs/ContainerApi.md#get_container_vuln_count_using_get) | **GET** /v1.1/containers/{containerId}/vuln/count | Show vulnerability count for a container
*ContainerApi* | [**get_container_vuln_details_using_get**](docs/ContainerApi.md#get_container_vuln_details_using_get) | **GET** /v1.1/containers/{containerId}/vuln | Show vulnerability details for a container
*ContainerApi* | [**get_containers_pivot_data_with_list_using_get**](docs/ContainerApi.md#get_containers_pivot_data_with_list_using_get) | **GET** /v1.1/containers | Show a list of containers in your account
*ImageApi* | [**delete_images_using_delete**](docs/ImageApi.md#delete_images_using_delete) | **DELETE** /v1.1/images | Delete images in your account
*ImageApi* | [**get_image_association_using_get**](docs/ImageApi.md#get_image_association_using_get) | **GET** /v1.1/images/{imageId}/association | Show associations for an image
*ImageApi* | [**get_image_details_using_get**](docs/ImageApi.md#get_image_details_using_get) | **GET** /v1.1/images/{imageId} | Show details of an image
*ImageApi* | [**get_image_installed_software_using_get**](docs/ImageApi.md#get_image_installed_software_using_get) | **GET** /v1.1/images/{imageId}/software | Show software installed on an image
*ImageApi* | [**get_image_pivot_data_with_list_using_get**](docs/ImageApi.md#get_image_pivot_data_with_list_using_get) | **GET** /v1.1/images | Show a list of images in your account
*ImageApi* | [**get_image_vuln_count_using_get**](docs/ImageApi.md#get_image_vuln_count_using_get) | **GET** /v1.1/images/{imageId}/vuln/count | Show vulnerability count for an image
*ImageApi* | [**get_image_vuln_details_using_get**](docs/ImageApi.md#get_image_vuln_details_using_get) | **GET** /v1.1/images/{imageId}/vuln | Show vulnerability details for an image
*RegistryApi* | [**cancel_schedule_using_post**](docs/RegistryApi.md#cancel_schedule_using_post) | **POST** /v1.1/registry/{registryId}/schedule/{scheduleId}/cancel | Cancel registry schedule in your account
*RegistryApi* | [**create_aws_connector_using_post**](docs/RegistryApi.md#create_aws_connector_using_post) | **POST** /v1.1/registry/aws/connector | Create new AWS connector
*RegistryApi* | [**create_registry_using_post**](docs/RegistryApi.md#create_registry_using_post) | **POST** /v1.1/registry | Create a new registry
*RegistryApi* | [**create_schedule_using_post**](docs/RegistryApi.md#create_schedule_using_post) | **POST** /v1.1/registry/{registryId}/schedule | Create a new registry scan schedule
*RegistryApi* | [**delete_registries_using_delete**](docs/RegistryApi.md#delete_registries_using_delete) | **DELETE** /v1.1/registry | Delete multiple registries in your account
*RegistryApi* | [**delete_registry_using_delete**](docs/RegistryApi.md#delete_registry_using_delete) | **DELETE** /v1.1/registry/{registryId} | Delete registry in your account
*RegistryApi* | [**delete_schedule_using_delete**](docs/RegistryApi.md#delete_schedule_using_delete) | **DELETE** /v1.1/registry/{registryId}/schedule/{scheduleId} | Delete registry schedule in your account
*RegistryApi* | [**delete_schedules_using_delete**](docs/RegistryApi.md#delete_schedules_using_delete) | **DELETE** /v1.1/registry/{registryId}/schedule/ | Delete multiple registry schedules in your account
*RegistryApi* | [**get_aws_base_using_get**](docs/RegistryApi.md#get_aws_base_using_get) | **GET** /v1.1/registry/aws-base | Fetch AWS account ID and External ID for your account
*RegistryApi* | [**get_aws_connectors_list_using_get**](docs/RegistryApi.md#get_aws_connectors_list_using_get) | **GET** /v1.1/registry/aws/connectors | Show a list of AWS connectors in your account
*RegistryApi* | [**get_aws_connectors_via_customer_account_id_using_get**](docs/RegistryApi.md#get_aws_connectors_via_customer_account_id_using_get) | **GET** /v1.1/registry/aws/connectors/{accountId} | Show a list of AWS connectors for an AWS account ID
*RegistryApi* | [**get_registry_details_using_get**](docs/RegistryApi.md#get_registry_details_using_get) | **GET** /v1.1/registry/{registryId} | Show details of a registry
*RegistryApi* | [**get_registry_pivot_data_with_list_using_get**](docs/RegistryApi.md#get_registry_pivot_data_with_list_using_get) | **GET** /v1.1/registry | Show a list of registries in your account
*RegistryApi* | [**get_registry_repo_pivot_list_using_get**](docs/RegistryApi.md#get_registry_repo_pivot_list_using_get) | **GET** /v1.1/registry/{registryId}/repository | Show a list of repositories in a registry
*RegistryApi* | [**get_schedule_pivot_list_using_get**](docs/RegistryApi.md#get_schedule_pivot_list_using_get) | **GET** /v1.1/registry/{registryId}/schedule | Show a list of schedules created for a registry
*RegistryApi* | [**update_registry_using_put**](docs/RegistryApi.md#update_registry_using_put) | **PUT** /v1.1/registry/{registryId} | Update existing registry in your account
*RegistryApi* | [**update_schedule_using_put**](docs/RegistryApi.md#update_schedule_using_put) | **PUT** /v1.1/registry/{registryId}/schedule/{scheduleId} | Update existing registry schedule in your account
*RegistryApi* | [**validate_registry_using_post**](docs/RegistryApi.md#validate_registry_using_post) | **POST** /v1.1/registry/validate | Validate information for new registry
*SensorApi* | [**delete_sensors_using_delete**](docs/SensorApi.md#delete_sensors_using_delete) | **DELETE** /v1.1/sensors | Delete sensors in your account
*SensorApi* | [**get_sensor_details_using_get**](docs/SensorApi.md#get_sensor_details_using_get) | **GET** /v1.1/sensors/{sensorId} | Show details of a sensor
*SensorApi* | [**get_sensors_list_using_get**](docs/SensorApi.md#get_sensors_list_using_get) | **GET** /v1.1/sensors | Show a list of sensors in your account


## Documentation For Models

 - [APIErrorFacade](docs/APIErrorFacade.md)
 - [AWS](docs/AWS.md)
 - [AWSBase](docs/AWSBase.md)
 - [AWSConnector](docs/AWSConnector.md)
 - [AWSConnectorRequest](docs/AWSConnectorRequest.md)
 - [AWSDTO](docs/AWSDTO.md)
 - [AbstractImage](docs/AbstractImage.md)
 - [CMSError](docs/CMSError.md)
 - [Container](docs/Container.md)
 - [ContainerDeleteRequest](docs/ContainerDeleteRequest.md)
 - [ContainerDetails](docs/ContainerDetails.md)
 - [ContainerVulnList](docs/ContainerVulnList.md)
 - [ContainerVulnResponseFacade](docs/ContainerVulnResponseFacade.md)
 - [Credential](docs/Credential.md)
 - [CredentialDTO](docs/CredentialDTO.md)
 - [Cvss3Info](docs/Cvss3Info.md)
 - [CvssInfo](docs/CvssInfo.md)
 - [Drift](docs/Drift.md)
 - [DriftSoftware](docs/DriftSoftware.md)
 - [DriftVulnerability](docs/DriftVulnerability.md)
 - [Filter](docs/Filter.md)
 - [Host](docs/Host.md)
 - [HostStats](docs/HostStats.md)
 - [ImageAssociation](docs/ImageAssociation.md)
 - [ImageDeleteRequest](docs/ImageDeleteRequest.md)
 - [ImageDetails](docs/ImageDetails.md)
 - [ImageVulnResponseFacade](docs/ImageVulnResponseFacade.md)
 - [InstalledSoftware](docs/InstalledSoftware.md)
 - [Label](docs/Label.md)
 - [Layer](docs/Layer.md)
 - [PatchAvailability](docs/PatchAvailability.md)
 - [PivotListResponseAbstractImage](docs/PivotListResponseAbstractImage.md)
 - [PivotListResponseContainer](docs/PivotListResponseContainer.md)
 - [PivotListResponseRegistryRepoResponse](docs/PivotListResponseRegistryRepoResponse.md)
 - [PivotListResponseRegistryResponse](docs/PivotListResponseRegistryResponse.md)
 - [PivotListResponseScheduleResponse](docs/PivotListResponseScheduleResponse.md)
 - [PivotListResponseSensor](docs/PivotListResponseSensor.md)
 - [PortMapping](docs/PortMapping.md)
 - [RegistryDetails](docs/RegistryDetails.md)
 - [RegistryRepoResponse](docs/RegistryRepoResponse.md)
 - [RegistryRequest](docs/RegistryRequest.md)
 - [RegistryResponse](docs/RegistryResponse.md)
 - [Repo](docs/Repo.md)
 - [RepoTags](docs/RepoTags.md)
 - [ScheduleRequest](docs/ScheduleRequest.md)
 - [ScheduleResponse](docs/ScheduleResponse.md)
 - [Sensor](docs/Sensor.md)
 - [SensorDeleteRequest](docs/SensorDeleteRequest.md)
 - [ServiceDetails](docs/ServiceDetails.md)
 - [ServiceVulnerabilityDetails](docs/ServiceVulnerabilityDetails.md)
 - [Software](docs/Software.md)
 - [SoftwarePivotListFacade](docs/SoftwarePivotListFacade.md)
 - [SoftwarePivotListResponse](docs/SoftwarePivotListResponse.md)
 - [ThreatIntel](docs/ThreatIntel.md)
 - [VulnSummary](docs/VulnSummary.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




