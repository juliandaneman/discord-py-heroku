import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
    
client = discord.Client()   

@client.event
async def on_message(message):

  capsMess = message.content.upper()
  
  if message.author == client.user:
    return
  
  if capsMess.find('HEY SHITBAG')>0 or capsMess.startswith('HEY SHITBAG'):
    await message.channel.send('FUCK YOU BITCH')
