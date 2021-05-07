import discord
import asyncio
import random

client = discord.Client()

token = "NTQwNzc4NDAzMDMzMzgyOTIy.DzV2xw.MZNDfDqLDLa6DgopA-ksWSS2HtM"

@client.event
async def on_ready():

    print(client.user.name)
    print("성공적으로 봇이 시작되었습니다.")
    game = discord.Game("noobisnoob.kro.kr 마크")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content == "*help":
        await message.channel.send("준비중")

    if message.content == "예하":
        await message.channel.send("예하!")

    if message.content == "embed":
        embed = discord.Embed(title="아맞다", description="음", color=0x00ff00)
        embed.add_field(name="음?", value="읔", inline=True)
        embed.add_field(name="음?", value="읔", inline=True)
        embed.set_footer(text="음!")
        await message.channel.send(embed=embed)

    if message.content == "뽑기":
        ran = random.randint(0,1)
        if ran == 0:
            msg = "꽝"
        if ran == 1:
            msg = "당첨"
        await message.channel.send(msg)

client.run(token)