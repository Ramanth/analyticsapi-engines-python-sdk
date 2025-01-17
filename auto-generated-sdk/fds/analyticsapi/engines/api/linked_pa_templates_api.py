"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fds.analyticsapi.engines.api_client import ApiClient, Endpoint as _Endpoint
from fds.analyticsapi.engines.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fds.analyticsapi.engines.model.client_error_response import ClientErrorResponse
from fds.analyticsapi.engines.model.linked_pa_template_parameters_root import LinkedPATemplateParametersRoot
from fds.analyticsapi.engines.model.linked_pa_template_root import LinkedPATemplateRoot
from fds.analyticsapi.engines.model.linked_pa_template_summary_root import LinkedPATemplateSummaryRoot
from fds.analyticsapi.engines.model.linked_pa_template_update_parameters_root import LinkedPATemplateUpdateParametersRoot


class LinkedPATemplatesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_linked_pa_templates(
            self,
            linked_pa_template_parameters_root,
            **kwargs
        ):
            """Create a linked PA template  # noqa: E501

            This endpoint creates a template from an **existing portfolio analysis tile**, allowing the user to replicate and fetch reports settings.    Remarks:    *   Mandatory, optional and locked fields can be  \"accounts\", \"benchmarks\", \"groups\", \"columns\", \"dates\", \"currencyisocode\" and \"componentdetail\".    *   Mandatory and locked strings are mutually exclusive.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_linked_pa_templates(linked_pa_template_parameters_root, async_req=True)
            >>> result = thread.get()

            Args:
                linked_pa_template_parameters_root (LinkedPATemplateParametersRoot): Request Parameters

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LinkedPATemplateSummaryRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['linked_pa_template_parameters_root'] = \
                linked_pa_template_parameters_root
            return self.call_with_http_info(**kwargs)

        self.create_linked_pa_templates = _Endpoint(
            settings={
                'response_type': dict({ 201:(LinkedPATemplateSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/linked-templates',
                'operation_id': 'create_linked_pa_templates',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'linked_pa_template_parameters_root',
                ],
                'required': [
                    'linked_pa_template_parameters_root',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'linked_pa_template_parameters_root':
                        (LinkedPATemplateParametersRoot,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'linked_pa_template_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_linked_pa_templates
        )

        def __delete_linked_pa_templates(
            self,
            id,
            **kwargs
        ):
            """Delete a linked PA template.  # noqa: E501

            This endpoint deletes an existing linked PA template.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_linked_pa_templates(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a linked PA template

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.delete_linked_pa_templates = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/linked-templates/{id}',
                'operation_id': 'delete_linked_pa_templates',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_linked_pa_templates
        )

        def __get_linked_pa_templates(
            self,
            **kwargs
        ):
            """Get linked PA templates  # noqa: E501

            This endpoint returns the list of linked PA templates in given path.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_linked_pa_templates(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                directory (str): Get linked PA templates in path.. [optional]
                document_directory (str): Get linked PA templates for documents in document path. [optional]
                document_name (str): Get linked PA templates for documents by document name. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LinkedPATemplateSummaryRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_linked_pa_templates = _Endpoint(
            settings={
                'response_type': dict({ 200:(LinkedPATemplateSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/linked-templates',
                'operation_id': 'get_linked_pa_templates',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'directory',
                    'document_directory',
                    'document_name',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'directory':
                        (str,),
                    'document_directory':
                        (str,),
                    'document_name':
                        (str,),
                },
                'attribute_map': {
                    'directory': 'directory',
                    'document_directory': 'documentDirectory',
                    'document_name': 'documentName',
                },
                'location_map': {
                    'directory': 'query',
                    'document_directory': 'query',
                    'document_name': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_linked_pa_templates
        )

        def __get_linked_pa_templates_by_id(
            self,
            id,
            **kwargs
        ):
            """Get linked PA template by id  # noqa: E501

            This endpoint fetches the linked PA template settings.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_linked_pa_templates_by_id(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a linked PA template

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LinkedPATemplateRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_linked_pa_templates_by_id = _Endpoint(
            settings={
                'response_type': dict({ 200:(LinkedPATemplateRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/linked-templates/{id}',
                'operation_id': 'get_linked_pa_templates_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_linked_pa_templates_by_id
        )

        def __update_linked_pa_templates(
            self,
            id,
            linked_pa_template_update_parameters_root,
            **kwargs
        ):
            """Update a linked PA template  # noqa: E501

            This endpoint allows the user to change the request body and description from an existing template.    Remarks:    *   Mandatory, optional and locked fields can be  \"accounts\", \"benchmarks\", \"groups\", \"columns\", \"dates\", \"currencyisocode\" and \"componentdetail\".    *   Mandatory and locked strings are mutually exclusive.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_linked_pa_templates(id, linked_pa_template_update_parameters_root, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Unique identifier for a linked PA template
                linked_pa_template_update_parameters_root (LinkedPATemplateUpdateParametersRoot): Request Parameters

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is False.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                LinkedPATemplateSummaryRoot
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', False
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['linked_pa_template_update_parameters_root'] = \
                linked_pa_template_update_parameters_root
            return self.call_with_http_info(**kwargs)

        self.update_linked_pa_templates = _Endpoint(
            settings={
                'response_type': dict({ 200:(LinkedPATemplateSummaryRoot,),  }),
                'auth': [
                    'Basic',
                    'Bearer'
                ],
                'endpoint_path': '/analytics/engines/pa/v3/linked-templates/{id}',
                'operation_id': 'update_linked_pa_templates',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'linked_pa_template_update_parameters_root',
                ],
                'required': [
                    'id',
                    'linked_pa_template_update_parameters_root',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'linked_pa_template_update_parameters_root':
                        (LinkedPATemplateUpdateParametersRoot,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'linked_pa_template_update_parameters_root': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_linked_pa_templates
        )
