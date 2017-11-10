# empty slice index defaults:
#   - beginning: 0
#   - ending: length of string

s = "abc"
n = len(s)

for i in range (0, n):
    print s[i]

    
print "s =", s
print "s[-1] =", s[-1]
print "s[0:n-1] =", s[0:n-1]
print "s[0:-1] =", s[0:-1]
print "s[:2] =", s[:2]
print "s[:] =", s[:]
print "s[1:] =", s[1:]
