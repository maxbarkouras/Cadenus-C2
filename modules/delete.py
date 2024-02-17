def delete():
    name = raw.split(" ")
    if os.path.exists(name[1]):
        if "." in name[1]:
            os.remove(name[1])
            s.sendall(("file has been deleted").encode("UTF-8"))
        elif "." not in raw:
            try:
                shutil.rmtree(name[1])
                s.sendall(("directory has been deleted").encode("UTF-8"))
            except:
                s.sendall(("file in folder is open in an application. cannot be deleted").encode("UTF-8"))
                pass
    else:
        s.sendall(("file does not exit").encode("UTF-8"))