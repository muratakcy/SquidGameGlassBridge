'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
satir=20
sutun=2
para=0
liste=[[0 for i in range(sutun)]for j in range(satir)]
print()
for i in range(20):
	bomba=random.randint(0,1)
	liste[i][bomba]=1
print("Bombalı Zemin")
print()
print(liste)

for i in range(20):
	tercih=int(input("tercih 1-2 :"))
	if liste[i][tercih-1]==0:
		para=para+1
	else:
	    print("ölmeseydin kazanacagın para :"+str(para))
	    para=0
	    break
	
if para !=0:
	print(para)
else:
    print("öldün")
