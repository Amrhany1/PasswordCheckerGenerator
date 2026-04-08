import math ,re
from secrets import choice
from string import ascii_letters , digits
from collections import Counter
def isLong(password):
    if len(password)>= 8:
        return True
    else:
        return False
password= "sfsdfds"
def isThereNumber(password):
    if any(char.isdigit() for char in password ):
        return True
    else:
        return False

def isThereAlpha(password):
    if any(char.isalpha() for char in password ):
        return True
    else:
        return False
    
def isThereLower(password):
    if any(char.islower() for char in password ):
        return True
    else:
        return False   

def isThereUpper(password):
    if any(char.isupper() for char in password ):
        return True
    else:
        return False

def isThereSymbols(password):
    if any(not char.isalnum() for char in password ):
        return True
    else:
        return False

def isPasswordComplex2(password):
    matchstr=re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,16}$",password)
    if matchstr !=None:
        print("Password is complex ")
        return True
    else:
        print("password is not complex")
        return False

def entropy(password):
    prob=[count / len(password) for count in Counter(password).values()]
    return -sum(p*math.log2(p) for p in prob)

def entropyScore(entropy):
    if entropy<=1.0:
        return 'Very weak password'
    elif entropy<=2.0:
        return 'Weak password'
    elif entropy <=3.0:
        return 'Meduim password'
    elif entropy <=4.0:
        return'Strong password'
    elif entropy<=5.0:
        return'Very strong password'
    else:
        return None



def isPasswordComplex(password):
    isComplex=0
    if isThereAlpha(password):
        if isThereUpper(password):
            isComplex+=1
        else:
            print("there is no upper case in the password")
        if isThereLower(password):
            isComplex+=1
        else:
            print("there is no lower case in the password")
    else:
        print("thre is no alpha in password")
    if isThereNumber(password):
        isComplex+=1
    else:
        print("there is no number")
    if isThereSymbols(password):
        isComplex+=1
    else:
        print("there is no symbols")
    if isLong(password):
        isComplex+=1
    else:
        print("password is less than 8 digit")
    if isComplex==5:
        return True
    else:
        return False
    
def generatePassword(n=12):
    passwordDomain=ascii_letters+digits+"!@#$%&*"
    password= "".join(choice(passwordDomain) for _ in range(n) )
    return password

password =input("Enter your password : ")

while password == None or not(isPasswordComplex(password)) :
    if password == None :
        print("Empty value !")
    else:
        print("Password is not complex !")
    password =input("Enter your password : ")
print(entropyScore(entropy(password)))
print(f"Recommended password : {generatePassword()} ")


