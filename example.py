import discord
import time

TOKEN = "NTEzOTQxMjk4MTYwMzM2OTI3.XVI1IA.oXllVWfa5sUxd8-CwsNgCLdKwoM"
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

symbol = "$"
last_message = ""
@client.event
async def on_message(message):
    global last_message
    
    if message.author == client.user:
        return
    
    last_message = message
    
    if message.content[:1] == symbol:
        msg = message.content[1:].split()
        
        if len(msg) > 1 and msg[1] == "help": 
            tags = []
            commands = {
                "load": [[], ["l: length", "s: size"]],
                "msg_me": [[], []],
            }
            
            await message.channel.send(generate_command_helper(msg[0], commands[msg[0]][0], commands[msg[0]][1]))
            return
        
        if msg[0] == "example":
            str1 = "$*command* *param_name1*: *argument1* *param_name2*: *argument2* ... "
            str2 = "Optional parameters are indicated with a tag"
            str3 = "ex: $load l: 10 s: 3000"
            str4 = "ex: $load s: 3000"
            str5 = "Both are valid"
            await message.channel.send(str1 + "\n" + str2 + "\n" + str3 + "\n" + str4 + "\n" + str5)
            return
        
        if msg[0] == "load":
            return
            
        if msg[0] == "test":
            blank = "⠀"
            s = await message.channel.send("```" + blank + "```")
            time.sleep(3)
            
            iter = "·○◯○·"
            for _ in iter:
                time.sleep(0)
                await s.edit(content = "```" + _ + "```")
        
            '''
            num = 10
            y = await message.channel.send(("[" + "-" * num + "]"))
            time.sleep(1)
            for x in range(num):
                time.sleep(0)
                str = "[" + "-" * x + "o" + "-" * (num - x - 1) + "]"
                #print(str)
                await y.edit(content = str)
            '''
            
        if msg[0] == "test2":
            alpha = "bcdefghijklmnopqrstuvwxyz"
            str = await message.channel.send("a")
            for x in alpha:
                time.sleep(1.1)
                await str.edit(content = x)
        
        if msg[0] == "test3":
            #do stuff
            m1 = await message.channel.send("Test")
            r1 = await m1.add_reaction("\U00002705")
            #print(m1.reactions, r1, m1)
            def check(reaction, user):
               return user == message.author and reaction.emoji == "\U00002705" and message == message
            
            t = await client.wait_for('reaction_add', check = check)
            m1 = t[0].message
            print(m1.reactions)
            #await message.remove_reaction("\U00002705", message.author)
            await m1.reactions[0].remove(message.author)
            m1 = await message.channel.send("Hello!")
            
        
        if msg[0] == "msg_me":
            c = await message.author.create_dm()
            await c.send("Hi!")
            return

def generate_command_helper(command, params_m, params_o):
    str = "Command:  "
    str += "'" + command + "'"
    str += "  |  Args:  "
    for x in range(len(params_m)):
        str += params_m[x] + "  "
    for x in range(len(params_o)):
        str += params_o[x] + "  "
    return str
 
client.run(TOKEN)

'''
+----------------------------------------------------------------------------------------+
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
|                                                                                        |
+----------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------+
|        XXX                                                            XXX              |
|      XXX                                                                 XX            |
|    XX                                                                     XX           |
|   X                                                                        X           |
|  X                                                                         XX          |
| X                                                                           X          |
| X                                                                            X         |
|X                                                                             X         |
|X                                                                             X         |
| X                                                                            X         |
| XXX                                                                          X         |
|   XX                                                                         X         |
|     XXXX                                                                    XX         |
|         XXXXX                                                              XX          |
|             XXXXX                                                         XX           |
|                 XXXXXXXXX                                             XXXX             |
|                          XXXXXXXXXXXXXXXXXXX                  XXXXXXXX                 |
|             XXX                            XXXXXXXXXXXXXXXXXXX                         |
|             XXX                                                                        |
+----------------------------------------------------------------------------------------+
'''
