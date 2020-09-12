
from rq import Queue
from rq.job import Job
from worker import conn
import operator
import requests
import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask import jsonify
from collections import Counter
from bs4 import BeautifulSoup
import os
import re
import time
from flask_caching import Cache


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+BASE_DIR+'/test.db'
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'redis'})
from count_word import *


q = Queue(connection=conn)

from models import *



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def find_result():
    data = json.loads(request.data)
    url = data['url']   
    job = q.enqueue_call(
        func=word_count, args=(url,), result_ttl=5000
    )
    resp = {
      "jobId": job.get_id()
    }
    return resp

@app.route('/analyze_test', methods=['POST'])
def find_result_test():
    data = json.loads(request.data)
    url = data['url'] 
    word_count_data = word_count(url)  
    resp = {
      "jobId": word_count_data
    }
    return resp

@app.route('/result/<job_id>', methods=['GET'])
def results(job_id):
    job = Job.fetch(job_id, connection=conn)
    if job.is_finished:
        result = get_result_db(job)
        results = sorted(
            result.count_data.items(),
            key=operator.itemgetter(1),
            reverse=True
        )
        return jsonify(results)
    else:
        return 'Job Pending', 200

@cache.memoize(timeout=60)
def get_result_db(job):
    return Result.query.filter_by(id=job.result).first()


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
