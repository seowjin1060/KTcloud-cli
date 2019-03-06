#!/usr/bin/env python
import codecs
import os.path
import re
import sys
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

ucloud_path = here.replace("/bin"," ")
def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

def command(path_bin):
    print(path_bin)
    os.system("chmod +x ../ucloud")
    #os.system("echo"+ "'export PATH=" + '$PATH":'+ucloud_path+ :"'+"'" + ">> ~/.bashrc" )
    os.system("echo "+ "'export PATH=" + '$PATH":'+ucloud_path+ '"'+"'" + ">> ~/.bashrc")

command(here)
