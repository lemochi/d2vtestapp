# -*- coding: utf-8 -*-

import json
from functools import wraps

from flask import Flask, jsonify, request, url_for, abort, Response

import gensim

app = Flask(__name__)

# モデル読み込み
mod1 = gensim.models.Doc2Vec.load('../model1/model/doc2vec.model')
mod2 = gensim.models.Doc2Vec.load('../model2/model/doc2vec.model')
mod3 = gensim.models.Doc2Vec.load('../model3/model/doc2vec.model')
mod4 = gensim.models.Doc2Vec.load('../model4/model/doc2vec.model')

@app.route('/model1/<string:word>', methods=['GET'])
def read1(word):
   result = mod1.wv.most_similar([word])
   resultdict = dict(result) 
   response = json.dumps(resultdict)

   return response

@app.route('/model2/<string:word>', methods=['GET'])
def read2(word):
   result = mod2.wv.most_similar([word])
   resultdict = dict(result) 
   response = json.dumps(resultdict)

   return response

@app.route('/model3/<string:word>', methods=['GET'])
def read3(word):
   result = mod3.wv.most_similar([word])
   resultdict = dict(result) 
   response = json.dumps(resultdict)

   return response

@app.route('/model4/<string:word>', methods=['GET'])
def read4(word):
   result = mod4.wv.most_similar([word])
   resultdict = dict(result) 
   response = json.dumps(resultdict)

   return response


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)
