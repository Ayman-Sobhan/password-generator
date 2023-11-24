import string, secrets
pass_len = int(input("Enter the length of your password: "))
def gen_pass(length):
    chars = string.ascii_letters
    digits = string.digits
    punc = string.punctuation
    random_password = ''.join(secrets.choice(chars+digits+punc) for _ in range(length))
    return random_password
print(gen_pass(pass_len))
