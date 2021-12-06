from unittest import TestCase

from Librabobus.Mocks.UserRepoMock import UserDBRepoMock
from unittest.mock import Mock

from Librabobus.Repositories.UserRepository import UserRepository




def test_function_d():

    mock_obj = Mock()
    mock_obj.name = "foo"

    assert function_d(mock_obj) == "FOO"



