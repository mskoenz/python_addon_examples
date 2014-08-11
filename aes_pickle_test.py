#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    11.08.2014 19:22:51 CEST
# File:    aes_pickle_test.py

from addon import aesPickle

if __name__ == "__main__":
    print("test_aes_pickle.py")
    message = "this is the message"
    
    key = input("enter key for encryption: ")
    cipher = aesPickle.dumps(message, key)
    
    key = input("enter key for decryption: ")
    message_decrypt = aesPickle.loads(cipher, key)
    
    print(message_decrypt)
