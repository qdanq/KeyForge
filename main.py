import string, random

rand = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(12)])
print(rand)