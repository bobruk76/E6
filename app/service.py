import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)
r.hmset('fib_memory', json.dumps({1: 1, 2: 1}))
r.hmset('fib_max', json.dumps(2))
def fib(num):
    fib_memory = json.loads(r.hgetall('fib_memory'))
    fib_max = json.loads(r.hgetall('fib_max'))
    print(fib_memory)
    if num <= fib_max:
        return fib_memory[num]
    for item in range(fib_memory['max']+1, num+1):
        fib_memory[item] = fib_memory[item-2] + fib_memory[item-1]
    r.hmset('fib_max', json.dumps(num))
    r.hmset('fib_memory', json.dumps(fib_memory))
    return fib_memory[num]
