import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# from main_app.models import UserProfile, Message
#
# # Create queries within functions
# # Create users
# user1 = UserProfile.objects.create(username='john_doe', email='john@example.com', bio='Hello, I am John Doe.')
#
# user2 = UserProfile.objects.create(username='jane_smith', email='jane@example.com', bio='Hi there, I am Jane Smith.')
#
# user3 = UserProfile.objects.create(username='alice', email='alice@example.com', bio='Hello, I am Alice.')
#
# # Create a message from user1 to user2
# message1 = Message.objects.create(
#     sender=user1,
#     receiver=user2,
#     content="Hello, Jane! Could you please tell Alice that tomorrow we are going on vacation?")
# print(message1.content)
#
# # Mark the message as read
# message1.mark_as_read()
# print(f"Is read: {message1.is_read}")

# Create a reply from user2 to user1
reply_message = message1.reply_to_message(
    receiver=user1,
    reply_content="Hi John, sure! I will forward this message to her!")
print(reply_message.content)

# Create a forwarded message from user2 to user3
forwarded_message = message1.forward_message(sender=user2, receiver=user3)
print(f"Forwarded message from {forwarded_message.sender.username} to {forwarded_message.receiver.username}")
