from ast import alias
import discord
import random
import random
from discord.ext import commands

import giphy_client
from giphy_client.rest import ApiException
import random

client = commands.Bot(command_prefix = '^')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('UR MOM'))
    print('We have logged in as {0.user}'.format(client))

@client.command(aliases=['funny?', 'Funny?', 'FUNNY?'])
async def amifunny(ctx):
    await ctx.send('https://tenor.com/view/poki-pokimane-streamer-clap-happy-gif-16214858')

@client.command(aliases=['dev', 'Developer', 'Dev', 'DEV', 'DEVELOPER'])
async def developer(ctx):
    em = discord.Embed(title = 'Developer', description = 'The developer of this bot is Daniel HD')

    await ctx.send(embed = em)

@client.command(aliases=['Gif', 'GIF'])
async def gif(ctx, *,q="Happy"):

    api_key = '38nJS7LJlTSbq0ZyMXwDNqExzzx3OdyV'
    api_instance = giphy_client.DefaultApi()


    try:

        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        await ctx.channel.send(giff.embed_url)


    except ApiException as e:
        print("Exception when calling Api")


@client.command(aliases=['HOTTIE'])
async def hottie(ctx):
    percent = [
        '1% :sunglasses:',
        '2% :sunglasses:',
        '3% :sunglasses:',
        '4% :sunglasses:',
        '5% :sunglasses:',
        '6% :sunglasses:',
        '7% :sunglasses:',
        '8% :sunglasses:',
        '9% :sunglasses:',
        '10% :sunglasses:',
        '11% :sunglasses:',
        '12% :sunglasses:',
        '13% :sunglasses:',
        '14% :sunglasses:',
        '15% :sunglasses:',
        '16% :sunglasses:',
        '17% :sunglasses:',
        '18% :sunglasses:',
        '19% :sunglasses:',
        '20% :sunglasses:',
        '21% :sunglasses:',
        '22% :sunglasses:',
        '23% :sunglasses:',
        '24% :sunglasses:',
        '25% :sunglasses:',
        '26% :smiling_face_with_tear:',
        '27% :smiling_face_with_tear:',
        '28% :smiling_face_with_tear:',
        '29% :smiling_face_with_tear:',
        '30% :smiling_face_with_tear:',
        '31% :smiling_face_with_tear:',
        '32% :smiling_face_with_tear:',
        '33% :smiling_face_with_tear:',
        '34% :smiling_face_with_tear:',
        '35% :smiling_face_with_tear:',
        '36% :smiling_face_with_tear:',
        '37% :smiling_face_with_tear:',
        '38% :smiling_face_with_tear:',
        '39% :smiling_face_with_tear:',
        '40% :smiling_face_with_tear:',
        '41% :smiling_face_with_tear:',
        '42% :smiling_face_with_tear:',
        '43% :smiling_face_with_tear:',
        '44% :smiling_face_with_tear:',
        '45% :smiling_face_with_tear:',
        '46% :smiling_face_with_tear:',
        '47% :smiling_face_with_tear:',
        '48% :smiling_face_with_tear:',
        '49% :smiling_face_with_tear:',
        '50% :smiling_face_with_tear:',
        '51% :cold_face:',
        '52% :cold_face:',
        '53% :cold_face:',
        '54% :cold_face:',
        '55% :cold_face:',
        '56% :cold_face:',
        '57% :cold_face:',
        '58% :cold_face:',
        '59% :cold_face:',
        '60% :cold_face:',
        '61% :cold_face:',
        '62% :cold_face:',
        '63% :cold_face:',
        '64% :cold_face:',
        '65% :cold_face:',
        '66% :cold_face:',
        '67% :cold_face:',
        '68% :cold_face:',
        '69% :hot_face:',
        '70% :hot_face:',
        '71% :hot_face:',
        '72% :hot_face:',
        '73% :hot_face:',
        '74% :hot_face:',
        '75% :hot_face:',
        '76% :hot_face:',
        '77% :hot_face:',
        '78% :hot_face:',
        '79% :hot_face:',
        '80% :hot_face:',
        '81% :hot_face:',
        '82% :hot_face:',
        '83% :hot_face:',
        '84% :hot_face:',
        '85% :hot_face:',
        '86% :hot_face:',
        '87% :hot_face:',
        '88% :hot_face:',
        '89% :hot_face:',
        '90% :hot_face:',
        '91% :hot_face:',
        '92% :hot_face:',
        '93% :hot_face:',
        '94% :hot_face:',
        '95% :hot_face:',
        '96% :hot_face:',
        '97% :hot_face:',
        '98% :hot_face:',
        '99% :hot_face:',
        '100% :hot_face:'
    ]
    em = discord.Embed(title = 'Dank percentage', description = f'You are a {random.choice(percent)} hottie', color = ctx.author.color)
    await ctx.send(embed = em)




@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = 'Help', description = 'Use ^help command to find information on our commands', color = ctx.author.color)

    em.add_field(name = 'Fun', value = 'amifunny, developer, gif, hottie')
    em.add_field(name = 'Moderation', value = 'clear, ')

    await ctx.send(embed = em)



client.run('TOKEN')