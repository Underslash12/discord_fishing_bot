import discord
import time
from game import Game
from bot_token import t as botToken

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

db_a = {}
db_m = {}
symbol = "$"
@client.event
async def on_message(message):
    global db_a
    global db_m
    
    # if message.author == client.user:
        # return
    
    if message.content[:1] == symbol:
        msg = message.content[1:].split()
        
        if msg[0] == "play":
            m = await message.channel.send("Setup")
            
            m_id = m.id
            a_id = message.author.id
            
            try:
                db_a[a_id]
            except KeyError:
                db_a[a_id] = Game(message.author, m_id)
                db_m[m_id] = db_a[a_id]
            else:
                db_a[a_id].update_game_id(m_id)
                db_m[m_id] = db_a[a_id]
            
        if msg[0] == "edit":
            x = await message.channel.fetch_message(db_a[message.author.id].game_id)
            await x.edit(content = "Hello")
            
        if msg[0] == "print":
            print(msg)
            
        if msg[0] == "test":
            x = await message.channel.fetch_message(msg[1])
            await x.add_reaction('⚙')
            
        if msg[0] == "do":
            await message.channel.send(message.content[len(msg[0]) + 2:])
            
@client.event
async def on_reaction_add(reaction, user):
    global db_a
    global db_m
    
    # print("Reaction")
    
    used_reaction_ids = ['🎣', 'ℹ', '⚙']
    
    try:
        db_m[reaction.message.id]
    except KeyError:
        return
  
    try:
        db_a[user.id]
    except KeyError:
        await reaction.remove(user)
        return
    
    if (reaction.emoji not in used_reaction_ids) or (db_a[user.id].game_id != reaction.message.id):
        await reaction.remove(user)
        return
        
    # print("Working")

client.run(botToken)

