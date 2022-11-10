import os
import subprocess

flag = True

path1 = "/root/.ssh/authorized_keys"
path2 = "/etc/ssh/sshd_config"
if os.path.isfile(path1):
    f = open(path1, "r")
    contexts = f.read()
    if contexts.find("ssh-rsa") != -1:
        pass
    else:
        flag = False
else:
    flag = False


res = subprocess.call('systemctl restart sshd', shell=True)
if res == 0:
    pass
else:
    flag == False

# print(os.access(path1, os.R_OK))
# print(os.access(path1, os.W_OK))
# print(os.access(path1, os.X_OK))

if os.path.isfile(path2):
    f = open(path2, "r")
    contexts = f.read()
    if "PasswordAuthentication no" in contexts:
        pass
    else:
        flag = False
    f.close()
else:
    flag = False

if flag:
    print("ok")
else:
    print("error")