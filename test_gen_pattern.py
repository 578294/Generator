BASE = '''
import paramiko
import time

class ConnectGenerator:
    def __init__(self, username, hostname, port, password):
        self.username = username
        self.hostname = hostname
        self.port = port
        self.password = password
        self.client = None
        self.connect_with_retry()

    def connect_with_retry(self, retries=3, delay=5):
        for attempt in range(retries):
            try:
                self.client = paramiko.SSHClient()
                self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                print(f"Attempt {attempt + 1} of {retries} to connect...")
                self.client.connect(
                    hostname=self.hostname,
                    port=int(self.port),
                    username=self.username,
                    password=self.password,
                    timeout=10,
                    allow_agent=False,
                    look_for_keys=False,
                    banner_timeout=30
                )
                print("Successfully connected to SSH server")
                return
            except paramiko.AuthenticationException:
                print("Authentication failed, please check your credentials")
                raise
            except paramiko.SSHException as e:
                print(f"SSH connection failed: {str(e)}")
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
            except Exception as e:
                print(f"Unexpected error: {str(e)}")
                if attempt == retries - 1:
                    raise
                time.sleep(delay)
'''

SSH = '''
    def ssh_ip(self):
        print("SSH Command: ssh {username}@{hostname} -p {port}".format(
            username=self.username,
            hostname=self.hostname,
            port=self.port
        ))
'''

PING = '''
    def ping_ip(self):
        stdin, stdout, stderr = self.client.exec_command('ping -c 4 {hostname}'.format(
            hostname=self.hostname
        ))
        print("PING Results:")
        print(stdout.read().decode())
'''

IFCONFIG = '''
    def ifconfig_ip(self):
        stdin, stdout, stderr = self.client.exec_command('ifconfig')
        print("Network Interfaces:")
        print(stdout.read().decode())
'''

NETSTAT = '''
    def netstat_ip(self):
        stdin, stdout, stderr = self.client.exec_command('netstat -tulpn')
        print("Active Connections:")
        print(stdout.read().decode())
'''

NMAP = '''
    def nmap_ip(self):
        stdin, stdout, stderr = self.client.exec_command('nmap -p 22 {hostname}'.format(hostname=self.hostname))
        print("Port Scan Results:")
        print(stdout.read().decode())
'''

DF = '''
    def df_ip(self):
        stdin, stdout, stderr = self.client.exec_command('df -h')
        print("Disk Usage:")
        print(stdout.read().decode())
'''

HTOP = '''
    def htop_ip(self):
        stdin, stdout, stderr = self.client.exec_command('htop')
        print("Processes:")
        print(stdout.read().decode())
'''

UNAME = '''
    def uname_ip(self):
        stdin, stdout, stderr = self.client.exec_command('uname -a')
        print("System Info:")
        print(stdout.read().decode())
'''

LSB_RELEASE = '''
    def lsb_release_ip(self):
        stdin, stdout, stderr = self.client.exec_command('lsb_release -a')
        print("OS Release:")
        print(stdout.read().decode())
'''

FREE = '''
    def free_ip(self):
        stdin, stdout, stderr = self.client.exec_command('free -h')
        print("Memory Usage:")
        print(stdout.read().decode())
'''

UPTIME = '''
    def uptime_ip(self):
        stdin, stdout, stderr = self.client.exec_command('uptime')
        print("Uptime:")
        print(stdout.read().decode())
'''

WHOIS = '''
    def whois_ip(self):
        stdin, stdout, stderr = self.client.exec_command('whois {hostname}'.format(hostname=self.hostname))
        print("Whois Info:")
        print(stdout.read().decode())
'''

LSCPU = '''
    def lscpu_ip(self):
        stdin, stdout, stderr = self.client.exec_command('lscpu')
        print("CPU Info:")
        print(stdout.read().decode())
'''

LSBLK = '''
    def lsblk_ip(self):
        stdin, stdout, stderr = self.client.exec_command('lsblk')
        print("Block Devices:")
        print(stdout.read().decode())
'''

JOURNALCTL = '''
    def journalctl_ip(self):
        stdin, stdout, stderr = self.client.exec_command('journalctl -xe --no-pager')
        print("System Logs:")
        print(stdout.read().decode())
'''

DMESG = '''
    def dmesg_ip(self):
        stdin, stdout, stderr = self.client.exec_command('dmesg')
        print("Kernel Messages:")
        print(stdout.read().decode())
'''

VMSTAT = '''
    def vmstat_ip(self):
        stdin, stdout, stderr = self.client.exec_command('vmstat 1 5')
        print("VM Statistics:")
        print(stdout.read().decode())
'''

OBJ_CREATE = '''
gen = ConnectGenerator(username='{username}', hostname='{hostname}', port={port}, password='{password}')
'''

CALL_SSH = '''
gen.ssh_ip()
'''

CALL_PING = '''
gen.ping_ip()
'''

CALL_IFCONFIG = '''
gen.ifconfig_ip()
'''

CALL_NETSTAT = '''
gen.netstat_ip()
'''

CALL_NMAP = '''
gen.nmap_ip()
'''

CALL_DF = '''
gen.df_ip()
'''

CALL_HTOP = '''
gen.htop_ip()
'''

CALL_UNAME = '''
gen.uname_ip()
'''

CALL_LSB_RELEASE = '''
gen.lsb_release_ip()
'''

CALL_FREE = '''
gen.free_ip()
'''

CALL_UPTIME = '''
gen.uptime_ip()
'''

CALL_WHOIS = '''
gen.whois_ip()
'''

CALL_LSCPU = '''
gen.lscpu_ip()
'''

CALL_LSBLK = '''
gen.lsblk_ip()
'''

CALL_JOURNALCTL = '''
gen.journalctl_ip()
'''

CALL_DMESG = '''
gen.dmesg_ip()
'''

CALL_VMSTAT = '''
gen.vmstat_ip()
'''
