from flask import Flask, render_template, request, jsonify
from test import ConnectGenerator
import random
import os
from test_gen_pattern import (
    BASE, SSH, PING, IFCONFIG, NETSTAT, NMAP, DF, HTOP, UNAME,
    LSB_RELEASE, FREE, UPTIME, WHOIS, LSCPU, LSBLK, JOURNALCTL, DMESG, VMSTAT,
    CALL_SSH, CALL_PING, CALL_IFCONFIG, CALL_NETSTAT, CALL_NMAP, CALL_DF,
    CALL_HTOP, CALL_UNAME, CALL_LSB_RELEASE, CALL_FREE, CALL_UPTIME,
    CALL_WHOIS, CALL_LSCPU, CALL_LSBLK, CALL_JOURNALCTL, CALL_DMESG,
    CALL_VMSTAT,
    OBJ_CREATE
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index_page():
    return render_template("index1.html")


@app.route("/execute", methods=["POST"])
def execute_command():
    try:
        data = request.json
        gen = ConnectGenerator()
        gen.username = data["username"]
        gen.hostname = data["hostname"]
        gen.port = data.get("port", "22")
        gen.password = data["password"]
        action = data.get("action", "SSH")

        action_map = {
            'PING': '2',
            'IFCONFIG': '3',
            'SSH': '1',
            'NETSTAT': '4',
            'NMAP': '5',
            'DF': '6',
            'HTOP': '7',
            'UNAME': '8',
            'LSB_RELEASE': '9',
            'FREE': '10',
            'UPTIME': '11',
            'WHOIS': '12',
            'LSCPU': '13',
            'LSBLK': '14',
            'JOURNALCTL': '15',
            'DMESG': '16',
            'VMSTAT': '17'
        }

        gen.selected_actions = [action_map.get(action, '1')]
        gen.actions_map = {
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

        result = gen.generate()
        return jsonify({"status": "success", "output": result})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
