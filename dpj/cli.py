#  -*- coding: utf-8 -*-
from .utils import *

def main():   
   
    Password="";targets=[];banfilels=[];sucessed=[];notsucessed=[] ;lensuc=0  ;decryptdata=bytearray();encryptdata=bytearray();state=False ;posbyte=0;k=""
    MetaKey=base64.b64encode(KDF(genpass(18,9,7).encode(),urandom(18),32,200000)).strip(b'=')
    PADDING_BYTES=bytes()
    if platform.system()!="Windows":
        if getuid()>0:
            print("--Permission denied--x_x")
            time.sleep(4)
            exit()
#---------------> building the arguments for parameters    
    parser = argparse.ArgumentParser(description="A simple CLI tool to encrypt/decrypt/hash files")
        
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt",metavar="", type=str, help="Encrypt Files/Messages")
    group.add_argument("-d", "--decrypt",metavar="", type=str, help="Decrypt Files/Messages Encrypted")
    group.add_argument("-s", "--scan", metavar="",type=str, help="Scan for encrypted files")
    group.add_argument("-hs", "--hash", metavar="",type=str, help="Hash a File or a String.")

    g2=parser.add_argument_group("Optional Arguments", "These arguments are optional and provide additional features." )
    g2.add_argument("-r", "--recursive", action="store_true", help="Enable recursive, allowing to process subdirectories [OPTIONAL]")
    g2.add_argument("-k", "--key", type=str,metavar="KEY", help="Specify a Passphrase to encrypt/decrypt [OPTIONAL]")
    g2.add_argument("-a", "--algo", type=str,default="sha256", help="Choose an algorithm to hash (blake2b, sha3_512, sha256, sha1,  sha512, shake_128, shake_256, sha3_256, blake2s, md5) or all, Default=sha256")

    try:    
        args = parser.parse_args()
    except SystemExit as e:
        intro()
        parser.print_help()
        helpscr()
        exit()
  #---------------> if  encryption/decryption/scan enabled  then get ready/collect files selected  and skip hashing function       
    for argx, valuex in vars(args).items():
        if argx=='encrypt'or argx=='decrypt'or argx=='scan':
            if valuex!=None:
                print("Collecting...")  
                if args.recursive:
                    targets=recursive(valuex)
                    break
                else:
                    targets=glob.glob(valuex)
                    break
  #-------------->here is where it start to hash files or text if -hs or --hash enabled      
        if argx=="hash" and valuex!=None:   
            if args.algo in ['blake2b', 'sha3_512', 'sha256', 'sha1',  'sha512', 'shake_128', 'shake_256',  'sha3_256', 'blake2s', 'md5']:
                    hashfunction=getattr(hashlib, args.algo.lower())()  
            elif args.algo=='all':
                pass
            else:
                args.algo='sha256'
                hashfunction=getattr(hashlib, args.algo)()
                    
            if path.isfile(valuex):
                targets=valuex  
                print("\n║HASHING A FILE╠"+"═"*60+"╣")    
                try:               
                    data=Filehandle(targets,0,-1) 
                    start_time = time.time() 
                    if args.algo!='all':                        
                        hashfunction.update(data)          
                        if args.algo.startswith("shake_"):
                            length=32
                            digest = hashfunction.hexdigest(length*2)  
                        else:
                            length=hashfunction.digest_size
                            digest = hashfunction.hexdigest() 
                        
                        print(f"📄Filename: {targets}")
                        print(f"\n🔐{args.algo.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                        print(f"🧬[{digest}]\n")
                    elif args.algo=='all': 
                        print(f"📄Filename: {targets}")
                        for ha in sorted(['blake2b', 'sha3_512', 'sha256', 'sha1',  'sha512', 'shake_128', 'shake_256',  'sha3_256', 'blake2s', 'md5']):
                            hashfunction=getattr(hashlib, ha)()      
                            hashfunction.update(data)
                            if ha.startswith("shake_"):
                                length=32
                                digest = hashfunction.hexdigest(length*2)  
                            else:
                                length=hashfunction.digest_size
                                digest = hashfunction.hexdigest() 
                            print(f"\n🔐{ha.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                            print(f"🧬[{digest}]\n")    
                    print("═"*90+"\n")            
                except Exception as e:
                            print(f"🚫 Error - {e}")       
                end_time = time.time() - start_time
                print(f"⌛Times Elapsed: {end_time:.4f} seconds" if start_time else "")
                exit("Done...")          
            elif len(glob.glob(valuex))>1:
                print("Collecting...")
                if args.recursive:
                    targets=recursive(valuex)
                else:
                    targets=glob.glob(valuex)   
                print("\n║HASHING FILES╠"+"═"*60+"╣")
                start_time=time.time() 
                for f in targets: 
                        try:               
                            data=Filehandle(f,0,-1)
                            if args.algo!='all':                            
                                hashfunction.update(data) 
                                if args.algo.startswith("shake_"):
                                    length=32
                                    digest = hashfunction.hexdigest(length*2)  
                                else:
                                    length=hashfunction.digest_size
                                    digest = hashfunction.hexdigest()                          
                                print(f"📄Filename: {f}")
                                print(f"\n🔐{args.algo.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                                print(f"🧬[{digest}]\n")
                                print("═"*90)
                            elif args.algo=='all':                              
                                print(f"📄Filename: {f}")
                                for ha in sorted(['blake2b', 'sha3_512', 'sha256', 'sha1',  'sha512', 'shake_128', 'shake_256',  'sha3_256', 'blake2s', 'md5']):
                                    hashfunction=getattr(hashlib, ha)()      
                                    hashfunction.update(data)
                                    if ha.startswith("shake_"):
                                        length=32
                                        digest = hashfunction.hexdigest(length*2)  
                                    else:
                                        length=hashfunction.digest_size
                                        digest = hashfunction.hexdigest()                                
                                    print(f"\n🔐{ha.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                                    print(f"🧬[{digest}]\n")  
                                print("═"*90)
                        except Exception as e:
                            notsucessed+=[f"🚫 Error - {e}"]
                if notsucessed:
                    for errr in notsucessed:
                        print(errr)
                end_time = time.time() - start_time
                print(f"⌛Times Elapsed: {end_time:.4f} seconds" if start_time else "")
                exit("Done...")                                                      
            else:
                targets=valuex 
                print("\n║HASHING TEXT STRING╠"+"═"*60+"╣")
                start_time=time.time()
                if args.algo!='all':
                    hashfunction.update(targets.encode('utf-8')) 
                    if args.algo.startswith("shake_"):
                        length=32
                        digest = hashfunction.hexdigest(length*2)  
                    else:
                        length=hashfunction.digest_size
                        digest = hashfunction.hexdigest() 
                    print(f"📝Text: {targets}")   
                    print(f"\n🔐{args.algo.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                    print(f"🧬[{digest}]\n")
                elif args.algo=='all':
                        print(f"📝Text: {targets}")
                        for ha in sorted(['blake2b', 'sha3_512', 'sha256', 'sha1',  'sha512', 'shake_128', 'shake_256',  'sha3_256', 'blake2s', 'md5']):
                            hashfunction=getattr(hashlib, ha)()      
                            hashfunction.update(targets.encode('utf-8')) 
                            if ha.startswith("shake_"):
                                length=32
                                digest = hashfunction.hexdigest(length*2)  
                            else:
                                length=hashfunction.digest_size
                                digest = hashfunction.hexdigest() 
                            print(f"\n🔐{ha.upper()} 🧮Length: {length} Bytes, {length*8} Bits")
                            print(f"🧬[{digest}]\n")    
                print("═"*90+"\n")        
                end_time = time.time() - start_time
                print(f"⌛Times Elapsed: {end_time:.4f} seconds" if start_time else "")
                exit("Done...")                 
    #-------------------> here starts  the execution to scan (-s --scan), encrypt(-e --encrypt) or decrypt(-d --decrypt)        
    if len(targets)==0:
        intro()
        parser.print_help()
        helpscr()
        exit("No Result Found...")  
    
    if args.key: Password=args.key    
    if argx=="scan":
        intro()  
        ctf=0
        print("\n║DETAILS OF ENCRYPTED FILES╠"+"═"*60+"╣\n")
        for xc in targets:
            try:
                if len(isencrypted(xc))>0:
                        idinfo=isencrypted(xc)
                        ctf+=1
                        lprint(f"\n\n{ctf})[✔️{path.basename(xc).upper()}]")
                        lprint(f"\n■📄Original Filename:{idinfo["file"].replace("*","")}")                       
                        lprint(f"\n■📐Size:{byteme(idinfo["size"].replace("*",""))}")
                        lprint(f"\n■⚙️Checksum:{idinfo["integrity"].upper()}") 
                        lprint(f"\n■📆Date Encrypted:{idinfo["date"].replace("*","")}")
                        lprint(f"\n■💻OS:{idinfo["os"].replace("*","")}\n")        
                else:
                    continue
            except IOError as errz:
                lprint(f"\n[🚫{errz}]\n")
                
        if ctf>0 :
            exit(f"\n{ctf} Encrypted Files Found...") 
        else: 
            exit(f"\nEncrypted Files not Found...")

    if argx=="encrypt":
        intro() 
        print("\n║TARGET'S LIST╠"+"═"*60+"╣\n")
        ctf=0
        for xc in targets:
            try:
                if len(isencrypted(xc))>0:     
                    banfilels+=[xc];emoj="🔐"
                else:
                    ctf+=1
                    print(f"{ctf}# FILE:[✔️📄 {path.basename(xc)}]")   
            except IOError as errz:
                banfilels+=[xc]
        for xc in banfilels:
            targets.remove(xc)
        if len(targets)==0:exit("***process canceled, no files to encrypt***")
        print("\n|",len(targets),"Files will be encrypted.\n")  
        if ValidPass(Password)==False:
            if len(Password)>0:
                print("""🚩 Passphrase Must have at least:
                    >>>🔠 One Uppercase
                    >>>🔢 One Number
                    >>>🔣 One Special character:#%&!$@
                    >>>⛓  12 or more Characters
                    """)
            else:
                print("Type a Passphrase to encrypt the Target's List")
            print("Type 'a'+ [ENTER] to generate a RANDOM Passphrase")
            print("Type 'q'+ [ENTER] to CANCEL\n")   
            while state!=True:
                Password=input("|🗝️PASSPHRASE:")
                state=ValidPass(Password)      
                if state==False:
                    print("""🚩  Must have at least:
                    >>>🔠 One Uppercase
                    >>>🔢 One Number
                    >>>🔣 One Special character:#%&!$@
                    >>>⛓  12 or more Characters
                    """)
            if Password.lower()=="q":exit("***Process canceled...***")
            if Password.lower()=="a":
                Password=genpass(18,5,4)
                while ValidPass(Password)!=True:
                    Password=genpass(18,5,4)
                print(f"-> Passphrase generated: {Password}")
                print("Please write it down before the encryption start." )
                print("Press [ENTER] to continue...")
                keypress('enter')    
        else:
            print(f"-> Passphrase: {Password}")
            print("Please write it down before the encryption start." )
            print("Press [ENTER] to continue...")
            keypress('enter')    
       
        lentarg=len(targets) 
        disclaimer(Password) 
        lprint("\n| Starting...")
        for scf,Filename in enumerate(targets):  
            try:
                Salt=urandom(16)
                iv=urandom(16)
                iters=rint()
                Pass_KDF=generate_round_keys(KDF(Password.encode() ,Salt,32,iters),0)               
                Pass_Hashed=hashpass(Salt,iters,Pass_KDF[0])
                Fsize=filesize(Filename);bitscv=byteme(str(Fsize))     
                fragbyte=isZipmp3rarother(Filename)
                s_box=generate_sbox(seedfromKDF(Pass_KDF[0]))[0]
                p_box=generate_pbox(16,seedfromKDF(Pass_KDF[0])+999)[0] 
                if fragbyte==0.03:
                    posbyte=Fsize-int((Fsize*fragbyte))
                    fragdata=Filehandle(Filename,posbyte,int(Fsize*fragbyte))
                    ldata=len(fragdata)
                    Type_file="Binary/Compressed"                     
                else:
                    posbyte=0        
                    fragdata=Filehandle(Filename,posbyte,int(Fsize*fragbyte))
                    if is_binary(fragdata)==True:
                        ldata=len(fragdata)
                        Type_file="Binary"            
                    else:     
                        ldata=(Fsize)
                        fragdata=Filehandle(Filename,posbyte,Fsize)
                        Type_file="Plain Text";fragbyte=1          
                
                            
                intro()
                lprint("\n║ENCRYPTION PROCESS╠"+"═"*60+"╣[CTRL+C] Cancel the Process ║")  
                lprint(f"\n| Total Files Encrypted:✔️ {lensuc} |Error Reading: ❌ {len(notsucessed)}\n")
                lprint('\r[%s%s]%s ' % ('█' * int(scf*65/lentarg), '░'*(65-int(scf*65/lentarg)),' % '+f"{((scf/lentarg)*100):.1f}"))
                lprint(f"\n| Target: 📝{path.basename(Filename)}")
                lprint(f"\n| Size: {bitscv}  | Type: [{Type_file}]")  
                lprint("\n■Hashing Data...")  
                F_hashed=hashlib.sha256(Filehandle(Filename,posbyte,int(Fsize*fragbyte))).digest()
                lprint("✅") 
                lprint("\n■Encrypting...")
                if "GB" in bitscv:lprint("It may take a while....")
                encryptdata=dpj_e(fragdata,Pass_KDF,iv,s_box,p_box)  
                if encryptdata[1]>0:
                    encrypted=encryptdata[0][:-encryptdata[1]]
                    padded_bytes=encryptdata[0][len(encrypted):]
                    encryptdata=encrypted
                lprint("✅")   
            
                hmc= hmac.new(Pass_KDF[0], encryptdata, hashlib.sha256).digest()
                lprint("\n■Patching...")
                dpj_dict=('{"#DPJ":"!CDXY","file":"'+Fn_clear(path.basename(Filename)).rjust(45,"*")+
                          '","padding":"'+str(padded_bytes.hex()).rjust(80,"*") +
                          '","posbytes":"'+str(posbyte).rjust(15,"*")+
                          '","tarbytes":"'+str(ldata).rjust(15,"*")+
                          '","date":"'+str(datetime.now().date()).rjust(10,"*")+
                          '","iv":"'+str(iv.hex()).rjust(32,"*")+
                          '","hmac":"'+str(hmc.hex()).rjust(64,"*")+
                          '","pass":"'+str(Pass_Hashed.hex()).rjust(108,"*")+
                          '","integrity":"'+str(F_hashed.hex()).rjust(64,"*")+
                          '","os":"'+platform.system().rjust(12,"*")+
                          '","size":"'+str(Fsize).rjust(15,"*")+'"}').encode()
                         
                Metadatax=Fernet(MetaKey+b'=').encrypt(dpj_dict).strip(b'=')+invertbytes(MetaKey)       
                FTarget=open(Filename,"rb+")
                FTarget.seek(posbyte)
                FTarget.write(encryptdata)
                FTarget.seek(Fsize) 
                FTarget.write(Metadatax)
                FTarget.close
                fragdata="";encryptdata=bytearray()
                sucessed+=[{"Filename":path.basename(Filename), "integrity":F_hashed}]
                lensuc=len(sucessed)
                lprint("✅")
            except IOError as errz:
                lprint("⛔")
                notsucessed+=[{"Filename":path.basename(Filename), "error":str(errz)}]
                FTarget="";fragdata="";encryptdata=bytearray()
            except KeyboardInterrupt as kk:
                    print("\n|ENCRYPTION PROCESS CANCELED...🙄\n")
                    print("|Result List:\n")
                    if lensuc>0:
                            print("***Encrypted\n")
                            for ln in range(0,lensuc,3):
                                if ln+2<lensuc:
                                    print(f"{ln+1})--🔐File:{sucessed[ln]['Filename']}     {ln+2})--🔐File:{sucessed[ln+1]['Filename']}     {ln+3})--🔐File:{sucessed[ln+2]['Filename']}")                    
                                else:
                                    print(f"{ln+1})--🔐File:{sucessed[ln]['Filename']}" )
                            print(f"✔️{lensuc} Files Encrypted ")
                            print(f"🚫{lentarg-lensuc} Files Not Encrypted ")                      
                    if len(notsucessed)>0:
                            print("\n***Failed\n")
                            for r in notsucessed:
                                print(f"--File: {r['Filename']}  --Reason:{r['error']}")  
                            print(f"❌ {len(notsucessed)}Files Failed to Encrypt...\n")               
                    exit("Terminated...")
                    
        intro()    
        if lensuc>0 and len(notsucessed)==0:titledone="|DONE ENCRYPTING...😃" 
        if lensuc>0 and len(notsucessed)>0:titledone="|DONE ENCRYPTING BUT...😱" 
        if lensuc==0 and len(notsucessed)>0:titledone="|ENCRYPTION PROCESS FAILED...❌"       
        print(f"\n{titledone}\n")  
        print("|Result:\n")    
        if lensuc>0:
                    print("***Encrypted List\n")
                    for ln in range(0,lensuc,3):
                        if ln+2<lensuc:
                            print(f"{ln+1})--🔐File:{sucessed[ln]['Filename']}     {ln+2})--🔐File:{sucessed[ln+1]['Filename']}     {ln+3})--🔐File:{sucessed[ln+2]['Filename']}")                    
                        else:
                            print(f"{ln+1})--🔐File:{sucessed[ln]['Filename']}" )            
                    
        if len(notsucessed)>0:
                    print("\n***Failed List\n")
                    for r in notsucessed:
                        print(f"--File: {r['Filename']}  --Reason:{r['error']}")          

        print(f"\n❌ {len(notsucessed)} Failed to Encrypt\n" if notsucessed else "")
        print(f"✔️ {len(sucessed)} Files Encrypted."  if sucessed else "")    
        
        exit("Done!")
        
    if argx=="decrypt":
        intro()  
        print("\n║TARGET'S LIST╠"+"═"*60+"╣\n") 
        ctf=0  
        for xc in targets:
            try:   
                if len(isencrypted(xc))>0:
                    ctf+=1
                    print(f"{ctf}# FILE:[🔐📄{path.basename(xc)}]")
                else: 
                    banfilels+=[xc]                   
            except IOError as errz:
                banfilels+=[xc]
        for xc in banfilels:
            targets.remove(xc) 
        if len(targets)==0:exit("***process canceled, no files to decrypt***") 
        print("\n|",len(targets),"Files will be decrypted.\n")
        if ValidPass(Password)==False:        
            if len(Password)>0:
                print("""🚩 Passphrase Must have at least:
                >>>🔠 One Uppercase
                >>>🔢 One Number
                >>>🔣 One Special character:#%&!$
                >>>⛓  12 or more Characters
                    """) 
            else:
                print("Type a passphrase to decrypt the Target's List")
            
            print("Type 'q'+[ENTER] to CANCEL\n")
            while state!=True:
                Password=input("|🗝️PASSPHRASE:")
                state=ValidPass(Password)      
                if state==False:
                    print("""🚩 Passphrase Must have at least:
                >>>🔠 One Uppercase
                >>>🔢 One Number
                >>>🔣 One Special character:#%&!$
                >>>⛓  8 Characters
                    """)  
            if Password.lower()=="q" or Password.lower()=="a":exit("***process canceled...***")      
        else:
            print(f"-> Passphrase: {Password}")
            print("Press [ENTER] to start the decryption...")
            keypress('enter')  
            
        lentarg=len(targets)     
        for scf,Filename in enumerate(targets):
            lprint(f"\n■Reading Next File #{scf}: {path.basename(Filename.upper())}...")
            AFsize=filesize(Filename)
            headinfo=isencrypted(Filename) 
            passhashed=hashparser(bytes.fromhex(headinfo["pass"]))
            iv=bytes.fromhex(headinfo['iv'])
            hmc=bytes.fromhex(headinfo['hmac'])
            F_hashed=bytes.fromhex(headinfo["integrity"])
            padded_bytes=bytes.fromhex(headinfo["padding"].replace("*",""))
            iters=passhashed[0]
            Salted=passhashed[1]
            hkey=passhashed[2] 
            Pass_KDF=generate_round_keys(KDF(Password.encode() ,Salted,32,iters),0)           
            bitscv=byteme(str(AFsize)) 
            Fsize=int(headinfo["size"].replace("*",""))
            BytesTarget=int(headinfo["tarbytes"].replace("*","")) 
            BytesPosition=int(headinfo["posbytes"].replace("*",""))      
            fragdata=Filehandle(Filename,BytesPosition,BytesTarget)           
            ispass=Pass_KDF[0]==hkey
            ishmac=hmac.new(Pass_KDF[0],fragdata,hashlib.sha256).digest()==hmc
            
            if ispass:
                if ishmac:
                    lprint("✅")
                    try:      
                        invs_box=generate_sbox(seedfromKDF(Pass_KDF[0]))[1]
                        invp_box=generate_pbox(16,seedfromKDF(Pass_KDF[0])+999)[1]                               
                        intro()    
                        lprint("\n║DECRYPTION PROCESS╠"+"═"*60+"╣[CTRL+C] Cancel the Process ║")  
                        lprint(f"\n| Total Files Decrypted: ✔️ {lensuc} |Error Reading: ❌ {len(notsucessed)}\n")      
                        lprint('\r[%s%s]%s ' % ('█' * int(scf*65/lentarg), '░'*(65-int(scf*65/lentarg)),f" Scanned {scf}/{lentarg}"))
                        lprint(f"\n| Target: 📝{path.basename(Filename)}")
                        lprint(f"\n| Size: {bitscv}") 
                        lprint("\n■Decrypting...")  
                        if "GB" in bitscv or "TB" in bitscv:lprint("It may take a while...")                 
                        decryptdata=dpj_d(fragdata,Pass_KDF,iv,invs_box,invp_box,padded_bytes)
                        lprint("✅" )  
                        lprint("\n■Checking Data's Integrity...")
                        integrity=hashlib.sha256(decryptdata).digest()== F_hashed
                        if integrity==True:
                            lprint("✅")
                        else:
                            lprint("⛔")
                            print("\n☢️|CheckSum didn't match...")
                            print("[I]gnore the warning, try to decrypt the file and keep an original copy.")
                            print("[S]kip this file, do not decrypt it and continue to the next....")
                            while k!='I' and k!= 'S':
                                k=keyboard.read_key().upper()
                            if k=="S":
                                notsucessed+=[{"Filename": path.basename(Filename),"error" : "CheckSUM Didn't match"}]
                                FTarget="";decryptdata=bytearray();fragdata=b""
                                continue
                            elif k=="I":
                                print("Copying....Please wait")
                                copy2(Filename,Filename+"_!DPJ_Copy")
                        lprint("\n■Patching...")
                        FTarget=open(Filename,"rb+")
                        FTarget.seek(BytesPosition)
                        FTarget.write(decryptdata)
                        FTarget.seek(0)
                        FTarget.truncate(Fsize)
                        FTarget.close             
                        fragdata=b"";decryptdata=bytearray()
                        sucessed+=[{"Filename": path.basename(Filename),"integrity" : str(integrity)}]
                        lensuc=len(sucessed)
                        lprint("✅")
                    except IOError as errz:
                        lprint("⛔")
                        notsucessed+=[{"Filename": path.basename(Filename),"error" : str(errz)}]
                        FTarget="";decryptdata=bytearray();fragdata=b""
                    except KeyboardInterrupt as kk:
                        print("\n|DECRYPTION PROCESS CANCELED...🙄\n")            
                        print("|Result:\n")     
                        if lensuc>0:
                            print("***Decrypted List\n")
                            for ln in range(0,lensuc,3):            
                                if ln+2<lensuc:
                                    if sucessed[ln]["integrity"]=='True': ic="✅"
                                    elif sucessed[ln]["integrity"]=='False':ic="⛔"
                                    if sucessed[ln+1]["integrity"]=='True': ic1="✅"
                                    elif sucessed[ln+1]["integrity"]=='False':ic1="⛔"
                                    if sucessed[ln+2]["integrity"]=='True': ic2="✅"
                                    elif sucessed[ln+2]["integrity"]=='False':ic2="⛔"
                                    print(f"{ln})--{ic}File:{sucessed[ln]['Filename']}     {ln+1})--{ic1}File:{sucessed[ln+1]['Filename']}     {ln+2})--{ic2}File:{sucessed[ln+2]['Filename']}")                    
                                else:
                                    if sucessed[ln]["integrity"]=='True': ic="✅"
                                    elif sucessed[ln]["integrity"]=='False':ic="⛔"
                                    print(f"{ln})--{ic}File:{sucessed[ln]['Filename']}" )
                                
                            print(f"✔️ {len(sucessed)} Files Decrypted\n")
                            print("🚫",lentarg-len(sucessed),"Files Not Decrypted ")     
                        if len(notsucessed)>0:
                                print("\n***Failed List\n")
                                for r in notsucessed:
                                    print(f"--File: {r['Filename']}  --Reason:{r['error']}")                                      
                                print(f"❌ {len(notsucessed)} Files Failed to decrypt...\n")
                        
                        exit("Done!") 
                else:
                    lprint("⛔")
                    notsucessed+=[{"Filename":path.basename( Filename),"error" : "The encrypted data you're trying to decrypt has been changed or corrupted!"}]
                    intro()    
                    lprint("\n║DECRYPTION PROCESS╠"+"═"*60+"╣[CTRL+C] Cancel the Process ║")  
                    lprint(f"\n| Total Files Decrypted: ✔️ {lensuc} |Error Reading: ❌ {len(notsucessed)}\n")      
                    lprint('\r[%s%s]%s ' % ('█' * int(scf*65/lentarg), '░'*(65-int(scf*65/lentarg)),f" Scanned {scf}/{lentarg}"))
                    lprint(f"\n| Target: 📝{path.basename(Filename)}")
                    lprint(f"\n| Size: {bitscv}")
            else:
                lprint("⛔")
                notsucessed+=[{"Filename":path.basename( Filename),"error" : "Invalid passphrase!"}]
                intro()    
                lprint("\n║DECRYPTION PROCESS╠"+"═"*60+"╣[CTRL+C] Cancel the Process ║")  
                lprint(f"\n| Total Files Decrypted: ✔️ {lensuc} |Error Reading: ❌ {len(notsucessed)}\n")      
                lprint('\r[%s%s]%s ' % ('█' * int(scf*65/lentarg), '░'*(65-int(scf*65/lentarg)),f" Scanned {scf}/{lentarg}"))
                lprint(f"\n| Target: 📝{path.basename(Filename)}")
                lprint(f"\n| Size: {bitscv}")        
           
        intro()
        if len(sucessed)>0 and len(notsucessed)==0:titledone="|DONE DECRYPTING...😃" 
        if len(sucessed)>0 and len(notsucessed)>0:titledone="|DONE DECRYPTING BUT...😱" 
        if len(sucessed)==0 and len(notsucessed)>0:titledone="|DECRYPTION PROCESS FAILED...❌"   
        print(f"\n{titledone}\n")      
        print("|Result List:\n")
        if lensuc>0:
                    print("***Decrypted list\n")
                    for ln in range(0,lensuc,3):            
                        if ln+2<lensuc:
                            if sucessed[ln]["integrity"]=='True': ic="✅"
                            elif sucessed[ln]["integrity"]=='False':ic="⛔"
                            if sucessed[ln+1]["integrity"]=='True': ic1="✅"
                            elif sucessed[ln+1]["integrity"]=='False':ic1="⛔"
                            if sucessed[ln+2]["integrity"]=='True': ic2="✅"
                            elif sucessed[ln+2]["integrity"]=='False':ic2="⛔"
                            print(f"{ln})--{ic}File:{sucessed[ln]['Filename']}     {ln+1})--{ic1}File:{sucessed[ln+1]['Filename']}     {ln+2})--{ic2}File:{sucessed[ln+2]['Filename']}")                    
                        else:
                            if sucessed[ln]["integrity"]=='True': ic="✅"
                            elif sucessed[ln]["integrity"]=='False':ic="⛔"
                            print(f"{ln})--{ic}File:{sucessed[ln]['Filename']}" )
                                
        if len(notsucessed)>0:
                    print("\n***Failed List\n")
                    for r in notsucessed:
                        print(f"--File: {r['Filename']}  --Reason:{r['error']}")  
                    
        print(f"\n❌ {len(notsucessed)} Files Failed to decrypt...\n" if notsucessed else "")
        print(f"✔️ {len(sucessed)} Files Decrypted"  if sucessed else "")    
        
        exit("Done!")


     

if __name__ == "__main__":
    
    main()    

#Developed by Jheff Mat(iCODEXYS) 12/22/2022