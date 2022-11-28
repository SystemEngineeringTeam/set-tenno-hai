import paramiko

with paramiko.SSHClient() as ssh:
    # 初回ログイン時に「Are you sure you want to continue connecting (yes/no)?」と
    # きかれても問題なく接続できるように。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh接続
    ssh.connect('127.0.0.1', port=22222, username='root', password='root')

    # コマンド実行
    stdin, stdout, stderr = ssh.exec_command('ls -al')

    # コマンド実行後に標準入力が必要な場合
    # stdin.write('password\n')
    # stdin.flush()

    # 実行結果を表示
    for o in stdout:
        print('[std]', o, end='')
    for e in stderr:
        print('[err]', e, end='')