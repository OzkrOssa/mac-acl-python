import unittest
import paramiko
from unittest.mock import Mock
from mac_acl.ubuquiti import UbiquitiACL
from mac_acl.settings import AP

import unittest
from unittest.mock import Mock
from mac_acl.ubuquiti import UbiquitiACL

class TestUbiquitiACL(unittest.TestCase):
    def test_add_mac(self):
        # Create a mock SSH connection
        mock_ssh = Mock()

        # Set up the mock exec_command() method to return
        # pre-defined data when called
        mock_ssh.exec_command.return_value = (
            Mock(),  # stdin
            ["wireless.1.mac_acl.1.mac=aa:bb:cc:dd:ee:ff\n",  # stdout
             "wireless.1.mac_acl.2.mac=11:22:33:44:55:66\n",
             "wireless.1.mac_acl.3.mac=01:02:03:04:05:06\n"],
            Mock()  # stderr
        )

        # Create an instance of UbiquitiACL using the mock SSH connection
        acl = UbiquitiACL("192.168.1.1")

        # Call the add_mac() method and check that the correct
        # command is executed on the mock SSH connection
        result = acl.add_mac("aa:bb:cc:dd:ee:ff", "Test MAC")
        self.assertEqual(
            result,
            {"message": "mac-address registered succesfully"}
        )
        mock_ssh.exec_command.assert_called_with(
            "echo -e 'wireless.1.mac_acl.4.mac=aa:bb:cc:dd:ee:ff\n"
            "wireless.1.mac_acl.4.comment=Test MAC\n"
            "wireless.1.mac_acl.4.status=enabled' >> /tmp/system.cfg"
        )

if __name__ == "__main__":
    unittest.main()