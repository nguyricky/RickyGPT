def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return 'Hi there!'

    return "Sorry I didn't get that!"