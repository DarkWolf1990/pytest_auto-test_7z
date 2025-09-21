import os
import random
import string
import subprocess
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
    for i in range(5):
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
