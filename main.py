import discord


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  capsMess = message.content.upper()
  
  if message.author == client.user:
    return
  
  if capsMess.find('HEY SHITBAG')>0 or capsMess.startswith('HEY SHITBAG'):
    await message.channel.send('FUCK YOU BITCH')

  if capsMess.find('SUMMON THE PEDOS')>0 or capsMess.startswith('SUMMON THE PEDOS'):
    await message.channel.send('<@937827232062263396>')

  if capsMess.find('GET IN')>0 or capsMess.startswith('GET IN'):
    await connect()

async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()

  
client.run('OTUxNjgzNDkwMzg5MzIzNzg2.YirCUQ.AKOL8J0gliTcBKmhEWi-w3cBCU4')
