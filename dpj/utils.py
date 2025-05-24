#  -*- coding: utf-8 -*-
from cryptography.fernet import Fernet,InvalidToken
from shutil import copy2
from random import shuffle,randint,seed
from string import ascii_letters,digits
import numpy as np
from os import system,path,urandom #,getuid #<---Only for Linux/MacOSX
import glob, platform,re,keyboard,argparse,hashlib,time,hmac,base64
from json import loads
from secrets import choice
from sys import exit,stdout
from datetime import datetime
def padding(data: np.ndarray, block_size: int = 16) -> np.ndarray:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    padding = np.full((pad_len,), pad_len, dtype=np.uint8)
    return np.concatenate((data, padding)),padding
def generate_round_keys(master_key, rounds):
    round_keys = [master_key]
    for i in range(rounds):
        prev = round_keys[-1]
        next_key = bytes((b ^ ((i * 17 + j * 31) % 256)) for j, b in enumerate(prev))
        round_keys.append(next_key)
    return round_keys
def swap_16bytes(data):
    data = data.reshape(-1, 16)  
    swapped = data[:, ::-1]
    return swapped.flatten()
def invertbytes(c):
   return c[::-1]
def insertbytes(d,i,b):
    return d[:i] + b + d[i:]
def getbytes(d,i,l):
    return d[i:i+l]
def subtract_key(data, key):
    key_expanded = np.resize(key, data.shape)
    result = (data - key_expanded) % 256
    return result.astype(np.uint8)
def add_key(data, key):
    key_expanded = np.resize(key, data.shape)
    result = (data + key_expanded) % 256
    return result.astype(np.uint8)
def xor_key(data, key):
    key_expanded = np.resize(key, data.shape)
    result = np.bitwise_xor(data, key_expanded)
    return result

def nonlinear(block,key,sbox,pbox):
    block = sbox[block]
    block = block[pbox]
    block= np.bitwise_xor(block, key[:16])
    block=swap_16bytes(block)
    return block

def nonlinear_inv(block,key,sbox,pbox):
    block=swap_16bytes(block)
    block= np.bitwise_xor(block, key[:16])
    block = block[pbox]
    block = sbox[block]  
    return block

def generate_sbox(seedx=42):
    rng = np.random.default_rng(seedx)
    sbox = np.arange(256, dtype=np.uint8)
    rng.shuffle(sbox)
    inv_sbox = np.empty_like(sbox)
    inv_sbox[sbox] = np.arange(256, dtype=np.uint8)
    return sbox,inv_sbox

def generate_pbox(block_size=16, seedx=1337):
    rng = np.random.default_rng(seedx)
    pbox = np.arange(block_size, dtype=np.uint8)
    rng.shuffle(pbox)
    inv_pbox = np.empty_like(pbox)
    inv_pbox[pbox] = np.arange(len(pbox), dtype=np.uint8)
    return pbox, inv_pbox

def seedfromKDF(key: bytes) -> int:
    return int.from_bytes(key, 'big') % (2**32)

def dpj_e(data,mkeys,iv,sbox,pbox):
    iv_arr = np.frombuffer(iv, dtype=np.uint8)
    data = np.frombuffer(data, dtype=np.uint8)
    pad=padding(data,16)
    data=pad[0]
    for k in mkeys:    
        k = np.frombuffer(k, dtype=np.uint8)  
        blocks = data.reshape(-1, 16)
        data = np.array([nonlinear(block, k,sbox,pbox) for block in blocks]) 
        data=xor_key(data,iv_arr)    
        data=subtract_key(data,k)
        data=xor_key(data,k)
        data=add_key(data,k)    
    return data.tobytes(),len(pad[1])

def dpj_d(data,mkeys,iv,sbox,pbox,padded):
    if padded:data=data+padded
    iv_arr = np.frombuffer(iv, dtype=np.uint8)
    data = np.frombuffer(data, dtype=np.uint8)
    for k in reversed(mkeys):
        k = np.frombuffer(k, dtype=np.uint8)       
        data=subtract_key(data,k)
        data=xor_key(data,k)
        data=add_key(data,k)       
        data=xor_key(data,iv_arr)          
        blocks = data.reshape(-1, 16)
        data = np.array([nonlinear_inv(block, k,sbox,pbox) for block in blocks])
    return data.tobytes()[:-len(padded)]

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
def rint():
    return randint(100000,170000)

def hashpass(salt,iter,key):
    result=[]
    for i in range(len(key)):
        if i<len(salt): result+=[salt[i]]
        if i<len(key): result+=[key[i]]
    return bytes(result+list(map(ord,str(iter))))

def hashparser(h):
    salt=[];p=[]    
    salt+=[h[i]  for i in range(0,32,2)]  
    p+=[h[i] for i in range(1,32,2)]
    hashed=bytes(p)+h[32:48]
    iters=int(h[48:])
    return (iters,bytes(salt),hashed)

def KDF(Pass,Salt,bk,r) ->bytes:
    return  hashlib.pbkdf2_hmac('sha3_512', Pass, Salt,r, dklen=bk)

def filesize(fname):
    f=open(fname,"rb");f.seek(0,2 );s=f.tell();f.close
    return s
def byteme(b):
    if b == 0:return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    while b >= 1024 and i < len(units) - 1:
        b /= 1024.0
        i += 1   
    return f"{b:.2f} {units[i]}"

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
    fragdata=Filehandle(fname,Fs-930,-1)
    MetaKey=invertbytes(getbytes(fragdata,887,43))+b'='
    metadata=fragdata[:887]+b'='
    if isx(metadata,MetaKey)==True:
        try:        
            metadata=Fernet(MetaKey).decrypt(metadata).decode()
            
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
| |_| ||  __/| |_| |     📊: 3.5.3  (05/04/2025)
|____/ |_|    \___/ 
**DATA PROTECTION JHEFF**, a Cryptographic Software.""" )                                                     
def disclaimer(p):
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
            if keyboard.is_pressed('P') and key_p==0: print("--->Your Password:"+p);key_p=1    
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
global MetaKey


#Developed by Jheff Mat(iCODEXYS) since 02-11-2021