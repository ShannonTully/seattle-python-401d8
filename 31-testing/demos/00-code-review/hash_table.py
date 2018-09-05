from functools import reduce
from linked_list import LinkedList as LL


class HashTable:
    def __init__(self, max_size=1024):
        self.max_size = max_size
        # self.buckets[LL()] * self.max_size
        self.buckets = [LL() for _ in range(self.max_size)]

    def hash_key(self, key):
        if type(key) is not str:
            raise TypeError

        # iterate through key, and convert each char to ascii char code
        # sum all char codes for a total int value
        # return => mod total by number of buckets

        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets
        # JS Reduce => [1, 2, 3].reduce((acc, curr) => acc + curr, {})

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.buckets

    def set(self, key, val):
        # hash the key; get a location for the bucket to insert into
        # set val into bucket

        # You will handle collissions here...
        # Your values may look something like a DB record:
            # {
            #     'id': '123',
            #     'name':'xxx',
            #     'title': 'zzz',
            # }

        # self.buckets[self.hash_key(key)] = val
        # --------------------- #

        # Hash the key for a location in buckets
        return self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key, filter=None):
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
