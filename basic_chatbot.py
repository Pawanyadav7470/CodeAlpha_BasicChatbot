print("🤖 Welcome to SmartBot! Type 'bye' anytime to end the chat.")

while True:
    user = input("\nYou: ").lower()

    if any(greet in user for greet in ['hello', 'hi', 'hey']):
        print("Bot 😊: Hello there! How can I assist you today?")
    
    elif 'name' in user:
        print("Bot 🤖: I'm SmartBot, your friendly chatbot buddy!")
    
    elif 'how are you' in user:
        print("Bot 🙂: I'm just a bunch of code, but I'm doing great! How about you?")
    
    elif 'bye' in user or 'exit' in user:
        print("Bot 👋: Goodbye! Take care and have a wonderful day.")
        break
    
    else:
        print("Bot ❓: I'm sorry, I didn't understand that. Can you try saying it differently?")
