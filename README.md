# cs361-aes
AES 128 and 256-bit

![Yeah RSA != AES but what can you do?](https://imgs.xkcd.com/comics/security.png)

## How to run:
`python3 aes.py Nk keyfile infile outfile mode`

Nk Should be either 4 (AES 128-bit) or 8 (AES 256-bit).
The keyfile must be either exactly 16 bytes long  for AES-128 or exactly 32 bytes long for AES-256.
If mode is `encrypt`, the infile will be encrypted with the provided key and written to outfile. Otherwise, the provided infile infile will be decrypted.

For example:

![Encrypt](https://raw.githubusercontent.com/connernewman/cs361-aes/master/p1.png)
![Encrypted](https://raw.githubusercontent.com/connernewman/cs361-aes/master/p2.png)
![Decrypt](https://raw.githubusercontent.com/connernewman/cs361-aes/master/p3.png)
