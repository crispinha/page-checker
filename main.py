import getter
import discord
import asyncio
import config

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    getter.set_initial_hash()
    print('------')
    
@client.event
async def on_message(message):
    if message.content.startswith("c!ping"):
        await client.send_message(client.get_channel("367920715116183554"), "Pong!")
    elif message.content.startswith("c!check"):
        print("Checking")
        if getter.has_hash_changed():
            words = "Your website at {} has updated!".format(config.site)
        else:
            words = "No change. :("
        await client.send_message(client.get_channel("367920715116183554"), words)


client.run(config.very_secret_key)
