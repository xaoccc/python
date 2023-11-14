# Here we will put queries and interactions with the database.
# Here we will write functions to perform various database operations

from models import User, Order
from main import Session

with Session() as session:

    #      1. CREATE user in db table users, model name: User
    #     new_user = User(username="Emily", email="emily@john.jon")
    #     session.add(new_user)
    #     session.commit()

    #   1.1. CREATE many users:
    #     many_users = [
    #         User(username="john_doe", email="john.doe@example.com"),
    #         User(username="sarah_smith", email="sarah.smith@gmail.com"),
    #         User(username="mike_jones", email="mike.jones@company.com"),
    #         User(username="emma_wilson", email="emma.wilson@domain.net"),
    #         User(username="david_brown", email="david.brown@email.org"),
    #     ]
    #     session.add_all(many_users)
    #     session.commit()
    # 1.2. CREATE many orders:
    #     many_orders = [
    #         Order(user_id=13),
    #         Order(user_id=14),
    #         Order(user_id=15)
    #     ]
    #     session.add_all(many_orders)
    #     session.commit()

    #   2. SEARCH. Retrieve data from db table users, model name User
    #     users = session.query(User).all()
    #     for user in users:
    #         print(user.username, user.email)

    #   3. UPDATE. Find a user, then update his/her email, print a message email is updated and save it to the db
    #     user = session.query(User).filter_by(username="Lana").first()
    #     if user:
    #         user.email = f"{user.username.lower()}@gmail.com"
    #         session.commit()
    #         print(f"The email if {user.username} is updated successfully")
    #     else:
    #         print("User not found")

    #   4. DELETE user. Find a user, then delete it, print a message
    #     user = session.query(User).filter_by(username="Misho Shamara").first()
    #     if user:
    #         session.delete(user)
    #         session.commit()
    #         print(f"The user is deleted successfully")
    #     else:
    #         print("User not found")

    #  5. Transactions

    # try:
    #     session.begin()
    # We can delete all users:
        # session.query(User).delete()
    # Or select/filter which users should be deleted:
    #     session.query(User).filter(User.username.like('%m%')).delete()
    #     session.commit()
    #     print("Users deleted successfully")
    #
    # except Exception as e:
    #     session.rollback()
    #     print("Error occurred and users could not be deleted:", str(e))
    #
    # finally:
    #     session.close()

    # 6. Queries
    orders = session.query(Order).filter_by(is_completed=False)

    if not orders:
        print("No orders available")
    else:
        for order in orders:
            order.is_completed = True
            session.commit()
        print("Completed all orders")
