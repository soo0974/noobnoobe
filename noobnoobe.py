import discord
import os
import asyncio
import random

client = discord.Client()

token = "NTQwNzc4NDAzMDMzMzgyOTIy.XFPlIg.a3j2cG-3AXHskTGl2ZqCcTcLhkY"

@client.event
async def on_ready():

    print(client.user.name)
    print("성공적으로 봇이 시작되었습니다.")
    game = discord.Game("noobisnoob.kro.kr 에서 마크")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "예하":
        await message.channel.send("예하!")
        
    if message.content == "적끈":
        await message.channel.send("적끈")

    if message.content == "고자":
        await message.channel.send(file=discord.File("simyoung.jpg"))

    if message.content == "도움":
        embed = discord.Embed(title="Commands", description="명령어", color=0x00ff00)
        embed.add_field(name="예하", value="예하", inline=True)
        embed.add_field(name="뽑기", value="1%로 당첨!", inline=True)
        embed.set_footer(text="더 있는데 기억 안남")
        await message.channel.send(embed=embed)

    if message.content == "뽑기":
        ran = random.randint(0,99)
        if ran == 0:
            msg = "당첨"
        else:
            msg = "꽝"
        await message.channel.send(msg)

client.run(token)