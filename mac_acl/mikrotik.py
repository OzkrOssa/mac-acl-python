import routeros_api
import macaddress
from settings import AP


class MAC(macaddress.MAC):
     formats = (
         'xx:xx:xx:xx:xx:xx',
     ) + macaddress.MAC.formats

class  MikrotikACL:
    def __init__(self, host, plaintext_login = False) -> None:
        self.host = host
        self.api = routeros_api.connect(host,AP["user"], AP["password"],plaintext_login=plaintext_login)

    def add_mac(self, mac, comment: str):
        try:
            self.api.get_binary_resource('/interface/wireless/access-list').call("add",{"mac-address":str(MAC(mac)).encode(), "comment":comment.encode()})
        except Exception as e:
            return {"error": e.args[0]}

