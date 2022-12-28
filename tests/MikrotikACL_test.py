import unittest
import routeros_api
from unittest.mock import Mock
from mac_acl.mikrotik import MikrotikACL
from mac_acl.settings import AP

class TestMikrotikACL(unittest.TestCase):
    def test_add_mac(self):
        # Mock the routeros_api.connect method to return a mock API connection object
        routeros_api.connect = Mock(return_value=Mock())
        
        # Create a MikrotikACL object
        mikrotik_acl = MikrotikACL("10.0.0.1")
        
        # Call the add_mac method and assert that it returns the expected result
        assert mikrotik_acl.add_mac("00:00:00:00:00:00", "Test MAC") == {"message": "mac-address regisreted successfully "}
        
        # Assert that the routeros_api.connect method was called with the expected arguments
        routeros_api.connect.assert_called_with("10.0.0.1", AP["user"], AP["password"], plaintext_login=False)

