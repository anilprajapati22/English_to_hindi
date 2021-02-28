#sgnons importing the module 
from os import listdir
from os.path import isfile, join
from englisttohindi.englisttohindi import EngtoHindi 
import os
mypath="/home/anilprajapati/Music/sgn"

s = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(s)
for i in s:
    print("coverting...",i)
    message = i
    message.replace("_"," ")
    res = EngtoHindi(message)
    sgn=res.convert
    if type(sgn) == str :
        if len(sgn) < 40 :
            sgn1 = sgn[0:len(sgn)-4] + i[-4:] 
        else:
            sgn1 = sgn[0:len(sgn)-20] + i[-4:]      
        print(sgn1)  
        os.rename(mypath+"/"+i,mypath+"/"+sgn1)
        print("next....")
    
# creating a EngtoHindi() object 
 
  
# displaying the translation 


