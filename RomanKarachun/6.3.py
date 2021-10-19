default = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
crypto = "CRYPTOABDEFGHIJKLMNQSUVWXZcryptoabdefghijklmnqsuvwxz"
encode = str.maketrans(default, crypto)
decode = str.maketrans(crypto, default)

def main():
    str = "Hello world"
    print (str.translate(encode))

    str = "Fjedhc dn atidsn"
    print (str.translate(decode))

if __name__ == "__main__":
    main()
