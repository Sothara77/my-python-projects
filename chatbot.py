#chatbot
import random
import time
chatplaces = ["park run", "trail running", "road racing"]
print("welcome to chatbot")
name = input("what is your name? ")
print("hey there", name, "it's nice to meet you!")
place = input("what is your favorite type of run? ")
time.sleep(2)
print("That sound great i really love", random.choice(chatplaces))
day = input("have you had any run today? ")
day = day.lower()
if day == "yes":
    print("well i hope tomorrow is better")
    print("Really enjoyed the chat, speak to you again soon.")
