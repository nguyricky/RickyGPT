from decouple import config
import responses
import discord

# m = message
# um = user message
# p = private
async def sendMessage(m, um, p):
    try:
        response = responses.grabResponse(um)
        await m.author.send(response) if p else await m.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = config('DISCORD_TOKEN')
    intents = discord.Intents.default()
    
    intents.message_content = True
    
    client = discord.Client(intents = intents)
    
    @client.event
    async def onReady():
        print(f'{client.user} is now running!')
        
    @client.event
    async def onMessage(m):
        if m.author == client.user:
            return
        
        username = str(m.author)
        um = str(m.content)
        channel = str(m.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await sendMessage(m, um, p=True)
        else:
            await sendMessage(m, um, p=False)
    
    client.run(TOKEN)