import os

import yaml

from checkout import ssh_checkout
from load_file import upload_files

with open(os.path.join(os.path.dirname(__file__), "config.yaml")) as f:
    data = yaml.safe_load(f)


def deploy():
    res = []
    upload_files(data['host'], data['user'], data['passwd'],
                 data['local_path'], data['remote_path'])
    res.append(ssh_checkout(data['host'], data['user'], data['passwd'],
                            f"echo {data['passwd']} | sudo -S dpgk -i {data['remote_path']}",
                            "Настраивается пакет"))
    res.append(ssh_checkout(data['host'], data['user'], data['passwd'],
                            f"echo {data['passwd']} | sudo sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


if deploy():
    print("Deploy Successful")
else:
    print("Deploy Error")
