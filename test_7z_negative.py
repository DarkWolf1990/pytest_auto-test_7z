import os
from checkout import checkout_negative
import yaml

with open(os.path.join(os.path.dirname(__file__), "config.yml")) as f:
    data = yaml.safe_load(f)

def test_step1():
    # test1
    assert checkout_negative(f"cd {data["{folder_out_negative}"]}; 7z e badarx.7z -o{data["{folder_ext}"]} -y", "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert checkout_negative(f"cd {data["{folder_out}"]}; 7z t badarx.7z", "ERROR"), "Test5 Fail"
