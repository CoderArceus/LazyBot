import discord
import os
import time
from dotenv import load_dotenv
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.members = True
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()
bot = commands.Bot(command_prefix="$", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$hp"))

@bot.command(name="std")
async def shutdown(ctx):
    id = str(ctx.author.id)
    if id == '707783923844776047':
        await ctx.send('Shutting down the bot!')
        await ctx.bot.logout()
    else:
        await ctx.send("You dont have sufficient permissions to perform this action!")
    
@bot.command(aliases = ['Ping', 'ping'])
async def pinger(ctx):
     embed = discord.Embed(description = f':hourglass: Pong!  {round(bot.latency * 1000)}ms', color = 0x00FFFF)
     await ctx.send(embed = embed)

@bot.command(aliases = ['bold', 'bd', 'Bold'])
async def bold_da_text(ctx, arg):
	await ctx.channel.send("**" + arg +"**")
	
@bot.command(aliases = ['italic', 'it', 'Italic'])
async def italic_da_text(ctx, arg):
	await ctx.channel.send("*" + arg +"*")
	
@bot.command(name="help")
async def commands(ctx):
	embed = discord.Embed(title = "LazyBot Commands" , description = """```
--> <> are required fiels whereas [ ] are optional

1. Ping
Use to check if bot is active.

2. Bold <text>
Prints text in bold.
--> Alias Bd

3. Italic <text>
Prints text in italics.
--> Alias It

4. Help
Shows this menu.

5. Hello [user]
Says hello.

6. Hru
I'm lazy.

7. F
FFFFFFF.

8. Random <num1> <num2>
Chooses a random number between two numbers.

9. Coinflip
Flips a coin.

11. Welcome [user]
Welcomes.

BOT PREFIX ->  $```""", color = 0x00FFFF)
	await ctx.channel.send(embed = embed)

@bot.command(aliases = ['Hello', 'hello'])
async def hello_ji(ctx, user: discord.Member=None):
	if not user:
		await ctx.send(f"Hello Ji, {ctx.author.name}")
		
	else:
		await ctx.send("""

░█─░█ █▀▀ █── █── █▀▀█ 
░█▀▀█ █▀▀ █── █── █──█ 
░█─░█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀
||{}||""".format(user.mention))
	
@bot.command(aliases = ['Hru', 'hru'])
async def howareyou(ctx):
	await ctx.channel.send("I'm tired af but my owner doesn't let me sleep :pensive:")

@bot.command(aliases = ['F', 'f'])
async def F_respects(ctx):
	await ctx.channel.send("""
FFFFFFFFFFFFFF
FFF
FFF
FFFFFFFFF
FFF
FFF
FFF
FFF""")

@bot.command(aliases = ['Random', 'random'])
async def randomizer(ctx, num1, num2):
	num1final = int(num1)
	num2final = int(num2)
	embed = discord.Embed(title = f"Random Number Between {num1final} and {num2final}", description = random.randint(num1final, num2final), color = 0x00FFFF)
	await ctx.send(embed = embed)
	
@bot.command(aliases = ['Coinflip', 'coinflip'])
async def flip_da_coin(ctx):
	variable = [
	"Heads",
	"Tails"]
	
	embed = discord.Embed(title = "Coinflipper!", description = f"The Coin has flipped on.... {random.choice(variable)}", color = 0x00FFFF)
	await ctx.send(embed = embed)
	
@bot.command(aliases = ['Welcome', 'welcome'])
async def welcomer_smol(ctx, user: discord.Member=None):
	if not user:
		await ctx.send("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")
	else:
		await ctx.send("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
||{}||""".format(user.mention))

@bot.event
async def on_member_join(member):
	await bot.get_channel(799616295364198403).send(f"""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

{member.mention} to {member.guild}""")


bot.run(DISCORD_TOKEN)