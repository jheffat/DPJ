import argparse,glob
from os import system,path 
 
parser = argparse.ArgumentParser(description="A simple CLI tool using argparse.", epilog= "USAGE: dpj -e *.* -k m3@rl0n1 -->Encrypt all files with a specified KEY")
    
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encrypt",metavar="", type=str, help="Encrypt Files/Messages")
group.add_argument("-d", "--decrypt",metavar="", type=str, help="Decrypt Files/Messages Encrypted")
group.add_argument("-s", "--scan", metavar="",type=str, help="Scan for encrypted files")

g2=parser.add_argument_group("Optional Arguments", "These arguments are optional and provide additional features." )
g2.add_argument("-r", "--recursive", action="store_true", help="Enable recursive, allowing to process subdirectories [OPTIONAL]")
g2.add_argument("-k", "--key", type=str,metavar="KEY", help="Specify a Passphrase to encrypt/decrypt [OPTIONAL]")
scf=3
lentarg=200

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

items = list(my_dict.items())
sucessed=[]
# Loop in steps of 2
a=glob.glob("C:/New folder/*.*")


for y,x in enumerate(a):
    sucessed+=[{"Filename":path.basename(x), "integrity":y}]
lensuc=len(sucessed)
for ln in range(0,lensuc,3):
                    if ln+2<lensuc:
                        print(f"{ln})--🔐File:{sucessed[ln]['Filename']}     {ln+1})--🔐File:{sucessed[ln+1]['Filename']}     {ln+2})--🔐File:{sucessed[ln+2]['Filename']}")                    
                    else:
                        print(f"{ln})--🔐File:{sucessed[ln]['Filename']}" )
                