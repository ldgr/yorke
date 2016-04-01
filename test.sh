#!/usr/bin/env bash

SECRET='More secret than top secret'

mkdir out
cd out

printf "$SECRET" | yorke random_pad 1> cipher.txt 2> key.txt
printf "$SECRET" | yorke rp         1> cipher.txt 2> key.txt

printf "$SECRET" > expected.txt

yorke file_xor cipher.txt key.txt > plain.txt
diff <(xxd plain.txt) <(xxd expected.txt)

yorke fxor key.txt cipher.txt > plain.txt
diff <(xxd plain.txt) <(xxd expected.txt)

cat key.txt | yorke fxor  cipher.txt > plain.txt
diff <(xxd plain.txt) <(xxd expected.txt)
