# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.task import Task  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTaskController(BaseTestCase):
    """TaskController integration test stubs"""

    def test_task_post(self):
        """Test case for task_post

        Adding task to list
        """
        body = Task()
        data = dict(name='name_example',
                    description='description_example')
        response = self.client.open(
            '/task',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
