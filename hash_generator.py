import hashlib

# generate hash of given string
def generate_hash(input_string):
    # generate a SHA-256 hash for the given input string
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode("utf-8"))
    return sha256_hash.hexdigest()


input_data = "Hello, world"
hash_result = generate_hash(input_data)
print(f'The SHA-256 hash of "{input_data}" is: {hash_result}')