import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import time



TOKEN = 'NTU0NzQ5NDIxNzc5MTU3MDI0.D2hKaw.R2FcMBAaDfb7gRA0wmfdZ8fdj-c'

client = commands.Bot(command_prefix = '?')
client.remove_command('help')


#whoiswho Bot   

@client.command()
async def ungay():
    await client.say('<@476907557915459598>')   #timmy

@client.command()
async def blacc():
    await client.say('<@478232173099352064>')   #paper

@client.command()
async def boss():
    await client.say('<@453976758644113410>')   #chris

@client.command()
async def buckangel():
    await client.say('<@309404780650823691>')   #adnan



#reaction Bot

@client.event
async def on_reaction_add(reaction, user):
    channel = discord.Object(id='534097839459008533')
    await client.send_message(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction, user):
    channel = discord.Object(id='534097839459008533')
    await client.send_message(channel, '{} has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))



#role Bot

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Member')
    await client.add_roles(member, role)



#on ready

@client.event
async def on_ready():

    await client.change_presence(game=discord.Game(name='with your mom'))

    print('Bot is ready.')


#?help Embed

@client.command()
async def help():
    embed = discord.Embed(
        title = '**Commands**',
        description = '__Here is a list of commands you can use:__',
        colour = discord.Colour.red()
    )

    embed.set_footer(text = 'Manual Boyz Gang!')
    embed.add_field(name = '!boss', value = 'Tells you who the big boss is', inline = False)
    embed.add_field(name = '!buckangel', value = 'Tells you who Buckangel is', inline = False)
    embed.add_field(name = '!blacc', value = 'Tells you who is blacc', inline = False)
    embed.add_field(name = '!ungay', value = 'Tells you who lost gay status', inline = False)

    await client.say(embed = embed)


client.run('NTU0NzQ5NDIxNzc5MTU3MDI0.D2hKaw.R2FcMBAaDfb7gRA0wmfdZ8fdj-c')
