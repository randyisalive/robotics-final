import sys

# check whether pc macOS or Windows
def check_os():
    if sys.platform.startswith('win'): # for windows
        arduino_port = "COM2"
    elif sys.platform.startswith('darwin'): # for MacOS
        arduino_port = "/dev/cu.wchusbserial1410"
    return arduino_port
