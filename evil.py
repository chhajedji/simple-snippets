#!/usr/bin/env python3

import signal

def ctrlc_handler(signum, frame):
    print ("Not dying here.")


signal.signal(signal.SIGINT, ctrlc_handler)

print("Waiting for some signals from you ;)")

while True:
    pass
