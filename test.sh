#!/usr/bin/env bash
set -e

mkdir out || echo "directory ./out exists"
cd out

echo 'More secret than top secret' > plain.txt

yorke xor plain.txt <(cat /dev/urandom | tee key.txt) > cipher.txt
yorke xor cipher.txt key.txt > plain2.txt
diff <(xxd plain.txt) <(xxd plain2.txt)

echo "Tests Ran Successfully"
