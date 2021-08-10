#FenialX Beta 4.1
#Copyright 2021

import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ':')
@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, 
    activity=discord.Activity(type=discord.ActivityType.listening, name=":help"))
	print('The bot is running under {0.user}'.format(client))

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send('Successfully kicked the user.')
	
@client.command()
async def ping(ctx):
	await ctx.send(f' :ping_pong: Pong! {round(client.latency * 1000)}ms')
	
@client.command()
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit=amount)

	

client.run(os.environ['DISCORD_TOKEN'])
