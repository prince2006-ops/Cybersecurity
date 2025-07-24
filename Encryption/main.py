from cryptography.fernet import Fernet

key=Fernet.generate_key()
chiper=Fernet(key)
text="hi, My name is pricne bartaula".encode()
encrypted_data=chiper.encrypt(text)
decrypted_data=chiper.decrypt(encrypted_data)

print(encrypted_data)
print(decrypted_data.decode())