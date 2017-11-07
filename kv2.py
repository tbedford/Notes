# Problems:
# 1. Volatile
# 2. Limited by RAM


class KeyValueStore:
    """World's simplest (in memory) key-value store"""

    def __init__ (self):
        self.key_table = {}

    def put (self, key, value):
        self.key_table[key] = value

    def get (self, key):
        if key in self.key_table:
            return self.key_table[key]

    def delete (self, key):
        if key in self.key_table:
            del self.key_table[key]


kv = KeyValueStore()

document = '{"title": "This is the title", "tags": ["Python", "Blogpost", "Django"]}'


kv.put("doc1", document) 

print (kv.get("doc1"))

kv.put("apples", 12)
kv.put("pears", 7)
kv.put("oranges", 8)

print (kv.get("apples"))
print (kv.get("oranges"))
print (kv.get("pears"))
print (kv.get("starfruits"))

kv.delete("apples")

print (kv.get("apples"))

