import random
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only required for the first time)
nltk.download('punkt')

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! How can I assist you?", "Hey! What can I do for you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!", "All good here! How about you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatBot!", "I'm ChatBot, your virtual assistant."]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and help you with basic tasks.", "I'm here to have conversations and assist you with information."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"what is (.*) ?",
        ["I'm not sure about %1, but I can look it up for you!", "I don't know much about %1, but I can try to help."]
    ],
    [
        r"i need (.*)",
        ["Why do you need %1?", "I can help you with %1. Can you tell me more?"]
    ],
    [
        r"i feel (.*)",
        ["Why do you feel %1?", "It's okay to feel %1. Do you want to talk about it?"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad to help!"]
    ],
    [
        r"default",
        ["I'm not sure I understand. Can you rephrase that?", "Could you elaborate on that?", "I didn't get that. Can you say it again?"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def start_chat():
    print("ChatBot: Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
