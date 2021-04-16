import random
from random import choice
#loop menu hh
v = 0
for v in range(100):
 def createpass(data):
    password = ''
    char = "fessuoymohamedldor"
    for i in range(data):
        password += choice(char)
    return password
import os
lm = ['@gmail.com','@yahoo.com']
x=random.choice(lm)
os.system('clear')
os.system('pkg install figlet')
os.system('figlet Email-Ness')
os.system('>Emls.txt')
for v in range(100):
 ssl = open('Emls.txt',"a")
 ssl.write("\n" +createpass(6) +x)
 ssl.write("\n" +createpass(7) +x)
ssl.close()
