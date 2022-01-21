import hashlib, string, random
from mysite import app

random.seed()

def randstring(length=app.config['RANDOM_LENGTH']):
    cs = list(string.ascii_letters + string.digits)
    random.shuffle(cs)
    return ''.join(cs[:length])

def hashfun(password, salt):
    h = password
    for i in range(app.config['HASH_ROUNDS']):
        h += salt + str(i * i)
        h = hashlib.sha256(h.encode('utf-8')).hexdigest()
    return h