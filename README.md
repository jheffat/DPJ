# 🔐 DPJ - CLI Data Encryption Tool(FiXOR)

![Alt text](https://github.com/jheffat/-DPJ/blob/main/scrnsht/intro.png)
**DPJ** is a command-line data encryption tool, a complete rebuild and upgrade from the legacy **Fixor** project (v2.11 / v1.0). Name changed to DPJ 
 in honor of the original encryption tools developed in QBasic and Visual Basic (2003–2005), DPJ is faster, more secure, and packed with new features designed to keep your data safe. Good tool to encrypt your work projects or your sensitive data(documents, PDFs, photos, videos, etc.).

## ⚡ Features

- 🔒 **Encrypt & Decrypt Files** using strong cryptography
- 🧠 **Choose or Autogenerate Passphrase** for encryption
- 🔐 **KDF-powered Key Derivation** to resist brute-force attacks
- 🧂 **Secure Password Hashing with bcrypt** (stored in encrypted metadata)
- 🧬 **Encrypted Metadata** using AES to protect internal config
- 🔍 **File Scan Mode** to check encryption status
- ✅ **File Integrity Verification** via cryptographic hash
- 🛡️ **Tamper Protection**: Files won’t be modified unless the passphrase is correct
- #️⃣ **Hash tools included**: Hash files/Msg using any theses functions(sha2,sha3,md5, blake3, whirlpool)
## 🚀 Performance

DPJ improves on Fixor with significantly faster encryption and decryption processes, optimized for modern systems and large files.

## 🔧 Installation

You can install DPJ 
  ++by cloning this repo:

```bash
git clone https://github.com/yourusername/dpj.git
cd dpj
python3 -m pip install
``` 
  ++install DPJ by pypi:
```bash
pip install dpj
```
  ++Download and install executable :
```bash
Developing....
```


## 🧪 Usage Examples
Encrypt all files including sub-directories with a key `#R3ds0ftwar3!len3zz`
```bash
dpj -e *.* -r -k #R3ds0ftwar3!len3zz    
```
Encrypt all files with the extension  `.JPG` on the current path `c:\pictures`
```bash
dpj -e  c:\pictures\*.jpg     
```
Decrypt all files including in sub-directories on the current local
```bash
dpj -d *.* -r  
```
scan all files including in sub-directories on the current local 
```bash
dpj -s *.* -r  
```
## 📷 Screenshots
`List of Files ready to be encrypted`
![Alt text](https://github.com/jheffat/-DPJ/blob/main/scrnsht/List%20to%20encrypt.png)
`Encryption Process`
![](https://github.com/jheffat/-DPJ/blob/main/scrnsht/Encrypting.png)
`Decryption Process`
![Alt text](https://github.com/jheffat/-DPJ/blob/main/scrnsht/Decrypting.png)
`Scanning files encrypted`
![Alt text](https://github.com/jheffat/-DPJ/blob/main/scrnsht/Scaning%20%20encrypted%20file.png)



## 🔐 Security Details

- KDF: Passphrases are transformed via a Key Derivation Function before use, making brute-force attempts extremely difficult.
- bcrypt: Passphrase hashes are stored using bcrypt to safely verify future attempts without revealing the key.
- AES Encryption: The metadata (containing the bcrypt hash) are encrypted with AES, the file content use different cryptographic method.
- No Overwrites: Files will not be altered if the provided passphrase is incorrect.
- Hash Verification: A post-decryption hash ensures that the data was correctly restored.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙌 Acknowledgements
DPJ(Data protection Jeff), was my first encryption app crafted in QBasic(CLI) and Visual Basic(GUI) between 2003–2007. This project is a modern revival with more power, speed, and security, thanks to the powerful language PYTHON. 
