while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Chatbot: Hi!")
    elif user == "how are you":
        print("Chatbot: I'm fine, thanks!")
    elif user == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: I don't understand.")
