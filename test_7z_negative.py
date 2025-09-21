from checkout import checkout_negative

folder_out = "/Users/darkwolf/Desktop/tst/badarx"
folder_ext = "/Users/darkwolf/Desktop/tst/ext"


def test_step1():
    # test1
    assert checkout_negative(f"cd {folder_out}; 7z e badarx.7z -o{folder_ext} -y", "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert checkout_negative(f"cd {folder_out}; 7z t badarx.7z", "ERROR"), "Test5 Fail"
