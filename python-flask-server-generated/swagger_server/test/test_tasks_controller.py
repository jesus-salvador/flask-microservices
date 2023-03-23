# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTasksController(BaseTestCase):
    """TasksController integration test stubs"""

    def test_tasks_get(self):
        """Test case for tasks_get

        Returns a list of tasks.
        """
        response = self.client.open(
            '/tasks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
