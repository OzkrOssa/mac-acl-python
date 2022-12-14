import paramiko
import macaddress


class MAC(macaddress.MAC):
     formats = (
         'xx:xx:xx:xx:xx:xx',
     ) + macaddress.MAC.formats

class UbiquitiACL:
    def __init__(self,host) -> None:
        self.host = host
        self.ubnt = paramiko.SSHClient()
        self.ubnt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ubnt.connect(host,22,AP["user"], AP["password"])

        stdin, stdout, stderr = self.ubnt.exec_command("cat /tmp/system.cfg | grep wireless.1.mac_acl.")

        self.data = stdout.readlines()

    def add_mac(self, mac , comment):
        last_number = 0
        for x in self.data:
            if x.startswith("wireless.1.mac_acl."):
                parts = x.split(".")
            try:
                last_number = max(last_number, int(parts[-2]))
            except:
                pass
    
        command = f"echo -e 'wireless.1.mac_acl.{last_number+1}.mac={mac}\nwireless.1.mac_acl.{last_number+1}.comment={comment}\nwireless.1.mac_acl.{last_number+1}.status=enabled' >> /tmp/system.cfg"

        try:
            self.ubnt.exec_command(command)
            return {"message":"mac-address registered succesfully"}
        except Exception as e:
            return {"error": e.args[0]}

print(UbiquitiACL("192.168.88.44").add_mac("44:D9:E7:62:F8:F6","Oscar Ossa"))