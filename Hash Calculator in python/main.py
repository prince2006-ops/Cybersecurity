import hashlib
def hash_file(filename):
    #this function passes the SHA-1

    h=hashlib.sha1()
    with open(filename,'rb') as file:
        chunk=0
        while chunk!=b'':
            chunk= file.read(1024)
            h.update(chunk)
    return h.hexdigest()
message=hash_file("a.txt")
print(message)