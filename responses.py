def grabResponse(message: str) -> str:
    userMessage = message.lower()
    
    if userMessage == "hello":
        return 'Hi there!'
