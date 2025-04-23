"""
Модуль test_gen_pattern.py содержит строковые шаблоны
для генерации Python-скриптов, которые выполняют диагностику
удаленного сервера через SSH-соединение.

Все шаблоны разделены на:
- BASE: основной шаблон с классом ConnectGenerator
  для подключения по SSH
- Командные шаблоны (SSH, PING, IFCONFIG и др.): методы
  для выполнения конкретных команд
- Шаблоны вызовов (CALL_SSH, CALL_PING и др.):
  код для вызова соответствующих методов
- OBJ_CREATE: шаблон для создания экземпляра ConnectGenerator
"""

# Основной шаблон класса для SSH-подключения
BASE = '''
import paramiko
import time

class ConnectGenerator:
    """Основной класс для установки SSH-соединения с удаленным сервером."""
    def __init__(self, username: str, hostname: str, port: str, password: str) -> None:
        """Инициализирует подключение к SSH серверу."""
        self.username = username
        self.hostname = hostname
        self.port = port
        self.password = password
        self.client = None
        self.connect_with_retry()

    def connect_with_retry(self, retries: int = 3, delay: int = 5) -> None:
        """
        Устанавливает соединение с сервером с повторными попытками при ошибках.
        """
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

# Шаблон метода для отображения SSH команды подключения
SSH: str = '''
    def ssh_ip(self) -> None:
        print("SSH Command: ssh {username}@{hostname} -p {port}".format(
            username=self.username,
            hostname=self.hostname,
            port=self.port
        ))
'''

# Шаблон метода для выполнения команды ping
PING: str = '''
    def ping_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('ping -c 4 {hostname}'.format(
            hostname=self.hostname
        ))
        print("PING Results:")
        print(stdout.read().decode())
'''

# Шаблон метода для отображения сетевых интерфейсов
IFCONFIG: str = '''
    def ifconfig_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('ifconfig')
        print("Network Interfaces:")
        print(stdout.read().decode())
'''

# Шаблон метода для просмотра активных соединений
NETSTAT: str = '''
    def netstat_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('netstat -tulpn')
        print("Active Connections:")
        print(stdout.read().decode())
'''

# Шаблон метода для сканирования портов
NMAP: str = '''
    def nmap_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('nmap -p 22 {hostname}'.format(hostname=self.hostname))
        print("Port Scan Results:")
        print(stdout.read().decode())
'''

# Шаблон метода для анализа дискового пространства
DF: str = '''
    def df_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('df -h')
        print("Disk Usage:")
        print(stdout.read().decode())
'''

# Шаблон метода для мониторинга процессов
HTOP: str = '''
    def htop_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('htop')
        print("Processes:")
        print(stdout.read().decode())
'''

# Шаблон метода для получения системной информации
UNAME: str = '''
    def uname_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('uname -a')
        print("System Info:")
        print(stdout.read().decode())
'''

# Шаблон метода для получения информации о дистрибутиве
LSB_RELEASE: str = '''
    def lsb_release_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('lsb_release -a')
        print("OS Release:")
        print(stdout.read().decode())
'''

# Шаблон метода для анализа использования памяти
FREE: str = '''
    def free_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('free -h')
        print("Memory Usage:")
        print(stdout.read().decode())
'''

# Шаблон метода для проверки времени работы системы
UPTIME: str = '''
    def uptime_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('uptime')
        print("Uptime:")
        print(stdout.read().decode())
'''

# Шаблон метода для WHOIS запроса
WHOIS: str = '''
    def whois_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('whois {hostname}'.format(hostname=self.hostname))
        print("Whois Info:")
        print(stdout.read().decode())
'''

# Шаблон метода для получения информации о CPU
LSCPU: str = '''
    def lscpu_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('lscpu')
        print("CPU Info:")
        print(stdout.read().decode())
'''

# Шаблон метода для анализа блочных устройств
LSBLK: str = '''
    def lsblk_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('lsblk')
        print("Block Devices:")
        print(stdout.read().decode())
'''

# Шаблон метода для просмотра системных логов
JOURNALCTL: str = '''
    def journalctl_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('journalctl -xe --no-pager')
        print("System Logs:")
        print(stdout.read().decode())
'''

# Шаблон метода для просмотра сообщений ядра
DMESG: str = '''
    def dmesg_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('dmesg')
        print("Kernel Messages:")
        print(stdout.read().decode())
'''

# Шаблон метода для мониторинга виртуальной памяти
VMSTAT: str = '''
    def vmstat_ip(self) -> None:
        stdin, stdout, stderr = self.client.exec_command('vmstat 1 5')
        print("VM Statistics:")
        print(stdout.read().decode())
'''

# Шаблон для создания объекта ConnectGenerator
OBJ_CREATE: str = '''
gen = ConnectGenerator(username='{username}', hostname='{hostname}', port={port}, password='{password}')
'''

# Шаблоны вызовов методов для SSH
CALL_SSH: str = '''
gen.ssh_ip()
'''

# Шаблон вызова метода для проверки доступности хоста
CALL_PING: str = '''
gen.ping_ip()
'''

# Шаблон вызова метода для просмотра сетевых интерфейсов
CALL_IFCONFIG: str = '''
gen.ifconfig_ip()
'''

# Шаблон вызова метода для просмотра активных соединений
CALL_NETSTAT: str = '''
gen.netstat_ip()
'''

# Шаблон вызова метода для сканирования портов
CALL_NMAP: str = '''
gen.nmap_ip()
'''

# Шаблон вызова метода для анализа дискового пространства
CALL_DF: str = '''
gen.df_ip()
'''

# Шаблон вызова метода для мониторинга процессов
CALL_HTOP: str = '''
gen.htop_ip()
'''

# Шаблон вызова метода для получения системной информации
CALL_UNAME: str = '''
gen.uname_ip()
'''

# Шаблон вызова метода для информации о дистрибутиве
CALL_LSB_RELEASE: str = '''
gen.lsb_release_ip()
'''

# Шаблон вызова метода для анализа использования памяти
CALL_FREE: str = '''
gen.free_ip()
'''

# Шаблон вызова метода для проверки времени работы системы
CALL_UPTIME: str = '''
gen.uptime_ip()
'''

# Шаблон вызова метода для WHOIS запроса
CALL_WHOIS: str = '''
gen.whois_ip()
'''

# Шаблон вызова метода для информации о процессоре
CALL_LSCPU: str = '''
gen.lscpu_ip()
'''

# Шаблон вызова метода для анализа блочных устройств
CALL_LSBLK: str = '''
gen.lsblk_ip()
'''

# Шаблон вызова метода для просмотра системных логов
CALL_JOURNALCTL: str = '''
gen.journalctl_ip()
'''

# Шаблон вызова метода для просмотра сообщений ядра
CALL_DMESG: str = '''
gen.dmesg_ip()
'''

# Шаблон вызова метода для мониторинга виртуальной памяти
CALL_VMSTAT: str = '''
gen.vmstat_ip()
'''
