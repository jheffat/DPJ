# Changelog

All notable changes to this project will be documented in this file.

---
## [3.6.0] - 2025-07-06
### Added
- *Menu options*, To select the algorithm to encrypt but AES function is not added yet, also to select Key expansion Level (basic, standard, advanced).
### Changed
- *CLI Upgrade*: Switched to a friendlier and more interactive command-line interface to make the tool easier and more pleasant to use.
- 
## [3.5.5] - 2025-30-05
### Added
- *Password masking* during input for enhanced security.
### Changed
- *Improved key press handling*, ensure key input only affects the current terminal session.


## [3.5.2] - 2025-08-05
### Added
- *Key Schedule*, a process that expands the main encryption key(KDF) into multiple round keys used throughout the encryption rounds to enhance security. 
- *Nonlinear transformation*, Improves resistance to differential and linear cryptanalysis
  - S-box substitution for strong nonlinearity
  - P-box permutation for diffusion
  - XOR mixing with round keys
  - Byte inversion for additional confusion
### Changed
- Better Password Hashing storage + random (salt/iteration count) per file.
- Encryption/Decryption more Faster.

---

## [3.5.0] - 2025-30-04
### Added
- Hash tools included, Hash files/Msg using any theses algorithms (blake2b, sha3_512, sha256, sha1, sha512, shake_128, shake_256, sha3_256, blake2s, md5)
- SHA-256-based *HMAC*.
- *KDF* Support, Passphrases are transformed via a Key Derivation Function before use, making brute-force attempts extremely difficult.
- *IV* Support, Uses a cryptographically secure IV to ensure ciphertext uniqueness, even with the same key and plaintext.
- Name FiXOR Changed to DPJ.
### Changed
- Encrypted Metadata with *AES*.
- Choose or Autogenerate Passphrase more complex.
- Progressbar Built-in(no Module needs anymore)
- Disclosure
- Better CLI Parameters
- Better *Linear Transformation*, increases the unpredictability of plaintext-to-ciphertext mapping while preserving reversibility, acting as a strong  preprocessing stage after [Nonlinear Transformation(🔧🧪Comming soon)]
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
- Encrypt data using *XOR* with a key.