#CONTRASEÑA ALEATORIA
import random as r
import string


num= string.digits
min= string.ascii_lowercase
may= string.ascii_uppercase
simb= string.punctuation


def rep(str1,str2):
    c = 0 
    for i in str1: 
        if i in str2:
            if str1.count(i) >= 2:
                return True
            if str1.count(i) == 1:
                if str2 == num :
                    c += 1
                    if c >= 4:
                        return False
                if str2 != num:
                    return False

def cons(str1,str2):
    for i in range(1,len(str1)):
        ant=str1[i-1:i]
        sig=str1[i:i+1]
        if sig in str2 and ant in str2:
            return True


c = 0
while c < 1:
    mix= ''.join(r.choice(num + min + may + simb) for x in range(0, r.randrange(11,16)))   
    if rep(mix,may) != None and rep(mix,num) == False and rep(mix,simb) != None \
    and rep(mix,min) != None and cons(mix,num) != True:
        c += 1

print(mix)


