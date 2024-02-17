def quit():
    s.sendall(("connection successfully closed").encode("UTF-8"))
    s.close()
    sys.exit()