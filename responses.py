def get_response(message: str) -> str:
    p_message = message.lower()
    
    if p_message == "!help":
        return (
        "**RickyGPT - Discord Chatbot**\n\n"
        "Hello! I'm RickyGPT, your friendly Discord chatbot powered by OpenAI's GPT-3. I'm here to assist you with various commands and features. Below is a list of available commands and their usage:\n\n"
        "1. `!chat <your_message>`:\n"
        "   - Initiate a chat conversation with me. Just type `!chat` followed by your message, and I'll respond accordingly.\n\n"
        "2. `!setprefix <new_prefix>`:\n"
        "   - Change my command prefix to something other than `!`. Replace `<new_prefix>` with your desired prefix to customize how you interact with me.\n\n"
        "3. `!help`:\n"
        "   - You're using it right now! The `!help` command displays this help message, providing you with information about all available commands.\n\n"
        "Feel free to start a conversation, ask questions, or explore my capabilities. If you ever need assistance or have any other questions, don't hesitate to reach out. Happy chatting!"
    )