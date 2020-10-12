import getopt
import sys

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
from datetime import datetime


def generate_key():
    return get_random_bytes(16)

def get_args(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return inputfile,outputfile


def encrypt(key, message):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    secret = cipher.encrypt(message)

    f = open("secret", "wb")
    f.write(secret)
    f.close()

    f = open("key.bin", "wb")
    f.write(key)
    f.close()
    return secret


if __name__ == '__main__':
    inputf,outputf=get_args(sys.argv[1:])

    key = get_random_bytes(16)

    with open(inputf, mode='rb') as file:
        fileContent = file.read()


    start = datetime.now()

    secret = encrypt(key, fileContent)

    print(datetime.now() - start)


