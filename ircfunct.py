
import traceback

import time

import random

import sys

import cleverbot

import socket



class IRCClient:
    socket = None
    connected = False
    nickname = 'nick'
    channels = ['#ProyectoMagallanes']
    server='server'
    
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
                        #self.socket.shutdown(SHUT_WR)
                        self.socket.close()
                        

                    elif query=='':
                        self.say('Que?', target)

                    elif query=='VERSION':
                        self.send("PRIVMSG R : Version 0.2")

                    elif query=='caracruz':

                        self.say('Iniciando protocolo de lanzamiento numismatico!', target)
                        time.sleep(1)
                        
                       
                        res=random.random()
                        if res>0.4:
                            self.say('Ha salido: Cara!', target)
                        elif (res>0.4) & (res<0.6):
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
            self.say('Hola', c)
            time.sleep(15)