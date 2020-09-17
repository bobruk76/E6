import redis
r = redis.StrictRedis(host='localhost', port=6379, db=1)
r.hmset('fib_memory', {1: 1, 2: 1, 'max': 2})
def fib(num):
    fib_memory = r.hgetall('fib_memory')
    if num <= fib_memory['max']:
        return fib_memory[num]
    for item in range(fib_memory['max']+1, num+1):
        fib_memory[item] = fib_memory[item-2] + fib_memory[item-1]
    fib_memory['max'] = num
    r.hmset('fib_memory', fib_memory)
    return fib_memory[num]
