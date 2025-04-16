#  -*- coding: utf-8 -*-
from shutil import copy2
from string import ascii_letters,digits
from os import system,path #,getuid #<---Only for Linux/MacOSX
    
from cryptography.fernet import Fernet,InvalidToken
import glob, platform,re,keyboard, bcrypt,base64,argparse,hashlib
from json import loads
from secrets import choice
from sys import exit, argv,stdout
from time import sleep
from datetime import datetime
def KDF(Pass,Salt,bk,r):
    return  bcrypt.kdf(Pass,salt=Salt,desired_key_bytes=bk,rounds=r)

def dpj(data,key):
    klen=len(key)  
    dx=bytearray();dy=bytearray();dz=bytearray() 
    dx+=bytes([n-key[c%klen] & 255 for c,n in enumerate(data)])      
    dy+=bytes([(n^key[c%klen]) for c,n in enumerate(dx)])          
    dz+=bytes([n+key[c%klen] & 255 for c,n in enumerate(dy)])
    return dz

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

def genpass():
    chars="koijQh4uW3!y1@gEM2#ftNR$rdBT6se^5VYw&7Ca*8U9q.0X,lI?ZpAm+SODc-FbGPHv/JxKLz";PasswordGen=""
    PasswordGen+="".join(choice(chars) for _ in range(18))
    return PasswordGen

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
def isencrypted (fname):
    key=KeyGeneratedBase64
    Fs=filesize(fname)
    r=open(fname,"rb");metadata=""
    r.seek(Fs-612)
    fragdt=r.read()

    if isx(fragdt,key)==True:
        try:
            
            metadata=Fernet(key).decrypt(fragdt).decode()
            if '"#DPJ":"!CDXY"' in metadata: 
                return loads(metadata)
        except:
            return ""
    return ""
        
def intro():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")
    print("""  
    ____   ____      _ 
   |  _ \ |  _ \    | |     🌍: https://icodexys.net
   | | | || |_) |_  | |     🔨: https://github.com/jheffat/-DPJ
   | |_| ||  __/| |_| |     📊: 3.0.6  (04/22/2025)
   |____/ |_|    \___/ 
**DATA PROTECTION JHEFF**, a Cryptographic Software.\n""" )                                                     
def warning():
    if platform.system()=='Linux':
        _ = system('clear')
    elif platform.system()=='Windows':
        _ = system("cls")
    else:
        _ = system("clear")  
    print("""##      ##    ###    ########  ##    ## #### ##    ##  ######   
##  ##  ##   ## ##   ##     ## ###   ##  ##  ###   ## ##    ##  
##  ##  ##  ##   ##  ##     ## ####  ##  ##  ####  ## ##        
##  ##  ## ##     ## ########  ## ## ##  ##  ## ## ## ##   #### 
##  ##  ## ######### ##   ##   ##  ####  ##  ##  #### ##    ##  
##  ##  ## ##     ## ##    ##  ##   ###  ##  ##   ### ##    ##  
 ###  ###  ##     ## ##     ## ##    ## #### ##    ##  ######   """)
    print("_"*80,"|")
    print("\n|☢️| Please follow the rules & consequences of this action:")
    print("*--->Forgetting your password means that you will lose your encrypted data....forever ;( ")
    print("*--->A Password that you type or auto-generate, make sure to write it down...Press [P] to show it.") 
    print("*--->Any action encrypt/decrypt a file, will generate a file log 'encryption.log' / 'decryption.log'....")
    print("*--->DPJ is capable to detect if a file is encrypted or not...")
    print("*--->Also is capable to check if the password is correct or not, before touching the file.")
    print("*--->By Pressing [ENTER] you are aware of your own responsibility of your data!")
    print("-"*80,"|\n")
    print
    print("Press [ENTER] to Proceed or [ESC] to Cancel the process...")
    key_p=0
    while True:
            if keyboard.is_pressed('enter'): break
            if keyboard.is_pressed('P') and key_p==0: print("--->Your Password:"+Original_Password);key_p=1    
            if keyboard.is_pressed('esc'): exit("Canceled...") 

def helpscr(): 
    print("""EXAMPLE: 
          dpj -e mydiary.txt        -->Encrypt a specified file mydiary.txt
          dpj -e *.exe              -->Encrypt all files with the extension .EXE on a specified location
          dpj -d *.* -r             -->Decrypt all files including files in subdirectories
          dpj -e *.* -k m3@rl0n1    -->Encrypt all files with a specified KEY
          dpj -s *.* -r             -->Scan all encrypted files including files in subdirectories
          dpj -sh *.* -a shake_256  -->Hash all files using algorithm SHAKE_256
          """)
global KeyGeneratedBase64
KeyGeneratedBase64=base64.b64encode(KDF(b"#IC)D#X!Sd@t@pJ3ff",b"s87r444r4e4w4#s@^43",32,100)).decode()
#Developed by Jheff Mat(iCODEXYS) since 02-11-2021
