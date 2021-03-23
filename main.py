from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Test")
conv = open("chats.txt", "r").readlines()

# bot.set_trainer(ListTrainer)
# bot.train(conv)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)

while True:
    request = input("You: ")
    response = bot.get_response(request)
    print("Bot: ", response)