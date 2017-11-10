
data = {"apples": 12, "oranges": 8, "pears": 4}

# Format:
# key: [key_sz value_sz, file_pos] 
key_dir = {}

# persist to store
f = open ("active.log", 'ab')


# Format to write
# key_sz : value_sz : key : value 

def rec_write (key, value):
    print("rec_write: " + key + ":" + str(value))
    file_pos = 0
    key_sz = len (key)
    value_sz = len (str(value))
    s = str(key_sz) + str(value_sz) + key + str(value)
    s = bytes (s.encode('ascii'))
    file_pos = f.tell()  # get current file offset
    f.write (s)
    key_dir[key] = [key_sz, value_sz, file_pos]
        
    
for d in data:
    rec_write(d, data[d])
    
f.close()

print("Dump key_dir:")

for k in key_dir:
    print (k, key_dir[k])

# Open file in binary mode for read
f = open ("active.log", 'rb')

def record_read (key):
    file_pos = key_dir[key][2]
    print ("file_pos: %d" % file_pos)
    value_sz = key_dir[key][1]
    print ("value_sz: %d" % value_sz)
    key_sz = key_dir[key][0]
    print ("key_sz: %d" % key_sz)
    
    f.seek(file_pos + 2 + key_sz)
    val = f.read(value_sz).decode('ascii')
    print("Value (from file) for %s = %s" % (key, val))

record_read("oranges")
record_read("pears")
record_read("apples")    

f.close()
