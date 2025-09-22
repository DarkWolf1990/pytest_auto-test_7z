import subprocess
from datetime import datetime
import os
import random
import string
import pytest
from checkout import checkout_positive
import yaml

with open(os.path.join(os.path.dirname(__file__), "config.yaml")) as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout_positive(
        f"mkdir {data['folder_in']} {data['folder_out']} {data['folder_ext']} {data['folder_badarx']} {data['folder_ext2']}",
        "")


@pytest.fixture()
def clear_folders():
    return checkout_positive(
        f"rm -rf {data['folder_in']}/* {data['folder_out']}/* {data['folder_ext']}/* {data['folder_badarx']}/*  {data['folder_ext2']}/*",
        "")


@pytest.fixture()
def make_files():
    list_off_files = []

    for i in range(data['count']):
        filename = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                f"cd {data['folder_in']}; dd if=/dev/urandom of={filename} bs=1M count=1 iflag=fullblock",
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive(
            f"cd {data['folder_in']}; mkdir {subfoldername}", ""):
        return None, None
    if not checkout_positive(
            f"cd {data['folder_in']}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs=1M count=1 iflag=fullblock"
            , ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_bad_arx(make_folders, clear_folders, make_files):
    checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_badarx']}/badarx1.7z",
        "Everything is Ok"), "Test1 Fail"
    return checkout_positive(
        f"cd truncate -s 1 {data['folder_badarx']}/badarx1.7z",
        ""), "Test1 Fail"


@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m %d %H:%M:%S")


@pytest.fixture()
def save_log(start_time, name=data['path_journal']):
    with open(os.path.join(os.path.dirname(__file__), name), "w") as f:
        f.write(
            subprocess.run(f"sudo journalctl -s -u {start_time}", shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, encoding="utf-8").stdout)
