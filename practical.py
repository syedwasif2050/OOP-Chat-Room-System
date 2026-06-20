

class User:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.history = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.username} has joined the {self.name} room.")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.username} has left the {self.name} room.")

    def send_message(self, sender, content):
        msg = Message(sender, content)


        self.history.append(msg)
        print(f"Message sent by {sender.username}")

    def view_history(self):
        print(f"\n--- {self.name} Chat History ---")
        for msg in self.history:
            print(f"{msg.sender.username}: {msg.content}")

# Implementation
room = ChatRoom("Python Developers")
user1 = User("Ali")
user2 = User("Sara")

room.join(user1)
room.join(user2)

room.send_message(user1, "Hello everyone!")
room.send_message(user2, "Hi Ali, how are you?")

room.view_history()
room.leave(user1)