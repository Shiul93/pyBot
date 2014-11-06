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

import socket

class IRCClient:
    socket = None
    connected = False
    nickname = 'ShiulTroller'
    channels = ['#ProyectoMagallanes']
    server='irc.Mibbit.Net'
    
    def __init__(self,server,channel,nickname):
        self.socket = socket.socket()
        self.socket.connect((server, 6667))
        self.send("NICK %s" % nickname)
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':nickname})
        cleverbot_client_one = cleverbot.Cleverbot()
        exit=True
        while exit==True:
            buf = self.socket.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()

                if data == '':
                    continue
                print "I<", data

                # server ping/pong?
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    self.send('PONG :' + n)
                    if self.connected == False:
                        self.perform()
                        self.connected = True

                args = data.split(None, 3)
                if len(args) != 4:
                    continue
                ctx = {}
                ctx['sender'] = args[0][1:]
                ctx['type']   = args[1]
                ctx['target'] = args[2]
                ctx['msg']    = args[3][1:]

                # whom to reply?
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]

                # some basic commands
                if ctx['msg'] == '!help':
                    self.say('available commands: !help', target)

                if ctx['msg'].startswith('***')==True:
                    self.say('Bienvenido al canal de Proyecto Magallanes '+ctx['msg'].split()[1]+'!', target)
                # directed to the bot?
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(nickname)] == nickname.lower() or ctx['target'] == nickname):
                    # something is speaking to the bot
                    query = ctx['msg']
                    if ctx['target'] != nickname:
                        query = query[len(nickname):]
                        query = query.lstrip(':,;. ')
                    # do something intelligent here, like query a chatterbot
                    print 'someone spoke to us: ', query
                    if query== 'pirate':
                        exit=False
                        self.say('Adios mundo cruel', target)

                    elif query=='':
                        self.say('Que?', target)

                    elif query=='VERSION':
                        exit=True

                    elif query=='caracruz':

                        self.say('Iniciando protocolo de lanzamiento numismatico!', target)
                        time.sleep(1)
                        
                       
                        res=random.random()
                        if res>0.4:
                            self.say('Ha salido: Cara!', target)
                        elif (res<0.4) & (res>0.6):
                            time.sleep(1)
                            self.say('...', target)
                            time.sleep(1)
                            self.say('...', target)
                            time.sleep(1)
                            self.say('Os quedais con cara de tontos al ver que ha quedado de canto!', target)
                        else:
                            self.say('Ha salido:  Cruz!', target)


                    elif query.startswith('ahora te llamas'):
                        self.send("PRIVMSG R : Login <>")
                        self.send("MODE %s +x" % query.split()[3])
                    

                        
                    else:
                        response = cleverbot_client_one.ask(query)
                        self.say(response, target)

    def send(self, msg):
        print "I>",msg
        self.socket.send(msg+"\r\n")

    def say(self, msg, to):
        self.send("PRIVMSG %s :%s" % (to, msg))

    def perform(self):
        self.send("PRIVMSG R : Register <>")
        self.send("PRIVMSG R : Login <>")
        self.send("MODE %s +x" % self.nickname)
        for c in self.channels:
            self.send("JOIN %s" % c)
            # say hello to every channel
            ###time.sleep(3)
            ##self.say('Sabes aquel que dice...', c)
            #time.sleep(5)
            #self.say('...que van dos bots y se cae el de enmedio?', c)
            #time.sleep(3)
            #self.say('yoqsetio xdxd', c)
            self.say('ShiulTroller v0.2 online, hola a todos :D', c)





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
    nickname = 'Mush'
    channels = '#ProyectoMagallanes'
    server='irc.Mibbit.Net'
    
    client=IRCClient(server,channels,nickname)
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