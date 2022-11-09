import os

path1 = "~/.ssh/authorized_keys"
path2 = "/etc/ssh/sshd_config"
if os.path.isfile(path1):
    print("OK")
else:
    print("NO")

if os.path.isfile(path2):
    print("OK")
    f = open(path2, "r")
    contexts = f.read()
    if "PasswordAuthentication no" in contexts:
        print("OK")
    f.close()
else:
    print("NO")