from random import randint 

magic_string = "keyboarding_"
magic_list = list(magic_string)

base_string = "abcdefghijklmnopqrstuvwxyz_"
base_list = list(base_string)

encoded_dict = {}
count = 100

# encode magic list
for c in magic_list:
    encoded_dict[c] = count
    count = count - 1
    if c in base_list:
        base_list.remove(c)

# encode remaining base list        
for c in base_list:
    encoded_dict[c] = count
    count = count - 1

keys = encoded_dict.keys()
encoded_string = ""

while len(keys) > 0:
    key = keys[randint(0, len(keys) - 1)]
    if encoded_dict[key] > 0:
        encoded_string = encoded_string + key
        encoded_dict[key] = encoded_dict[key] - 1
    elif encoded_dict[key] == 0:
        keys.remove(key)

print(encoded_string)    
    
