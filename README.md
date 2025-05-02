![License](https://img.shields.io/github/license/jheffat/DPJ)
![Repo Size](https://img.shields.io/github/repo-size/jheffat/DPJ)
![Build](https://img.shields.io/pypi/v/dpj)

```text
 ____   ____      _ 
|  _ \ |  _  \   | |     🌍: https://icodexys.net
| | | || |_) |_  | |     🛠️: https://github.com/jheffat/DPJ
| |_| ||  __/| |_| |     📊: 3.5.0  (04/30/2025)
|____/ |_|    \___/ 
**DATA PROTECTION JHEFF**, a Cryptographic Software.

```

# 🔐 DPJ - CLI Data Cryptographic Tool

**DPJ** is a command-line data encryption tool, an improvement of [Fixor](https://github.com/jheffat/-FiXOR) 2.50(Discontinued). The Name Fixor changed to DPJ 
 in honor of the my first encryption tool developed in QBasic and Visual Basic (2003–2007), DPJ is faster, more secure, and packed with new features designed to keep your data safe. Is a lightweight CLI tool, encrypt/decrypt files securely using custom method, built with python. Good tool to encrypt your work projects or your sensitive data(documents, PDFs, photos, videos, etc.). -->✨ [Changelog](https://github.com/jheffat/DPJ/blob/main/CHANGELOG.md)

## 🧾 Features

- 🔒 **Encrypt & Decrypt Files**, using strong cryptography
- ⚡ **IV Support**,  Uses a cryptographically secure IV to ensure ciphertext uniqueness, even with the same key and plaintext.
- 🧠 **Choose or Autogenerate Passphrase**, for encryption
- 🚫 **No Overwrites**, a file will not be altered if the provided passphrase is incorrect. DPJ detects if a file is encrypted and prevents redundant encryption
- 🔐 **KDF Support**, Passphrases are transformed via a `Key Derivation Function` before use, making brute-force attempts extremely difficult.
- 🧂 **Secure Password Hashing with bcrypt**, stored in encrypted metadata
- 🧬 **Encrypted Metadata with AES**, Used to protect internal config
- 🔍 **File Scan Mode**, to check encryption details
- ✅ **Integrity Check Passed**, A SHA-256-based verification step checks whether the decrypted data matches the original, ensuring the decryption process was successful.
- 🛡️ **HMAC Support**, A SHA-256-based HMAC is generated during encryption and verified during decryption to detect tampering or corruption.
- #️⃣ **Hash tools included**, Hash files/Msg using any theses algorithms (blake2b, sha3_512, sha256, sha1,  sha512, shake_128, shake_256, sha3_256, blake2s, md5), In the absence of a specified algorithm, the default SHA256 will be applied.

## 🚀 Performance

DPJ improves on Fixor with significantly faster encryption and decryption processes, optimized for modern systems and large files.

## ⚠️ Disclaimer
**DPJ is a secure encryption tool intended for responsible use.**
By using this software, you acknowledge and accept the following:

-You are solely responsible for managing your passwords, keys, and encrypted data.

-If you lose or forget your passphrase, there is no way to recover your data.
This is by design, as DPJ does not store or transmit any recovery information.

-The author(s) of DPJ are not liable for any data loss, damage, or consequences resulting from misuse, forgotten credentials, or failure to follow best security practices.

**Use at your own risk.**

## 🔧 Installation

You can install DPJ, 
  
  ++by cloning this repo:

```bash
git clone https://github.com/jheffat/dpj.git
cd dpj
python3 -m pip install
``` 
  ++by using pypi [pypi.org/dpj...](https://pypi.org/project/dpj/) or:
```bash
pip install dpj
```
  ++By download and install executable for:

`*Windows`
[DPJ 3.0.7 Installer.exe](https://raw.githubusercontent.com/jheffat/DPJ/main/Bins/DPJ%203.0.7%20Installer.exe)  (Need to setup your anti-virus to allow using this app)

`*Linux Debian`
[DPJ_307LinuxDeb.deb](https://raw.githubusercontent.com/jheffat/DPJ/main/Bins/DPJ%203.0.7%20Installer.deb) (Link Dead**Fixing...)

   ```bash
   sudo dpkg -i DPJ_307LinuxDeb.deb
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
Hash all files using all algorithms
```bash
dpj -hs *.* -a all
```
Hash a text using md5
```bash
dpj -hs 'Life is Good' -a md5
```

## 📷 Screenshots
`List of Files ready to be encrypted`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/List%20to%20encrypt.png)
`Encryption Process`
![](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/Encrypting.png)
`Decryption Process`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/Decrypting.png)
`Scanning files encrypted`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/Scaning%20%20encrypted%20file.png)
`Hashing a file`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/hashing%20a%20file.png)
`Hashing a file with all algorithms`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/hashing%20a%20file%20with%20all.png)
`Hashing all files using only the algorithm SHA256`
![Alt text](https://raw.githubusercontent.com/jheffat/-DPJ/main/scrnsht/hashing%20all%20files.png)


## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.


## 🙌 Acknowledgements
DPJ(Data protection Jeff), was my first encryption app crafted in QBasic(CLI) and Visual Basic(GUI) between 2003–2007. This project is a modern revival with more power, speed, and security, thanks to the powerful language PYTHON. 
