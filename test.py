import random
import os
from test_gen_pattern import (BASE, SSH, PING, IFCONFIG, CALL_SSH, CALL_PING,
                              CALL_IFCONFIG, OBJ_CREATE)


class ConnectGenerator:
    def settings(self):
        print(
            "Выберите действия (через запятую):\n1 - ssh\n2 - ping\n3 - ifconfig")
        self.actions = input("> ").strip().split(',')
        self.username = input('Введите имя пользователя: ')
        self.hostname = input('Введите IP-адрес: ')
        self.port = input('Укажите порт: ')
        self.password = input('Укажите пароль: ')

    def generate(self):
        calls = []
        os.makedirs('generate', exist_ok=True)
        filename = f'generate/NPC_{random.randint(1000, 9999)}.py'

        with open(filename, 'w') as file:
            file.write(BASE)
            if '1' in self.actions:
                file.write(
                    SSH.format(username=self.username, hostname=self.hostname))
                calls.append(CALL_SSH)
            if '2' in self.actions:
                file.write(PING.format(hostname=self.hostname))
                calls.append(CALL_PING)
            if '3' in self.actions:
                file.write(IFCONFIG)
                calls.append(CALL_IFCONFIG)

            file.write(OBJ_CREATE.format(
                username=self.username,
                hostname=self.hostname,
                port=self.port,
                password=self.password
            ))
            file.write(''.join(calls))

        print(f"\nФайл {filename} успешно создан!")
        print("Для запуска выполните команду в терминале:")
        print(f"python {filename}")


if __name__ == "__main__":
    gen = ConnectGenerator()
    gen.settings()
    gen.generate()