from crypto_utils.crypto_utils import *



username = 'test_username'
password = 'test_password'

key_file = r'tests\test.key'

generate_key(key_file)

encrypted_username = encrypt(username, key_file)
print(encrypted_username)
decrypted_username = decrypt(encrypted_username, key_file)
print(decrypted_username)
