from asyncio import sleep
from random import randint

import discord
import pymysql as pymysql
from discord import channel
from discord.ext import commands
from pymysql.cursors import DictCursor

from config import settings

dbh = pymysql.connect(
    host='',
    port=123123,
    user='guests',
    password='*****',
    db='datebaseass',
    charset='utf8mb4',
    cursorclass=DictCursor
)
cur = dbh.cursor()

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command(pass_context=True)
async def auth(ctx, email, ):
    member = ctx.message.author
    cur.execute(f'''SELECT Tier FROM datebase_with_cute_ass WHERE Email = '{email}';''')
    aboba = cur.fetchone()
    if aboba == {'Tier': 'Supporter'}:
        role_1 = member.guild.get_role(990005388034342963)
        await member.add_roles(role_1)
    elif aboba == {'Tier': 'Best friend'}:
        role_2 = member.guild.get_role(990005345793490954)
        await member.add_roles(role_2)
    elif aboba == {'Tier': 'Friend'}:
        role_3 = member.guild.get_role(990005392845189170)
        await member.add_roles(role_3)
    await ctx.channel.delete()


@bot.command()
async def create(ctx):
    guild = bot.get_guild(990002053340340234)

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


bot.run(settings['token'])
