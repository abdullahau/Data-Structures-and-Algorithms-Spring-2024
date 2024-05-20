from random import choices, randint
from string import ascii_lowercase

def find(N):
    hashes = {}
    
    while True:
        wordlen = randint(1,10)
        x = ''.join(choices(ascii_lowercase, k=wordlen))
        hash_value = hash(x) % N
        
        if hash_value in hashes:
            return (hashes[hash_value], x)

        hashes[hash_value] = x