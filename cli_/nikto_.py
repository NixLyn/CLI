# LOCAL
from File_man import File_Man


# SYS_BASE
import subprocess
from threading import Thread
import time


class Nikto_Scan():
    def __init__(self, **kw):
        super(Nikto_Scan, self).__init__(**kw)
        self.FM         = File_Man()



    def main(self, **args):
        try:
            print(str(args))
        except Exception as e:
            print(f"[E]:[NIKTO_SCAN]:[{str(e)}]")

