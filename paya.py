import discord
import json
from discord.ext import commands
import random
import os

jfile = open('config.json')
config = json.load(jfile)

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command(aliases = config['aliases'])
async def send_image(ctx):
	files = os.listdir(config['repertory'])
	number = len(files)-1

	rand = random.randint(0, number)

	filename=r'{}/{}'.format(config['repertory'], files[rand])
	await ctx.send(config['message'], file=discord.File(filename))

bot.run(config['token'])
