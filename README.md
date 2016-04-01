# Yorke

Yorke is an experimental encryption library and command-line tool.

# Usage

Encrypt a file using a randomly generated pad. The encrypted cipher text is
sent to STDOUT and the random pad is sent STDERR:

```
cat plain.txt | yorke random_pad 1> cipher.txt 2> key.txt
cat plain.txt | yorke rp         1> cipher.txt 2> key.txt
```

Decrypt a file using a previously generated pad:

```
yorke file_xor cipher.txt key.txt > plain.txt
yorke fxor key.txt cipher.txt > plain.txt
```

# Installation

```
git clone https://github.com/ldgr/yorke.git
cd yorke
python setup.py install
```

# Testing

Library:
```
pip install nose
nosetests
```

Command:
```
./test.sh
```
