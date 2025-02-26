# pip install faker

from faker import Faker


def generate_fake_users(num_users=10):
    fake = Faker()
    users = []
    for _ in range(num_users):
        user = {
            'name': fake.name(),
            'address': fake.address().replace("\n", ", "),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'job': fake.job()
        }
        users.append(user)
    return users


# Example usage:
if __name__ == "__main__":
    fake_users = generate_fake_users(5)
    for user in fake_users:
        print(user)


# Why? This snippet leverages the Faker library to generate realistic fake user data. It's perfect for testing,
# prototyping, or seeding databases with dummy data, saving you time and effort while developing your applications
