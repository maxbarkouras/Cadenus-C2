def upies():
    upfile = raw.split('<up>')[0]
    upsize = raw.split('<up>')[1]
    f = open(upfile, 'wb')
    while True:
        upbytes = s.recv(20480)
        if upbytes == b'loser':
            f.close()
            break
        else:
            f.write(upbytes)