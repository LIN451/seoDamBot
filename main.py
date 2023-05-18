import discord
import random
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Logged")

@client.event
async def on_message(message):
    if message.content.startswith('/주사위'):
        dice = 0
        roll = message.content
        rolld = re.split('[ |d|+]',roll)
        for i in range(1, int(rolld[1])+int(rolld[1])):
            dice = dice + random.randint(1, int(rolld[2]))
        if len(rolld) == 4: 
            dice=dice + int(rolld[3])
        await message.channel.send("결과는 " + str([ dice ]) + " 입니다"  , reference=message)


    if message.content.startswith('!오리'):       
        await message.channel.send('괏괏' , reference=message)

    if message.content.startswith('!매점'):       
        await message.channel.send('뭘 살거냐 괫괫, 콜라, 나나콘, 돌이 있다' , reference=message)
    
    if message.content.startswith('!콜라'):
        await message.channel.send('투ㅔ' , reference=message)

    if message.content.startswith('!돌'):
        await message.channel.send('그걸 왜 먹냐 괫됏' , reference=message)

    if message.content.startswith('!나나콘'):
        await message.channel.send('[나나콘이 부여되었다]')
    
    
    
    

client.run('MTEwNzc0MDM5NTU2OTQzNDYyNA.Gd4ZyS.0UI2YcOiQ5h-duPrpJKEQp84rabelozVy2JGJo')