import asyncio
from asyncio import sleep
from random import randint

import discord
import pymysql as pymysql
from discord import channel
from discord.ext import commands
from pymysql.cursors import DictCursor

from config import settings

dbh = pymysql.connect(
        host='109.120.190.242',
        port=3306,
        user='root',
        password='qBND9KgPur9jAxDwcRrEmReN7y2HBwWFYTYc',
        db='datebaseass',
        charset='utf8mb4',
        cursorclass=DictCursor,
        autocommit=True
    )
cur = dbh.cursor()

bot = commands.Bot(command_prefix=settings['prefix'])






@bot.command(pass_context=True)
async def auth(ctx, email, ):
    member = ctx.message.author
    cur.execute(f"""SELECT Email, Tier, status, Name FROM datebase_with_cute_ass WHERE Email = '{email}';""")
    aboba = cur.fetchone()
    cur.execute(f"""SELECT Email, Tier, status, Name FROM for_discord_bot WHERE Email = '{email}';""")
    aboba1 = cur.fetchone()
    if aboba == None:
        await ctx.send(f"Such mail does not exist in our database. Are you sure you entered it correctly?")
        await asyncio.sleep(10)
        await ctx.channel.delete()
    elif not aboba1:
        query = '''INSERT INTO for_discord_bot( Name, Email, Tier, status) VALUES (%s,%s,%s,%s)'''
        values = aboba['Name'], aboba['Email'], aboba['Tier'], '16'
        cur.execute(query, values)
        await ctx.send(f"Congratulations! You have your role!")
        if aboba['Tier'] == 'Supporter':
            role_1 = member.guild.get_role(626123834919092244)
            await member.add_roles(role_1)
            await asyncio.sleep(10)
            await ctx.channel.delete()
        elif aboba['Tier'] == 'Friend':
            role_3 = member.guild.get_role(626137973918007316)
            await member.add_roles(role_3)
            await asyncio.sleep(10)
            await ctx.channel.delete()
        elif aboba['Tier'] == 'Best friend':
            role_2 = member.guild.get_role(626138204755591248)
            await member.add_roles(role_2)
            await asyncio.sleep(10)
            await ctx.channel.delete()
        elif aboba['Tier'] == 'Super Best Friend':
            role_2 = member.guild.get_role(671433790639439875)
            await member.add_roles(role_2)
            await asyncio.sleep(10)
            await ctx.channel.delete()
        elif aboba['Tier'] == 'School Game is my life!':
            role_2 = member.guild.get_role(671431724684673025)
            await member.add_roles(role_2)
            await asyncio.sleep(10)
            await ctx.channel.delete()

    else:
        await ctx.send(f"A role has already been issued for this email.")
        await asyncio.sleep(10)
        await ctx.channel.delete()


@bot.command()
async def create(ctx):
    guild = bot.get_guild(990986544611491900)

    category = discord.utils.get(guild.categories, name="auth")

    overwrites = {

    }
    channel = await guild.create_text_channel(f'{ctx.message.author}', category=category, overwrites=overwrites)
    await channel.set_permissions(ctx.guild.default_role,
                                  read_messages=False)
    await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)





@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.message.delete()

@bot.command()
async def sos(ctx):
    await ctx.send("To get your role , write !create, and then in the channel created for yourself !auth and your email\n Example: !auth test@outlook.com")
@bot.command()
async def помощь(ctx):
   await ctx.send("Чтобы получить свою роль напиши !create, а после в созданном для себя канале !auth и свою почту\n Пример: !auth test@outlook.com")



bot.run(settings['token'])
