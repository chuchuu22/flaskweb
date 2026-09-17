from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', method=['GET'])
def listening():
    articles = list(db.articles.fine({}, {'_id:False'}))
    return jsonify


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)