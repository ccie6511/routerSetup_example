import netmiko
import config

print(config.devices)
print(config.login_info)

config_sets = [[
    'router ospf 100',
    'network 192.168.12.0 0.0.0.255 area 0',
    'network 1.1.1.1 0.0.0.0 area 0'
], [
    'router ospf 100',
    'network 192.168.12.0 0.0.0.255 area 0',
    'network 192.168.23.0 0.0.0.255 area 0',
    'network 2.2.2.2 0.0.0.0 area 0'
], [
    'router ospf 100',
    'network 192.168.23.0 0.0.0.255 area 0',
    'network 3.3.3.3 0.0.0.0 area 0'
]]

for i in range(len(config.devices)):
    config.login_info['host'] = config.devices[i]
    conn = netmiko.ConnectHandler(**config.login_info)
    print(conn.enable())
    print(conn.send_config_set(config_sets[i]))
    conn.disconnect()

print('OSPF 100 setup completed!!')
