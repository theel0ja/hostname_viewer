import socket
from netaddr import *

def get_hostname(ip):
    return socket.gethostbyaddr(ip)[0]

def get_ip_addresses_in_ip_range(ip_range):
    ip = IPNetwork(ip_range)

    data = []

    for addr in ip:
        data.append(str(addr))

    return data

def get_data_by_ipblock(ip_block):
    data = {}


    addresses = get_ip_addresses_in_ip_range(ip_block)

    for address in addresses:
        try:
            hostname = get_hostname(address)
        except:
            pass
            hostname = None

        if hostname is not None:
            data.update({
                address: hostname
            })


    return data