import getopt
import sys

from Crypto.Cipher import AES
from Crypto.Util import Counter


def decrypt(key, secret):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    msg = cipher.encrypt(secret)
    return msg



def get_args(argv):
    inputfile = ''
    key = ''
    try:
        opts, args = getopt.getopt(argv, "hi:k:", ["ifile=", "kfile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -k <key>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -k <key>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-k", "--kfile"):
            key = arg
    return inputfile,key


if __name__ == '__main__':
    inputf, key= get_args(sys.argv[1:])

    with open('key.bin', mode='rb') as file:
        key = file.read()

    with open('secret', mode='rb') as file:
        secret = file.read()

    msg = decrypt(key, secret)
    print(str(msg,encoding='utf-8'))
    f = open('msg.txt', "w")
    f.write(str(msg,encoding='utf-8'))
    f.close()


