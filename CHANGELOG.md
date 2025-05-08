# Changelog

All notable changes to this project will be documented in this file.


---

## [3.5.2] - 2025-08-05
### Changed
- Strong Password Hashing storage + random (salt/iteration count) per file.
- Encryption/Decryption more Faster.
---

## [3.5.0] - 2025-30-04
### Added
- Hash tools included, Hash files/Msg using any theses algorithms (blake2b, sha3_512, sha256, sha1, sha512, shake_128, shake_256, sha3_256, blake2s, md5)
- SHA-256-based HMAC.
- KDF Support, Passphrases are transformed via a Key Derivation Function before use, making brute-force attempts extremely difficult.
- IV Support, Uses a cryptographically secure IV to ensure ciphertext uniqueness, even with the same key and plaintext.
- Name FiXOR Changed to DPJ.
### Changed
- Encrypted Metadata with AES.
- Choose or Autogenerate Passphrase more complex.
- Progressbar Built-in(no Module needs anymore)
- Disclosure
- Better CLI Parameters
- Encrypt data with Multi-Layer Linear Transformation:
  A layered sequence of simple but powerful operations applied to the data:
  - **Subtraction** using the derived key
  - **XOR** using the derived key
  - **Addition** using the derived key
  - Final **XOR** with a IV unique.
---

## [2.55.0] - 2022-22-12
### Added
- Password convertion to hash for a better encryption by XORing.
- Password Hashing handled by Bcrypt.
- File integrity check feature.
- Progressbar Module.
- Choose or Autogenerate Passphrase.
- Disclosure.
### Changed
- Encrypted Metadata by Better XORing .
- File Handling.
- No Overwriting.
---

## [1.0.0] - 2020-28-10
### Added
- Encrypted Metadata by XORing.
- Function to scan encrypted files, encrypt and decrypt based on XORing method for content and metadata
- CLI Parameters 
- No Overwriting.
- Encrypt data using XOR with a key.
