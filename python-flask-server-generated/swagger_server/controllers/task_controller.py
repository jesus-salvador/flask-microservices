import connexion
import six

from swagger_server.models.task import Task  # noqa: E501
from swagger_server import util


def task_post(body=None):  # noqa: E501
    """Adding task to list

     # noqa: E501

    :param body: Created task object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def task_post(name=None, description=None):  # noqa: E501
    """Adding task to list

     # noqa: E501

    :param name: 
    :type name: str
    :param description: 
    :type description: str

    :rtype: None
    """
    return 'do some magic!'
