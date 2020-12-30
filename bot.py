import key
import discord,datetime,aiohttp,pprint,beautifulsoup4
from discord.ext import commands,tasks
TOKEN = key.TOKEN
PREFIX = 'c!'
bot = commands.Bot(command_prefix=PREFIX)




@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def getAPI(ctx):
    now = datetime.datetime.now()
    if now.hour == 10 and now.minute == 0:
        print("10oclock")
        
    async with aiohttp.ClientSession() as session:
        async with session.get('https://kenkoooo.com/atcoder/resources/contests.json') as r:
            if r.status == 200:
                js = await r.json()
                pprint.pprint(js[-1])
                

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def stop(ctx):
    await bot.close()

@bot.command()
async def time(ctx):
    n = datetime.datetime.now()
    #await ctx.send(n)
    await ctx.send(str(n.hour)+":" + str(n.minute))


bot.run(TOKEN)