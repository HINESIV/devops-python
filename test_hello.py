from devopslib.randomdevice import Cisco_Devices


def test_Cisco_Devices():
    device_choice = Cisco_Devices()
    assert device_choice in ["ASA", "FTD", "Nexus", "Catalyst"]
