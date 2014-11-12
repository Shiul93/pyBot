"""Cleverbot chats with himself."""
import traceback

import time

import random

import datetime

import sys

import conversation

import cleverbot

import ircfunct

import socket

f = open('clever.log','a')

stdin = sys.stdin

socket = socket.socket() #Socket for the IRC connection



def ircBot():
    nickname = 'Magallanes'
    channels = '#ProyectoMagallanes'
    server='irc.Mibbit.Net'
    
    client=ircfunct.IRCClient(socket,server,channels,nickname)
    del client
    menu()

def testFunct():
    testStr= stdin.readline()
    print testStr
    print '#'
    print testStr.rstrip()
    print '#'

def menu():
    print 'Select functionality'
    print '1:               Conversation'
    print '2:               IRC Bot'
    print 'test:            Test'
    print 'e,q,exit,quit:   Exit'
    menuarg = stdin.readline()
    menuarg= menuarg.rstrip()
    if menuarg== '1':
        conversation.conversation(f)
    elif menuarg== '2':
        ircBot()
    elif menuarg=='test':
        testFunct()
    elif (menuarg=='e')|(menuarg=='exit')|(menuarg=='q')|(menuarg=='quit'):
        print 'Exiting'
        f.close()
    else:
        print 'Invalid input, try again'    
        menu()

        
    
def main():
    
    menu()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        socket.close()
        menu()
        
    except Exception, err:
        f.close()
        print traceback.format_exc(err)