"""Cleverbot chats with himself."""
import traceback

import cleverbot

import time

import random

import datetime

import sys

import irc

f = open('clever.log','a')
stdin = sys.stdin

def conversation():
    # instantiate two Cleverbot objects
    
    cleverbot_client_one = cleverbot.Cleverbot()
    cleverbot_client_two = cleverbot.Cleverbot()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    f.write('///////////////////////////////////\n')
    f.write(st+'\n')
    f.write('///////////////////////////////////\n')
    print 'Enter first message, please'
    query=stdin.readline()
    print '>> Cleverbot #1: '+query
    f.write('>> Cleverbot #1: '+query.rstrip()+"\n")
    answer = cleverbot_client_two.ask(query)
    #print '##Answer= '+answer+' ##'
    
    time.sleep(random.random()+2)
    while True:
        if (answer!="")&(not answer.startswith('\n')):
            print '>> Cleverbot #2: {}'.format(answer)
            f.write('>> Cleverbot #2: '+answer+"\n")
        answer = cleverbot_client_one.ask(answer)
        #print '##Answer= '+answer+' ##'
        time.sleep(random.random()+2)
        if (answer!="")&(not answer.startswith('\n')):
            print '>> Cleverbot #1: {}'.format(answer)
            f.write('>> Cleverbot #1: '+answer+"\n")
        time.sleep(random.random()+2)
        answer = cleverbot_client_two.ask(answer)
        #print '##Answer= '+answer+' ##'

def ircBot():
    print
    ircRoboto= irc.bot.SingleServerIRCBot()
 
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
        conversation()
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
        menu()
        
    except Exception, err:
        f.close()
        print traceback.format_exc(err)