import paramiko
import macaddress
from mac_acl.settings import AP


class MAC(macaddress.MAC):
     formats = (
         'xx:xx:xx:xx:xx:xx',
     ) + macaddress.MAC.formats

class UbiquitiACL:
    """Construct SSH connection"""
    def __init__(self,host) -> None:
        self.host = host
        self.ubnt = paramiko.SSHClient()
        self.ubnt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ubnt.connect(host,22,AP["user"], AP["password"])

        stdin, stdout, stderr = self.ubnt.exec_command("cat /tmp/system.cfg | grep wireless.1.mac_acl.")

        self.data = stdout.readlines()

    def add_mac(self, mac , comment):
        """Calcule last mac acl added from list"""
        last_number = 0
        for x in self.data:
            if x.startswith("wireless.1.mac_acl."):
                parts = x.split(".")
            try:
                last_number = max(last_number, int(parts[-2]))
            except:
                pass
    
        command = f"echo -e 'wireless.1.mac_acl.{last_number+1}.mac={mac}\nwireless.1.mac_acl.{last_number+1}.comment={comment}\nwireless.1.mac_acl.{last_number+1}.status=enabled' >> /tmp/system.cfg"
        """Execute the command that registre mac to file /tmp/system.cfg into ubiquiti device"""
        try:
            self.ubnt.exec_command(command)
            return {"message": f"mac-address {mac} regisreted successfully "}
        except Exception as e:
            return {"error": e.args[0]}