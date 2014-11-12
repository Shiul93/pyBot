
import traceback

import time

import random

import datetime

import sys

import cleverbot




def conversation(f):
    # instantiate two Cleverbot objects
    stdin = sys.stdin
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
