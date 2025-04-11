# 🔐 DPJ - CLI File Encryption Tool

**DPJ** is a command-line file encryption tool, a complete rebuild and upgrade from the legacy **Fixor** project (v2.11 / v1.0). Name changed to DPJ 
 in honor of the original encryption tools developed in QBasic and Visual Basic (2003–2005), DPJ is faster, more secure, and packed with new features designed to keep your files safe.

## ⚡ Features

- 🔒 **Encrypt & Decrypt Files** using strong cryptography
- 🧠 **Choose or Autogenerate Passphrase** for encryption
- 🔐 **KDF-powered Key Derivation** to resist brute-force attacks
- 🧂 **Secure Password Hashing with bcrypt** (stored in encrypted metadata)
- 🧬 **Encrypted Metadata** using AES to protect internal config
- 🔍 **File Scan Mode** to check encryption status
- ✅ **File Integrity Verification** via cryptographic hash
- 🛡️ **Tamper Protection**: Files won’t be modified unless the passphrase is correct

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


##🧪 Usage Examples
```bash
dpj -e *.* -r -k #R3ds0ftwar3!len3zz    
```
Will encrypt all files including sub-directories with a key `#R3ds0ftwar3!len3zz`

