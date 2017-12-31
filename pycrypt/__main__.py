'''
pycrypt is a module used for symmetric encryption of plain text documents.
Intended use is to be over the command line, to invoke __main__.py.
functions exist in crypt to aid the creation of fernet keys from an md5 hash.
'''
from pycrypt.crypt import generate_key, encrypt, decrypt
from getpass import getpass
import sys
import argparse


def is_arg_set(arg):
    '''
    checks if a given argument is not None
    '''
    return arg != None


def main():
    '''
    Main routine for program
    '''

    parser = argparse.ArgumentParser(
        description='Symmetric encryption tool for plain text files.',
        prog='pycrypt',
        allow_abbrev=True
    )
    parser.add_argument('--encrypt', metavar='FILE', type=str,
                        help='Path to file')

    parser.add_argument('--decrypt', metavar='FILE', type=str,
                        help='Path to file')

    args = parser.parse_args()

    if args.encrypt != None and args.decrypt != None:
        raise argparse.ArgumentError(None, 'encrypt and decrypt options are mutually exclusive')



    key = getpass()

    fernet = generate_key(key)

    if is_arg_set(args.encrypt):

        file_name = args.encrypt

        with open(file_name, 'r') as file:
            content = file.read()

        encrypted_content = encrypt(fernet, content)

        with open(file_name, 'wb') as file:
            file.write(encrypted_content)


    elif is_arg_set(args.decrypt):

        file_name = args.decrypt

        with open(file_name, 'rb') as file:
            content = file.read()

        decrypted_content = decrypt(fernet, content)

        with open(file_name, 'w') as file:
            file.write(decrypted_content.decode())


main()
