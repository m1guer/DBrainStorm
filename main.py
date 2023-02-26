import os
import discord
from discord import file, message as message
from OpenaiDbrain.openapi import OpenAI
from OpenaiDbrain.imagine import Imagine
intents = discord.Intents.default()
intents.message_content = True
token = str(os.getenv("DISCORD_API_TOKEN"))

class DBrainStormain(discord.Client):
    async def on_message(self, message):
        if message.content.startswith("!pt"):
            openai = OpenAI()
            discord_prompt = message.content[4:]
            response = openai.start_prompt(prompt=discord_prompt)
            print(response)
            await message.channel.send(response)
        if message.content.startswith("!im"):
            imagine = Imagine()
            imagine_discord_prompt = message.content[4:]
            img = imagine.start_imagine(prompt=imagine_discord_prompt)
            with open(f"{imagine_discord_prompt}.jpg","rb") as generated_image:
                send_image = discord.File(generated_image)
                await message.channel.send(file=send_image)
                
client = DBrainStormain(intents=intents)
client.run(token)
