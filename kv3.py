# Adds append to log file

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

