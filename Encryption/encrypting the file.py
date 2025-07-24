from cryptography.fernet import Fernet

# Generate key once and keep it accessible (in memory or save to file)
key = Fernet.generate_key()
cipher = Fernet(key)

def encryption():
    filename = 'a.txt'
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_file = cipher.encrypt(data)
    with open(filename + ".encrypted", 'wb') as f:
        f.write(encrypted_file)

def decryption():
    filename = 'a.txt.encrypted'  # Read encrypted file here!
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    # Write decrypted data back as text (decode bytes)
    with open('a.txt.decrypted', 'w') as f:
        f.write(decrypted_data.decode())

# Run encryption and then decryption
encryption()
decryption()
