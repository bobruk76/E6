import json
import os
import redis

host = str(os.environ.get("REDIS_HOST", "localhost"))
port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.StrictRedis(host=host, port=port, db=1)

def init_redis():
    if not r.exists('fib_memory', 'fib_max'):
        r.set('fib_memory', json.dumps({0: 0, 1: 1}))
        r.set('fib_max', json.dumps(1))

def fib(num):
    init_redis()
    fib_memory = json.loads(r.get('fib_memory'))

    fib_max = json.loads(r.get('fib_max'))
    if num <= fib_max:
        return fib_memory[str(num)]
    for item in range(fib_max+1, num+1):
        fib_memory[str(item)] = fib_memory[str(item-2)] + fib_memory[str(item-1)]
    r.set('fib_max', json.dumps(num))
    r.set('fib_memory', json.dumps(fib_memory))
    return fib_memory[str(num)]
