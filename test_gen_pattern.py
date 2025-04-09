BASE = '''
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class ConnectGenerator:
    def __init__(self, username, hostname, port, password):
        self.username = username
        self.hostname = hostname
        self.port = port
        self.password = password
        client.connect(hostname, port=int(port), username=username, password=password)
'''

SSH = '''
    def ssh_ip(self):
        return "ssh {username}@{hostname}"
'''

PING = '''
    def ping_ip(self):
        return "ping {hostname}"
'''

IFCONFIG = '''
    def ifconfig_ip(self):
        stdin, stdout, stderr = client.exec_command('ls -la')
        print("Результат выполнения команды:", stdout.read().decode())
'''

OBJ_CREATE = '''
gen = ConnectGenerator(username='{username}', hostname='{hostname}', port={port}, password='{password}')
'''

CALL_SSH = '''
print(gen.ssh_ip())
'''

CALL_PING = '''
print(gen.ping_ip())
'''

CALL_IFCONFIG = '''
gen.ifconfig_ip()
'''