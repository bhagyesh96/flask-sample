import os
import redis
from rq import Worker, Queue, Connection

listen = ['default']
print("#############################Worker Started#####################")
redis_url = os.getenv('REDISTOGO_URL', 'redis://:oqtfTZzsVvqZmm9scwKb5qCjC7FGAdaT@redis-12903.c99.us-east-1-4.ec2.cloud.redislabs.com:12903')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()