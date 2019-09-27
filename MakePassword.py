# -*- coding: UTF-8 -*-
#!/usr/bin/python

from random import choice

zhi=["!","@","#","$","%","^","&","*","1","2","3","4","5","6","7","8","9","0","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",]
count=20
p=""
for x in range(0,count):
	p+=choice(zhi)
print(p)
