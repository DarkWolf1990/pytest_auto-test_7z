from load_file import upload_files
from checkout import ssh_checkout


def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "11",
                 "/tests/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "11",
                            "echo '11' | sudo -S dpgk -i home/user2/p7zip-full.deb", "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "11",
                            "echo '11' | sudo sudo -S dpkg -s p7zip-full", "Status: install ok installed"))
    return all(res)


if deploy():
    print("Deploy Successful")
else:
    print("Deploy Error")
