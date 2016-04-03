# Yorke

Yorke is an experimental stream cipher library and command-line tool.

# Usage

Encrypt a message with a random pad:

```bash
yorke xor <(echo "secret message") <(cat /dev/urandom | tee key.txt) > cipher.txt
yorke xor cipher.txt key.txt
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
