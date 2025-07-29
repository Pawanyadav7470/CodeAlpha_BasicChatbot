# CodeAlpha_BasicChatbot
A rule-based Python chatbot that gives simple responses to user input.
# 🤖 SmartBot – A Simple Python Chatbot

**SmartBot** is a basic command-line chatbot written in Python.  
It responds to simple greetings, questions, and can end the conversation gracefully.

---

## 💬 Features

- Greets user with a friendly message
- Responds to common inputs like:
  - Greetings (`hi`, `hello`, `hey`)
  - Name inquiries (`what's your name?`)
  - Mood (`how are you?`)
  - Exit phrases (`bye`, `exit`)
- Handles unrecognized input with a polite fallback
- Loops until the user says "bye" or "exit"

---

## 🛠️ How to Run

1. Make sure Python is installed.
2. Save the code in a file named `smartbot.py`.
3. Run the program using the terminal or command prompt:

```bash
python smartbot.py


🤖 Welcome to SmartBot! Type 'bye' anytime to end the chat.

You: hi  
Bot 😊: Hello there! How can I assist you today?

You: what's your name  
Bot 🤖: I'm SmartBot, your friendly chatbot buddy!

You: how are you  
Bot 🙂: I'm just a bunch of code, but I'm doing great! How about you?

You: goodbye  
Bot 👋: Goodbye! Take care and have a wonderful day.
