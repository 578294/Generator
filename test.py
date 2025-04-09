import random
from test_gen_pattern import (BASE, SSH, PING, IFCONFIG, CALL_SSH, CALL_IFCONFIG, OBJ_CREATE, CALL_PING)

class Connect:
    def __init__(self, username, hostname):
        self.username = username
        self.hostname = hostname

class Generator:

    def call_ssh(self):
        return CALL_SSH

    def call_ping(self):
        return CALL_PING


class ConnectGenerator:
    def settings(self):
        self.actions = input('Введите пользователя и ip-адрес через запятую:'
                             '\n1 - ssh'
                             '\n2 - ping'
                             '\n3 - ifconfig'
                             '\nВыбранные действия: ').split(', ')
        self.username = input('Введите имя пользователя: ')
        self.hostname = input('Введите ip-адрес: ')
        self.port = input('Укажите порт: ')
        self.password = input('укажите пароль: ')

    def generate(self):
        calls = []
        with open(f'generate/NPC_{random.randint(1000, 9999)}.py',
                  'w') as file:
            file.write(BASE)
            if '1' in self.actions:
                file.write(SSH.format(self.username, self.hostname))
                calls.append(CALL_SSH)
            elif '2' in self.actions:
                file.write(PING)
                calls.append(CALL_PING)
            elif '3' in self.actions:
                file.write(IFCONFIG)
                calls.append(CALL_IFCONFIG)

            file.write(OBJ_CREATE.format(self.username, self.hostname, self.port, self.password))
            calls = ''.join(calls)
            file.write(calls)


gen = ConnectGenerator()
gen.settings()
gen.generate()