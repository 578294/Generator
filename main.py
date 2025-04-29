"""
Основной модуль для генерации диагностических скриптов в CLI-режиме.

Класс ConnectGenerator предоставляет интерфейс для настройки
и генерации скриптов.
"""

import random
import os
from gen_pattern import (BASE, SSH, PING, IFCONFIG, NETSTAT, NMAP, DF,
                         HTOP, UNAME,
                         LSB_RELEASE, FREE, UPTIME, WHOIS, LSCPU, LSBLK,
                         JOURNALCTL, DMESG, VMSTAT,
                         CALL_SSH, CALL_PING, CALL_IFCONFIG, CALL_NETSTAT,
                         CALL_NMAP, CALL_DF,
                         CALL_HTOP, CALL_UNAME, CALL_LSB_RELEASE,
                         CALL_FREE, CALL_UPTIME,
                         CALL_WHOIS, CALL_LSCPU, CALL_LSBLK,
                         CALL_JOURNALCTL, CALL_DMESG, CALL_VMSTAT,
                         OBJ_CREATE)


class ConnectGenerator:
    """Класс для генерации Python-скриптов диагностики сервера."""

    def settings(self) -> None:
        """Запрашивает у пользователя настройки для генерации скрипта."""

        actions = [
            'SSH', 'PING', 'IFCONFIG', 'NETSTAT', 'NMAP', 'DF', 'HTOP',
            'UNAME', 'LSB_RELEASE', 'FREE', 'UPTIME', 'WHOIS', 'LSCPU',
            'LSBLK', 'JOURNALCTL', 'DMESG', 'VMSTAT'
        ]

        self.actions_map = {
            str(i + 1): (
                action, globals()[action], globals()[f'CALL_{action}'])
            for i, action in enumerate(actions)
        }

        print("Доступные действия (введите номера через запятую):")
        for num, (name, _, _) in self.actions_map.items():
            print(f"{num} - {name}")

        self.selected_actions = input("> ").strip().split(',')
        self.username = input('Введите имя пользователя: ')
        self.hostname = input('Введите IP-адрес/домен: ')
        self.port = input('Укажите порт (по умолчанию 22): ') or '22'
        self.password = input('Укажите пароль: ')

    def generate(self) -> str:
        """Генерирует Python-скрипт на основе выбранных настроек."""
        os.makedirs('generate', exist_ok=True)
        filename = f'generate/NPC_{random.randint(1000, 9999)}.py'

        with open(filename, 'w', encoding='utf-8') as file:
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
