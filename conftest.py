import random
import string
import subprocess
import pytest
from checkout import checkout_positive

folder_in = "/Users/darkwolf/Desktop/tst/file"
folder_out = "/Users/darkwolf/Desktop/tst/out"
folder_ext = "/Users/darkwolf/Desktop/tst/ext"
folder_badarx = "/Users/darkwolf/Desktop/tst/badarx"


@pytest.fixture()
def make_folders():
    return checkout_positive(
        f"mkdir {folder_in} {folder_out} {folder_ext} {folder_badarx}", "")


@pytest.fixture()
def clear_folders():
    return checkout_positive(
        f"rm -rf {folder_in}/* {folder_out}/* {folder_ext}/* {folder_badarx}/*",
        "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(5):
        filename = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                f"cd {folder_in}; dd if=/dev/urandom of={filename} bs=1M count=1 iflag=fullblock",
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
            f"cd {folder_in}; mkdir {subfoldername}", ""):
        return None, None
    if not checkout_positive(
            f"cd {folder_in}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs=1M count=1 iflag=fullblock"
            , ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename
