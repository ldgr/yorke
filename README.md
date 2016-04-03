# Yorke

Yorke is an experimental stream cipher library and command-line tool.

# Usage

Encrypt a message with a random pad:

```bash
yorke xor <(echo "secret message") <(cat /dev/urandom | tee key.txt) > cipher.txt
yorke xor cipher.txt key.txt
```

Encrypt a message with a deterministic, pseudo-random stream:

```bash
yorke xor <(echo "secret message") <(yorke sha256 `uuidgen | tee key.iv`) > cipher.txt
yorke xor cipher.txt <(yorke sha256 `cat key.iv`) | xxd
```

WARNING: Never re-use the same initialization vector! It is feasible to recover
the initialization vector by XOR'ing two ciphertexts generated against the
common stream. Observe the following:

```bash
yorke xor <(echo "SSN: 512-73-5461") <(yorke sha256 `uuidgen | tee key.iv`) > cipher1.txt
yorke xor <(echo "SSN: 389-16-2734") <(yorke sha256 `cat key.iv`) > cipher2.txt

xxd cipher1.txt
  0000000: 641a c768 a61c 4d2e dd58 abd9 ad05 451c  d..h..M..X....E.
  0000010: 17                                       .

xxd cipher2.txt
  0000000: 641a c768 a61a 4425 dd5e aed9 aa06 4019  d..h..D%.^....@.
  0000010: 17                                       .

yorke xor cipher1.txt cipher2.txt | xxd
  0000000: 0000 0000 0006 090b 0006 0500 0703 0505  ................
  0000010: 00

```

# Installation

```bash
git clone https://github.com/ldgr/yorke.git
cd yorke
python setup.py install
```

# Testing

Run library tests:
```bash
pip install nose
nosetests
```

Run command tests:
```bash
./test.sh
```
