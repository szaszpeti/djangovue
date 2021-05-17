import random
import string

APHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRIN_LENGTH = 6

def generate_random_string(chars=APHANUMERIC_CHARS, length=STRIN_LENGTH):
	return "".join(random.choice(chars) for _ in range(length))