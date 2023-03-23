# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestTaskNameController(BaseTestCase):
    """TaskNameController integration test stubs"""

    def test_task_taskname_delete(self):
        """Test case for task_taskname_delete

        Delete a task by name.
        """
        response = self.client.open(
            '/task/{taskname}'.format(taskname='taskname_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_task_taskname_get(self):
        """Test case for task_taskname_get

        Returns a task by name.
        """
        response = self.client.open(
            '/task/{taskname}'.format(taskname='taskname_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
