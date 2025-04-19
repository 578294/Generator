import random
import os
from test_gen_pattern import (BASE, SSH, PING, IFCONFIG, NETSTAT, NMAP, DF, HTOP, UNAME,
    LSB_RELEASE, FREE, UPTIME, WHOIS, LSCPU, LSBLK, JOURNALCTL, DMESG, VMSTAT,
    CALL_SSH, CALL_PING, CALL_IFCONFIG, CALL_NETSTAT, CALL_NMAP, CALL_DF,
    CALL_HTOP, CALL_UNAME, CALL_LSB_RELEASE, CALL_FREE, CALL_UPTIME,
    CALL_WHOIS, CALL_LSCPU, CALL_LSBLK, CALL_JOURNALCTL, CALL_DMESG, CALL_VMSTAT,
    OBJ_CREATE)

class ConnectGenerator:

    def settings(self):
        self.actions_map = {
            '1': ('SSH', SSH, CALL_SSH),
            '2': ('PING', PING, CALL_PING),
            '3': ('IFCONFIG', IFCONFIG, CALL_IFCONFIG),
            '4': ('NETSTAT', NETSTAT, CALL_NETSTAT),
            '5': ('NMAP', NMAP, CALL_NMAP),
            '6': ('DF', DF, CALL_DF),
            '7': ('HTOP', HTOP, CALL_HTOP),
            '8': ('UNAME', UNAME, CALL_UNAME),
            '9': ('LSB_RELEASE', LSB_RELEASE, CALL_LSB_RELEASE),
            '10': ('FREE', FREE, CALL_FREE),
            '11': ('UPTIME', UPTIME, CALL_UPTIME),
            '12': ('WHOIS', WHOIS, CALL_WHOIS),
            '13': ('LSCPU', LSCPU, CALL_LSCPU),
            '14': ('LSBLK', LSBLK, CALL_LSBLK),
            '15': ('JOURNALCTL', JOURNALCTL, CALL_JOURNALCTL),
            '16': ('DMESG', DMESG, CALL_DMESG),
            '17': ('VMSTAT', VMSTAT, CALL_VMSTAT)
        }

        print("Доступные действия (введите номера через запятую):")
        for num, (name, _, _) in self.actions_map.items():
            print(f"{num} - {name}")

        self.selected_actions = input("> ").strip().split(',')
        self.username = input('Введите имя пользователя: ')
        self.hostname = input('Введите IP-адрес/домен: ')
        self.port = input('Укажите порт (по умолчанию 22): ') or '22'
        self.password = input('Укажите пароль: ')


    def generate(self):
            os.makedirs('generate', exist_ok=True)
            filename = f'generate/NPC_{random.randint(1000, 9999)}.py'

            with open(filename, 'w') as file:
                file.write(BASE)

                calls = []
                for action in self.selected_actions:
                    if action in self.actions_map:
                        _, template, call = self.actions_map[action]
                        if '{hostname}' in template:
                            file.write(template.format(hostname=self.hostname))
                        elif '{username}' in template:
                            file.write(template.format(
                                username=self.username,
                                hostname=self.hostname,
                                port=self.port
                            ))
                        else:
                            file.write(template)
                        calls.append(call)

                file.write(OBJ_CREATE.format(
                    username=self.username,
                    hostname=self.hostname,
                    port=self.port,
                    password=self.password
                ))
                file.write(''.join(calls))

            return (f"\nФайл {filename} успешно создан!"
                    f"\nДля запуска выполните: {filename}")


if __name__ == "__main__":
    gen = ConnectGenerator()
    gen.settings()
    gen.generate()