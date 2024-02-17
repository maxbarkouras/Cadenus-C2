def dl():
    import os
    filename = raw.split(' ')[1]
    filesize = os.path.getsize(filename)
    s.sendall((filename + '<sep>' + str(filesize)).encode('UTF-8'))
    time.sleep(0.1)
    f = open(filename, 'rb')
    while True:
        filebytes = f.read(20480)
        if filebytes == b'':
            s.sendall(b'five')
            f.close()
            break
        else:
            s.sendall(filebytes)
            time.sleep(0.1)