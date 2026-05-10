'''Assignment (03/04/2026)

Assignment Name : NLP Mini App
Description : Build a chatbot, fake news detector, or keyword extractor.
'''
#Chatbot using NLP
def chatbot():
    print("Chatbot: Hello! I am your assistant.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            print("Bot: Hi Akshitha!")

        # How are you
        elif any(word in user_input for word in ["how are you", "how are u"]):
            print("Bot: I am fine. How about you?")

        # Name
        elif "your name" in user_input:
            print("Bot: I am an NLP chatbot.")

        # Course
        elif "course" in user_input:
            print("Bot: You are studying MCA.")

        # Exit
        elif "bye" in user_input:
            print("Bot: Goodbye!")
            break

        # Default
        else:
            print("Bot: Sorry, I didn't understand that.")

# Run chatbot
chatbot()

#output
'''Chatbot: Hello! I am your assistant.
Type 'bye' to exit.

You: HI
Bot: Hi Akshitha!
You: how are You
Bot: I am fine. How about you?
You: Your name
Bot: I am an NLP chatbot.
You: jk
Bot: Sorry, I didn't understand that.
You: bye
Bot: Goodbye!'''