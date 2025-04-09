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

        client.connect(hostname, port, username, password)        
'''

SSH = '''
    def ssh_ip(self):
        return "ssh {}@{}" 
'''

PING = '''
    def ping_ip(self):
        return "ping {}@{}"
'''

IFCONFIG = '''
    def ifconfig_ip(self):
        stdin, stdout, stderr = client.exec_command('ls -la')
        print("Результат выполнения команды:", stdout.read().decode())
'''

OBJ_CREATE = '''
gen = ConnectGenerator('{}', '{}', '{}', '{}')
'''

CALL_SSH = '''
    print(gen.username())
'''

CALL_PING = '''
    print(calc.sub_number())
'''

CALL_IFCONFIG = '''
gen.ifconfig_ip()
'''