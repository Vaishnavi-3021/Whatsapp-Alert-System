import sys
import pywhatkit
import os
import time
import pyautogui as pg
import argparse  as argparser
from argparse import ArgumentParser
argParser = argparser.ArgumentParser()
argParser.add_argument("-n","--name",help="your name")
args=argParser.parse_args()
print(args.name)
pywhatkit.sendwhatmsg_to_group_instantly("Fl8oTLXsKdK447dHDYnH0U",args.name)
time.sleep(25)
try:
    os.system("taskkill /im msedge.exe /f")
except Exception:
    sys.exc_clear()