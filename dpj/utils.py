#  -*- coding: utf-8 -*-
from cryptography.fernet import Fernet,InvalidToken
from shutil import copy2
from random import shuffle
from string import ascii_letters,digits
from os import system,path,urandom #,getuid #<---Only for Linux/MacOSX
import glob, platform,re,keyboard, bcrypt,argparse,hashlib,time,hmac,base64
from json import loads
from secrets import choice
from sys import exit,stdout
from datetime import datetime
def KDF(Pass,Salt,bk,r):
    return  bcrypt.kdf(Pass,salt=Salt,desired_key_bytes=bk,rounds=r)


def dpj_e(data,key,iv):
    klen=len(key)  
    kiv=len(iv)
    data = bytearray([n ^ iv[c % kiv] for c, n in enumerate(data)]) 
    data=bytearray([n-key[c%klen] & 255 for c,n in enumerate(data)])      
    data=bytearray([(n^key[c%klen]) for c,n in enumerate(data)])          
    data=bytearray([n+key[c%klen] & 255 for c,n in enumerate(data)])
    return data
def dpj_d(data,key,iv):
    klen=len(key)  
    kiv=len(iv) 
    data=bytearray([n-key[c%klen] & 255 for c,n in enumerate(data)])      
    data=bytearray([(n^key[c%klen]) for c,n in enumerate(data)])          
    data=bytearray([n+key[c%klen] & 255 for c,n in enumerate(data)])
    data = bytearray([n ^ iv[c % kiv] for c, n in enumerate(data)]) 
    return data

def isZipmp3rarother(fname):
    r=Filehandle(fname,0,4)
    if r==b'Rar!' or b'PK' in r:
        r="";return 0.03
    elif b'ID3' in r:
        r="";return 0.20
    r="";return 0.02
def lprint(s):
    stdout.write(s)
    stdout.flush()
    return  
def Fn_clear(fname):
    for c in fname:
        if c not in ascii_letters+digits+" !@#$%^&-+;.~_éáíóúñÑ":
            fname=fname.replace(c,"")        
    return fname
def passhash(Pass ,Salt ):
    return bcrypt.hashpw(Pass,salt=Salt)
def checkpass(Pass,Passhashed):
    return bcrypt.checkpw(Pass,Passhashed)
def filesize(fname):
    f=open(fname,"rb");f.seek(0,2 );s=f.tell();f.close
    return s
def byteme(b):
    if b.isdigit():
        b=str(int(b))
        l=len(b)
        if l>=1 and l<4: exp=0;nb=" Bytes"
        if l>=4 and l<7: exp=1;nb=" KB"
        if l>=7 and l<10: exp=2;nb=" MB"
        if l>=10 and l<13: exp=3;nb=" GB"
        if l>=13 and l<16: exp=4;nb=" TB"
        if l>=16 and l<19: exp=5;nb=" PB"
        return str(round((int(b)/(1024**exp)),2))+nb
    return "Invalid digits"

def is_binary(fcontent):
     return (b'\x00' in fcontent)

def genpass(l,n,s):
    numbers=['0','1','2','3','4','5','6','7','8','9']
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special=['!','@','#','$','%','^','&','*','?']
    n_let=[choice(letters) for _ in range(l)]
    n_num=[choice(numbers) for _ in range(n)]
    n_spe=[choice(special) for _ in range(s)]        
    chars=n_let+n_num+n_spe
    shuffle(chars)
    return "".join(chars)

def keypress(key):
    keyboard.wait(key)
def ValidPass(Passwd):
    if Passwd=="q" or Passwd=="Q":return True
    if Passwd=="a" or Passwd=="A":return True
    if len(Passwd)>=12:
        if  re.search("[A-Z]",Passwd):
            if  re.search("[a-z]",Passwd): 
                if  re.search("[0-9]",Passwd): 
                    if  re.search("[@#$!%&]",Passwd):
                        return True
    return False
def recursive(par):
   lf=glob.glob("./"+par)
   lf2=glob.glob("./**/"+par)
   lf3=glob.glob("./**/**/"+par)
   lf4=glob.glob("./**/**/**/"+par)
   lf5=glob.glob("./**/**/**/**/"+par)
   lf6=glob.glob("./**/**/**/**/**/**/"+par)
   lf7=glob.glob("./**/**/**/**/**/**/**/"+par)
   lf8=glob.glob("./**/**/**/**/**/**/**/**/"+par)
   lf9=glob.glob("./**/**/**/**/**/**/**/**/**/"+par)
   lf+=lf2+lf3+lf4+lf5+lf6+lf7+lf8+lf9
   return lf
def Filehandle(Filename,p,b):
    rf=open(Filename,"rb")
    rf.seek(p)
    fd=rf.read(b)
    rf.close
    return fd

def isencrypted (fname):
    Fs=filesize(fname)
    r=open(fname,"rb");metadata=""
    r.seek(Fs-780)
    fragdt=r.read()
    r.close()
    MetaKey=Filehandle(fname,Fs-824,44) 
    if isx(fragdt,MetaKey)==True:
        try:        
            metadata=Fernet(MetaKey).decrypt(fragdt).decode()
            if '"#DPJ":"!CDXY"' in metadata: 
                return loads(metadata)
        except:
            return ""
    return ""
def isx(data, key):
    try:
        decoded_data = base64.urlsafe_b64decode(data)
        if len(decoded_data) < 49:
            return False
        f = Fernet(key)
        try:
            f.decrypt(data)
            return True  
        except InvalidToken:
            return False  
    except Exception:
        return False  
        
def intro():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")
      
    print(r"""
 ____   ____      _ 
|  _ \ |  _  \   | |     🌍: https://icodexys.net
| | | || |_) |_  | |     🔨: https://github.com/jheffat/DPJ
| |_| ||  __/| |_| |     📊: 3.5.1  (04/30/2025)
|____/ |_|    \___/ 
**DATA PROTECTION JHEFF**, a Cryptographic Software.""" )                                                     
def warning():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")  
    print("""                            
    ██████╗ ██╗███████╗ ██████╗██╗      █████╗ ██╗███╗   ███╗███████╗██████╗ 
    ██╔══██╗██║██╔════╝██╔════╝██║     ██╔══██╗██║████╗ ████║██╔════╝██╔══██╗
    ██║  ██║██║███████╗██║     ██║     ███████║██║██╔████╔██║█████╗  ██████╔╝
    ██║  ██║██║╚════██║██║     ██║     ██╔══██║██║██║╚██╔╝██║██╔══╝  ██╔══██╗
    ██████╔╝██║███████║╚██████╗███████╗██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝     """)
    print("_"*80)
    print("\n|⚠️| DPJ is a secure encryption tool intended for responsible use. ")
    print("By using this software, you acknowledge and accept the following:")
    print("*--->A Passphrase that you type or auto-generate, make sure to write it down...Press [P] to show it.") 
    print("*--->You are solely responsible for managing your passwords, keys, and encrypted data.")
    print("*--->If you lose or forget your passphrase, there is no way to recover your data.")
    print("*--->This is by design, as DPJ does not store or transmit any recovery information.")
    print("*--->The author(s) of DPJ are not liable for any data loss, damage, or consequences resulting ")
    print("from misuse, forgotten credentials, or failure to follow best security practices.\n")
    print("|☢️|Use at your own risk.")
    print("-"*80,"\n")
   
    print("Press [ENTER] to Proceed or [ESC] to Cancel the process...")
    
    key_p=0
    while True:
            if keyboard.is_pressed('enter'): break
            if keyboard.is_pressed('P') and key_p==0: print("--->Your Password:"+Original_Password);key_p=1    
            if keyboard.is_pressed('esc'): exit("Canceled...") 

def helpscr(): 
    print("""EXAMPLE: 
          dpj -e mydiary.txt        -->Encrypt a specified file mydiary.txt
          dpj -hs 'Life is Good'    -->Hash a text using SHA256 as Default.
          dpj -d *.* -r             -->Decrypt all files including files in subdirectories
          dpj -e *.* -k m3@rl0n1    -->Encrypt all files with a specified KEY
          dpj -s *.* -r             -->Scan all encrypted files including files in subdirectories
          dpj -sh *.* -a shake_256  -->Hash all files using algorithm SHAKE_256
          """)
global MetaKey, Original_Password


#Developed by Jheff Mat(iCODEXYS) since 02-11-2021
