import secrets
import string

def generate_secure_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

print("Your Secure Password:", generate_secure_password(16))

# This line keeps the window open
input("\nPress Enter to exit...")
