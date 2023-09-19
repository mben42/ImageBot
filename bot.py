import discord
import json
from discord.ext import commands
import random
import os

jfile = open('config.json')
config = json.load(jfile)

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command(aliases = config['commands'])
async def send_image(ctx):
	rep = ctx.invoked_with
	files = os.listdir(rep)
	number = len(files)-1

	rand = random.randint(0, number)

	filename=r'{}/{}'.format(rep, files[rand])
	await ctx.send(config['message'], file=discord.File(filename))

bot.run(config['token'])
