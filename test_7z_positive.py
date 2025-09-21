import os
from checkout import checkout_positive
import yaml

with open(os.path.join(os.path.dirname(__file__), "config.yaml")) as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files):
    # test1
    res1 = checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive(f"ls {data['folder_out']}",
                             "arx1.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"))
    res.append(checkout_positive(
        f"cd {data['folder_out']}; 7z e arx1.7z -o{data['folder_ext']} -y",
        "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive(f"ls {data['folder_ext']}", item))
    assert all(res)


def test_step3(make_folders, clear_folders, make_files):
    # test3
    assert checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"), "Test3 Fail"
    assert checkout_positive(
        f"cd {data['folder_in']}; 7z t {data['folder_out']}/arx1.7z",
        "Everything is Ok"), "Test3 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert checkout_positive(
        f"cd {data['folder_in']}; 7z u {data['folder_out']}/arx1.7z",
        "Everything is Ok"), "Test4 Fail"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"))
    for item in make_files:
        res.append(
            checkout_positive(f"cd {data['folder_out']}; 7z l arx1.7z",
                              item))
    assert all(res)


def test_step6(make_folders, clear_folders, make_files, make_subfolder):
    res = []
    res.append(checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"))
    res.append(
        checkout_positive(
            f"cd {data['folder_out']}; 7z x arx1.7z -o{data['folder_ext2']} -y",
            "Everything is Ok"))

    for item in make_files:
        res.append(checkout_positive(f"ls {data['folder_ext2']}", item))

    subfolder_name = make_subfolder[0]
    res.append(
        checkout_positive(f"ls {data['folder_ext2']}", subfolder_name))

    res.append(
        checkout_positive(f"ls {data['folder_ext2']}/{subfolder_name}",
                          make_subfolder[1]))

    assert all(res)


def test_step7(make_folders, clear_folders, make_files):
    # Сначала создаем архив
    assert checkout_positive(
        f"cd {data['folder_in']}; 7z a {data['folder_out']}/arx1.7z",
        "Everything is Ok"), "Test7 Fail"
    # Затем удаляем
    assert checkout_positive(f"7z d {data['folder_out']}/arx1.7z",
                             "Everything is Ok"), "Test7 Fail"