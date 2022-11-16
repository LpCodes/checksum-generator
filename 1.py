import hashlib

file = "../apitestng.7z"


def get_cheksum(file):
    with open(file, 'rb') as file:
        data = file.read()
        # print(data)
        hasheddata = hashlib.md5(data).hexdigest()
        print(hasheddata)
        hasheddata = hashlib.sha256().hexdigest()
        print(hasheddata)
        hasheddata = hashlib.sha1().hexdigest()
        print(hasheddata)
        hasheddata = hashlib.sha224().hexdigest()
        print(hasheddata)
        hasheddata = hashlib.sha3_384().hexdigest()
        print(hasheddata)


get_cheksum(file)
