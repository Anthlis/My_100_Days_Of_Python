import secrets, string

# secret_key_gen = secrets.token_hex(8).upper()

def gen_key(parts=4, chars_per_part=8):
    result = []
    for i in range(parts):
        secret_key_gen = secrets.token_hex(8).upper()
    for x in range(chars_per_part):
        result.append(''.join(secret_key_gen))
    return '-'.join(result)
     
     
print(gen_key())