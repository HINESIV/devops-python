from random import choices


def Cisco_Devices():
    Devices = ["ASA", "FTD", "Nexus", "Catalyst"]
    return choices(Devices)[0]
