# coding: utf-8

"""
    Fugue API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class NotificationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_notification(self, notification, **kwargs):  # noqa: E501
        """Creates a new notification.  # noqa: E501

        Creates a new notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_notification(notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateNotificationInput notification: Configuration options for the new notification. (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_notification_with_http_info(notification, **kwargs)  # noqa: E501
        else:
            (data) = self.create_notification_with_http_info(notification, **kwargs)  # noqa: E501
            return data

    def create_notification_with_http_info(self, notification, **kwargs):  # noqa: E501
        """Creates a new notification.  # noqa: E501

        Creates a new notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_notification_with_http_info(notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateNotificationInput notification: Configuration options for the new notification. (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification' is set
        if ('notification' not in params or
                params['notification'] is None):
            raise ValueError("Missing the required parameter `notification` when calling `create_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'notification' in params:
            body_params = params['notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/notifications', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notification',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_notification(self, notification_id, **kwargs):  # noqa: E501
        """Deletes a notification.  # noqa: E501

        Deletes a notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_notification(notification_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str notification_id: Notification ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
            return data

    def delete_notification_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Deletes a notification.  # noqa: E501

        Deletes a notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_notification_with_http_info(notification_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str notification_id: Notification ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if ('notification_id' not in params or
                params['notification_id'] is None):
            raise ValueError("Missing the required parameter `notification_id` when calling `delete_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notification_id'] = params['notification_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/notifications/{notification_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_notifications(self, **kwargs):  # noqa: E501
        """Lists details for all notifications.  # noqa: E501

        Lists details for all notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_notifications(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: Number of items to skip before returning. This parameter is used when the number of items spans multiple pages.
        :param int max_items: Maximum number of items to return.
        :return: Notifications
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_notifications_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_notifications_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_notifications_with_http_info(self, **kwargs):  # noqa: E501
        """Lists details for all notifications.  # noqa: E501

        Lists details for all notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_notifications_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int offset: Number of items to skip before returning. This parameter is used when the number of items spans multiple pages.
        :param int max_items: Maximum number of items to return.
        :return: Notifications
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'max_items']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_notifications" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `list_notifications`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'max_items' in params and params['max_items'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_items` when calling `list_notifications`, must be a value less than or equal to `100`")  # noqa: E501
        if 'max_items' in params and params['max_items'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `max_items` when calling `list_notifications`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'max_items' in params:
            query_params.append(('max_items', params['max_items']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notifications',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_notification(self, notification_id, notification, **kwargs):  # noqa: E501
        """Updates an existing notification.  # noqa: E501

        Updates an existing notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_notification(notification_id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str notification_id: Notification ID. (required)
        :param UpdateNotificationInput notification: New configuration options for the notification. (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_notification_with_http_info(notification_id, notification, **kwargs)  # noqa: E501
        else:
            (data) = self.update_notification_with_http_info(notification_id, notification, **kwargs)  # noqa: E501
            return data

    def update_notification_with_http_info(self, notification_id, notification, **kwargs):  # noqa: E501
        """Updates an existing notification.  # noqa: E501

        Updates an existing notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_notification_with_http_info(notification_id, notification, async=True)
        >>> result = thread.get()

        :param async bool
        :param str notification_id: Notification ID. (required)
        :param UpdateNotificationInput notification: New configuration options for the notification. (required)
        :return: Notification
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id', 'notification']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if ('notification_id' not in params or
                params['notification_id'] is None):
            raise ValueError("Missing the required parameter `notification_id` when calling `update_notification`")  # noqa: E501
        # verify the required parameter 'notification' is set
        if ('notification' not in params or
                params['notification'] is None):
            raise ValueError("Missing the required parameter `notification` when calling `update_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notification_id'] = params['notification_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'notification' in params:
            body_params = params['notification']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/notifications/{notification_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Notification',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)