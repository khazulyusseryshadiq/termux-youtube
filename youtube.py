#Author by Khazul Yussery Shadiq
#Yuk dengerin Musik

import os
import sys
import time
import requests
import mechanize
import random

def runn(s):
    for khazul in s + '\n':
        sys.stdout.write(khazul)
        sys.stdout.flush()
        time.sleep(100. / 2100)

def welcome():
    os.system('clear')
    print "\033[1;32m         ---    ---                       "
    print "\033[1;32m         \  \__/  /                       "
    print "\033[1;32m          \      /      YOUTUBE           "
    print "\033[1;32m           \ YY /              ON         "
    print "\033[1;32m            \  /                COMMAND   "
    print "\033[1;32m            |  |    ---  BY               "
    print "\033[1;32m            |  |    | |    KHAZUL         "
    print "\033[1;32m            |__|    | |         YUSSERY   "
    print "\033[1;32m                ,---| |---, SHADIQ        "
    print "\033[1;32m                '---'-'---'               "
    print "\033[1;32m                    '  '---,              "
    print "\033[1;32m                     \_____'              "
    print "\033[1;33m =================[YOUTUBE.COM]=================="
welcome()

def awal():
    runn ("\033[1;34m      Powered by Khazul Yussery Shadiq ")
    runn ("\033[1;34m                   Hacking is Illusion ")
    time.sleep(1.5)
awal()

def pil():
    print " "
    print "\033[1;31m Ketikan Mulai Untuk Menampilkan Menjalankan "
    pilihan = raw_input("\033[1;36m <+>@khazul&Fadya ~# : ")
    if pilihan == "Mulai" or pilihan == "mulai":
             print " "
             time.sleep(1.5)
             os.system('bash requirements.sh')
             os.system('clear')
             os.system('mpsyt')
pil()
