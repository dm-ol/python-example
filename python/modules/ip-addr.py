# Коли доводиться писати на Python програми для роботи з мережею — варто звернути увагу на модуль ipaddress.
# Одним з варіантів його використання є генерація списку IP-адрес з діапазону адрес, заданих у форматі CIDR.
# https://docs.python.org/3/howto/ipaddress.html

import ipaddress

net = ipaddress.ip_network('74.125.227.0/25')
# IPv4Network('74.125.227.0/29')

for addr in net:
    print(addr)

# 74.125.227.0
# 74.125.227.1
# 74.125.227.2
# 74.125.227.3
# ...
