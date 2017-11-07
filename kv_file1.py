# Open file in binary mode for append
f = open ("active.log", 'ab')

# We should always encode (and decode) when leaving (or entering) Python
s1 = bytes("abcd".encode('ascii'))
s2 = bytes("efgh\n".encode('ascii'))

f.write (s1)
f.write (s2)
f.close()

# Open file in binary mode for read
f = open ("active.log", 'rb')

f.seek(0, 0)
c = f.read(1).decode('ascii')
print (c)

f.seek(1, 0)
c = f.read(1).decode('ascii')
print (c)

f.seek(2, 0)
c = f.read(1).decode('ascii')
print (c)

f.seek(3, 0)
c = f.read(1).decode('ascii')
print(c)

