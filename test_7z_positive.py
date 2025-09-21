from checkout import checkout_positive

folder_in = "/Users/darkwolf/Desktop/tst/file"
folder_out = "/Users/darkwolf/Desktop/tst/out"
folder_ext = "/Users/darkwolf/Desktop/tst/ext"


def test_step1(make_folders, clear_folders, make_files):
    # test1
    res1 = checkout_positive(f"cd {folder_in}; 7z a {folder_out}/arx1.7z",
                             "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive(f"ls {folder_out}",
                             "arx.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    # test2
    res = []
    res.append(checkout_positive(
        f"cd {folder_in}; 7z a {folder_out}/arx1.7z",
        "Everything is Ok"))
    res.append(checkout_positive(
        f"cd {folder_out}; 7z e arx1.7z -o{folder_ext} -y",
        "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive(f"ls {folder_ext}", ""))
    assert all(res)


def test_step3():
    # test3
    assert checkout_positive(
        f"cd {folder_in}; 7z t {folder_out}/arx1.7z",
        "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert checkout_positive(
        f"cd {folder_in}; 7z u {folder_out}/arx1.7z",
        "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files):
    # test5
    res = []
    res.append(checkout_positive(
        f"cd {folder_in}; 7z a {folder_out}/arx1.7z",
        "Everything is Ok"))
    for item in make_files:
        res.append(
            checkout_positive(f"cd {folder_out}; 7z l arx1.7z", item))
    assert all(res)


# def test_step6():


def test_step7():
    assert checkout_positive(f"7z d {folder_out}/arx1.7z",
                             "Everything is Ok"), "Test1 Fail"
