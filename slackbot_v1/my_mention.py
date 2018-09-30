# coding: utf-8

from slackbot.bot import respond_to     
from slackbot.bot import listen_to      
from slackbot.bot import default_reply  

import gensim


model1 = gensim.models.Doc2Vec.load('../model1/model/doc2vec.model')
model2 = gensim.models.Doc2Vec.load('../model2/model/doc2vec.model')
model3 = gensim.models.Doc2Vec.load('../model3/model/doc2vec.model')
model4 = gensim.models.Doc2Vec.load('../model4/model/doc2vec.model')


def_word = 'デフォルトの返事です'

@default_reply()
def default_func(message):
    message.reply(def_word)     # def_wordの文字列を返す

@respond_to(r'^m1\s+\S.*')
def set_default_func(message):
    text = message.body['text']     # メッセージを取り出す
    t1, t2, t3 = text.split('.')    # 設定する言葉を取り出す
    word = t2
    msglist = model1.wv.most_similar([word])
    
    msglist = map(str,msglist)
    l = list()
    
    for name in msglist:
      t11, t22, t33 = name.split("'")
      text1 = t1 + t22 + t3      
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)
    

@respond_to(r'^m2\s+\S.*')
def set_default_func(message):
    text = message.body['text']     # メッセージを取り出す
    t1, t2, t3 = text.split('.')    # 設定する言葉を取り出す
    word = t2
    msglist = model2.wv.most_similar([word])
    
    msglist = map(str,msglist)
    l = list()
    
    for name in msglist:
      t11, t22, t33 = name.split("'")
      text1 = t1 + t22 + t3      
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)

@respond_to(r'^m3\s+\S.*')
def set_default_func(message):
    text = message.body['text']     # メッセージを取り出す
    t1, t2, t3 = text.split('.')    # 設定する言葉を取り出す
    word = t2
    msglist = model3.wv.most_similar([word])
    
    msglist = map(str,msglist)
    l = list()
    
    for name in msglist:
      t11, t22, t33 = name.split("'")
      text1 = t1 + t22 + t3      
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)
    

@respond_to(r'^m4\s+\S.*')
def set_default_func(message):
    text = message.body['text']     # メッセージを取り出す
    t1, t2, t3 = text.split('.')    # 設定する言葉を取り出す
    word = t2
    msglist = model4.wv.most_similar([word])
    
    msglist = map(str,msglist)
    l = list()
    
    for name in msglist:
      t11, t22, t33 = name.split("'")
      text1 = t1 + t22 + t3      
      l.append(text1)
    
    replist = map(str,l)
    repmsg = ',\n'.join(replist)
    repmsg = repmsg.encode('utf-8')

    message.reply(repmsg)
