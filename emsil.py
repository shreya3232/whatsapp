import random

def scramble_email(email):
    username, domain = email.split('@')

    # Scramble the username
    scrambled_username = ''.join(random.sample(username, len(username)))

    # Generate a random number for the domain
    random_number = random.randint(1000, 9999)

    # Create the scrambled email address
    scrambled_email = scrambled_username + str(random_number) + '@' + domain

    return scrambled_email

# Example usage
email = 'shreyasgowda1436@gmail.com'
scrambled_email = scramble_email(email)
print(scrambled_email)
