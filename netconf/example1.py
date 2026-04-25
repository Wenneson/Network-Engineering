"""
3 NETCONF get-config example (ncclient) for Cisco IOS XE.
4 - Connects to 192.168.1.201
5 - Runs <get-config> against the running datastore
6 - Pretty prints the reply with minidom
7 """


from ncclient import manager
from xml.dom import minidom

def pretty_xml(xml_str: str) -> str:
    """Pretty-print XML string using minidom."""
    return minidom.parseString(xml_str.encode("utf-8")).toprettyxml(indent=" ")

def main():
    host = "10.99.2.165"
    username = "lab_admin"
    password = "Cisco123"
    port = 830
    
    with manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False, # lab only; use host key verification in real envs
    ) as m:
        # You can change "running to "startup if needed
        reply = m.get_config(source="running")
        
        # ncclient reply can be turned into an XML string like this:
        raw_xml = reply.xml
        
        print(pretty_xml(raw_xml))
    
if __name__ == "__main__":
     main()