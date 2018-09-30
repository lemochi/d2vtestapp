# coding: utf-8

from slackbot.bot import respond_to     
from slackbot.bot import listen_to      
from slackbot.bot import default_reply  

import requests
import gensim

def_word = 'デフォルトの返事です'

@default_reply()
def default_func(message):
    message.reply(def_word)     # def_wordの文字列を返す

#model1
@respond_to(r'^m1\s+\S.*')
def set_default_func(message):

    text = message.body['text']                   # メッセージを取り出す
    t1, t2, t3 = text.split('.')                  # ..で囲まれた言葉を取り出す
    apiURL = 'http://0.0.0.0:3000/model1/' + t2   # API用URL生成
    dic = requests.get(apiURL).json()             # APIでJSON取得

    l = list()
    
    for k in dic.keys():
      text1 = t1 + k + t3
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)
    
#model2
@respond_to(r'^m2\s+\S.*')
def set_default_func(message):

    text = message.body['text']                   # メッセージを取り出す
    t1, t2, t3 = text.split('.')                  # ..で囲まれた言葉を取り出す
    apiURL = 'http://0.0.0.0:3000/model2/' + t2   # API用URL生成
    dic = requests.get(apiURL).json()             # APIでJSON取得

    l = list()
    
    for k in dic.keys():
      text1 = t1 + k + t3
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)

#model3
@respond_to(r'^m3\s+\S.*')
def set_default_func(message):

    text = message.body['text']                   # メッセージを取り出す
    t1, t2, t3 = text.split('.')                  # ..で囲まれた言葉を取り出す
    apiURL = 'http://0.0.0.0:3000/model3/' + t2   # API用URL生成
    dic = requests.get(apiURL).json()             # APIでJSON取得

    l = list()
    
    for k in dic.keys():
      text1 = t1 + k + t3
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)

#model4
@respond_to(r'^m4\s+\S.*')
def set_default_func(message):

    text = message.body['text']                   # メッセージを取り出す
    t1, t2, t3 = text.split('.')                  # ..で囲まれた言葉を取り出す
    apiURL = 'http://0.0.0.0:3000/model4/' + t2   # API用URL生成
    dic = requests.get(apiURL).json()             # APIでJSON取得

    l = list()
    
    for k in dic.keys():
      text1 = t1 + k + t3
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)
