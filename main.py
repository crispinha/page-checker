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
    await getter.set_initial_hash()
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("c!ping"):
        await client.send_message(client.get_channel(config.channel_id), "Pong!")
    elif message.content.startswith("c!site"):
        await client.send_message(client.get_channel(config.channel_id), "The current website is {}.".format(config.site))
    elif message.content.startswith("c!check"):
        if getter.has_hash_changed():
            words = "Your website at {} has updated!".format(config.site)
        else:
            words = "No change. :("
        await client.send_message(client.get_channel(config.channel_id), words)


async def do_site_check():
    await client.wait_until_ready()
    while not client.is_closed:
        if await getter.has_hash_changed():
            await client.send_message(client.get_channel(config.channel_id),  "Your website at {} has updated!".format(config.site))
        await asyncio.sleep(60 * config.time_between_tries)


client.loop.create_task(do_site_check())
client.run(config.very_secret_key)
