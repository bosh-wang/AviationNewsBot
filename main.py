from dotenv import load_dotenv
from discord import Intents, Client, Message
import os

from aviation_news import crawl_news, next_news, latest_news

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("!hello"):
        await message.channel.send(
            "Hello this is Aviation News"
        )

    if msg.startswith("!allnews"):
        stories, urls = crawl_news()
        for i in range(len(stories)):
            await message.channel.send(
                f"{stories[i]} - {urls[i]}"
            )
    if msg.startswith("!nextnews"):
        story, url = next_news()
        await message.channel.send(
            f"{story} - {url}"
        )
    if msg.startswith("!latestnews"):
        story, url = latest_news()
        await message.channel.send(
            f"{story} - {url}"
        )

client.run(TOKEN)