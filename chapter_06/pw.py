#! /usr/bin/python3
# -*- coding: utf-8 -*-

# pw.py - password generator and keeper

PASSWORDS = {
    'email': 'my_email_password',
    'blog': 'my_blog_password',
    'luggage': '12345',
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    try:
        pyperclip.copy(PASSWORDS[account])
        print(f'Password for {account} copied to clipboard.')
    except pyperclip.PyperclipException:
        print(f'Password for {account}: {PASSWORDS[account]}')
else:
    print(f'There is no account named {account}.')

