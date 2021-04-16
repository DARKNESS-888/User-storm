import random
from random import choice
#loop menu hh
v = 0
for v in range(100):
 def createpass(data):
    password = ''
    char = "01234567890"
    for i in range(data):
        password += choice(char)
    return password
import os
os.system('clear')
os.system('pkg install figlet')
os.system('figlet Done!')
os.system('>Auto__int__Num.txt')
for v in range(500):
 fromm = input ('Enter the country code: +')
 ssl = open('Auto__int__Num.txt',"a")
 codec = "+"
 ssl.write("\n" +codec +fromm +createpass(10))
ssl.close()

