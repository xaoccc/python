# Here we will put queries and interactions with the database.
# Here we will write functions to perform various database operations

from models import User
from main import Session


with Session() as session:

#      1. Create data in db table users, model name User
#     new_user = User(username="Emily", email="emily@john.jon")
#     session.add(new_user)
#     session.commit()

#   2. Retrieve data from db table users, model name User
#     users = session.query(User).all()
#     for user in users:
#         print(user.username, user.email)

#   3. Find a user, then update his/her email, print a message email is updated and save it to the db
    user = session.query(User).filter_by(username="Lana").first()
    if user:
        user.email = f"{user.username.lower()}@gmail.com"
        session.commit()
        print(f"The email if {user.username} is updated successfully")
    else:
        print("User not found")

