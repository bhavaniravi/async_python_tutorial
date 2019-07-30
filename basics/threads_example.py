import threading


def do_something():
    print ("Doing stuff...")


threading.Timer(10.0, do_something).start()
