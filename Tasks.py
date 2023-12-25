import re
def text_Match(text):
    patterns= '[A-Z]+[a-z]+$'
    if re.search(patterns,text):
        return 'String matches as per requirement!'
    else:
        return('String does not match the requirement')
    
def z_Match(text):
    patterns='\w*z\w*'
    if re.search(pattern,text):
        return 'Character z found in the string'
    else:
        return('Given string does not contain charachter z')
    
def str_Match(text):
    patterns='^[a-zA-Z0-9_]*$'
    if re.search(patterns,text):
        return 'found a match!'
    else:
        return('Not matched!')
    
def removeZeros(ip):
    ip=re.sub('\.[0]*','.',ip)
    print('IP address after removing leading zeros',ip.lstrip('0'))
while(True):
    print('1.Find the sequencee of one upper case letter followed by lower case letters')
    print('2.Match a word containing letter z')
    print('3.Match a string that contains only upper and lowercase letters,numbers,underscores')
    print('4.To remove leading zeros from an IP adress')
    ch=int(input('Enter yout choice:'))
    if(ch==1):
        str=input('Enter a string:')
        print(text_Match(str))
    elif(ch==2):
        str=input('Enter a string:')
        print(str_Match(str))
    elif(ch==4):
        ip=input('Enter the IP address:')
        removeZeros(ip)
    else:
        print('Program terminated')
        break