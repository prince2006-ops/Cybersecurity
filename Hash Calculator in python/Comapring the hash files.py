import  hashlib
def hash_function(filename):
    h=hashlib.sha224()
    with open(filename ,'rb') as f:
        while True:
            chunk=f.read(1024)
            if not  chunk:
                break
            h.update(chunk)
    return h.hexdigest()

hash_value1=hash_function('a.txt')
hash_value2=hash_function('b.txt')
if hash_value1==hash_value2:
    print("The hash value for both is same.")
else:
    print("The hash value for both is different")
