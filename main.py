import discord
import os
import search_runpee
from dotenv import load_dotenv

# Use python-dotenv pakcage to get variables stored in .env file of your project
load_dotenv()

client = discord.Client()

hello_message = '''Hello there! I\'m the fidgeting bot from RunPee. Sorry but I really need to go to the bathroom... 
Please read my manual by typing $help or $commands while I\'m away.'''

no_result_message = '''Sorry, we can\'t find what you are searching for.'''

# instantiate RunPeeWeb class from search_runpee.py
runpee_web = search_runpee.RunPeeWeb()

@client.event
async def on_ready():
  print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  
  if message.content.startswith(f'$hello'):
    await message.channel.send(hello_message)
  
  if f'$search' in message_content:

    key_words, search_words = runpee_web.key_words_search_words(message_content)
    result_links = runpee_web.search(key_words)
    links = runpee_web.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)


client.run(TOKEN)