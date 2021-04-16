import random
from random import choice
#loop menu hh
v = 0
for v in range(100):
 def createpass(data):
    password = ''
    char = "qpvsapzvaozvwosvs207297201277"
    for i in range(data):
        password += choice(char)
    return password
import os
os.system('clear')
os.system('pkg install figlet')
os.system('figlet User-storm')
os.system('>Usr.txt')
for v in range(100):
 ssl = open('Usr.txt',"a")
 ssl.write("\n" +createpass(6))
ssl.close()

