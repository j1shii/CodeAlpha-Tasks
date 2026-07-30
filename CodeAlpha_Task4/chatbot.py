def get_response(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hey there! How can I help you today? "
    
    elif any(word in user_input for word in ["how are you", "how r you", "how are u"]):
        return "I'm doing great, thanks for asking! How about you?"
    
    elif any(word in user_input for word in ["good", "fine", "great", "awesome", "i'm good"]):
        return "That's wonderful to hear! "
    
    elif any(word in user_input for word in ["bad", "sad", "not good", "terrible"]):
        return "Oh no, I'm sorry to hear that. Hope things get better soon! "
    
    elif any(word in user_input for word in ["your name", "who are you", "what are you"]):
        return "I'm Cardsy Bot — a simple chatbot built with Python! "
    
    elif any(word in user_input for word in ["what can you do", "help", "features"]):
        return "I can chat with you, answer simple questions, and keep you company! "
    
    elif any(word in user_input for word in ["time", "what time"]):
        import datetime
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} "
    
    elif any(word in user_input for word in ["date", "today", "what day"]):
        import datetime
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {today} "
    
    elif any(word in user_input for word in ["joke", "tell me a joke", "funny"]):
        return "Why do programmers prefer dark mode? Because light attracts bugs! "
    
    elif any(word in user_input for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        return "Goodbye! Have a wonderful day! "
    
    else:
        return "Hmm, I didn't quite get that. Could you rephrase? "


def main():
    print("=" * 40)
    print("   Welcome to Cardsy Bot ")
    print("   Type 'bye' to exit")
    print("=" * 40)
    print()

    while True:
        user_input = input("You: ")
        if not user_input.strip():
            continue
        response = get_response(user_input)
        print(f"Bot: {response}")
        print()
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()