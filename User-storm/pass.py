import random
from random import choice
#loop menu hh
v = 0
for v in range(100):
 def createpass(data):
    password = ''
    char = "numoabsirvyx213456780"
    for i in range(data):
        password += choice(char)
    return password
import os
os.system('clear')
os.system('pkg install figlet')
os.system('figlet storm-ness')
os.system('>Pas.txt')
for v in range(100):
 ssl = open('Pas.txt',"a")
 ssl.write("\n" +createpass(7))
ssl.close()
