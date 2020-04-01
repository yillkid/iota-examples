import string
import random

seed = ''.join(random.choice(string.ascii_uppercase + "9") for _ in range(81))
print(seed)
