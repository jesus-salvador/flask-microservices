import connexion
import six

from swagger_server import util


def tasks_get():  # noqa: E501
    """Returns a list of tasks.

    Optional extended description in Markdown. # noqa: E501


    :rtype: str
    """
    tasks = [
        {'name': 'Laundry', 'description': 'Do the laundry this weekend'},
        {'name': 'Assignment', 'description': 'Finish assignment by Friday'},
        {'name': 'Call family', 'description': 'Call family Sunday morning'},
        {'name': 'Pay bills', 'description': 'Pay the electricity and water bill'},
    ]

    return tasks
