# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands
import random

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="$")

@bot.command(name="std")
async def shutdown(ctx):
    id = str(ctx.author.id)
    if id == '707783923844776047':
        await ctx.send('Shutting down the bot!')
        await ctx.bot.logout()
    else:
        await ctx.send("You dont have sufficient permissions to perform this action!")
    
@bot.command(name="ping")
async def ping_da_bot(ctx):
	await ctx.channel.send("pong")

@bot.command(name="bd")
async def bold_da_text(ctx, arg):
	await ctx.channel.send("**" + arg +"**")
	
@bot.command(name="it")
async def italic_da_text(ctx, arg):
	await ctx.channel.send("*" + arg +"*")
	
@bot.command(name="hp")
async def commands(ctx):
	embed = discord.Embed(title = "LazyBot Commands" , description = """```

1. ping
Use to check if bot is active.

2. bd <text>
Prints text in bold.

3. it <text>
Prints text in italics.

4. hp
Shows this menu.

5. hello
Says hello.

6. hru
I'm lazy.

7. f
FFFFFFF.

8. random <num1> <num2>
Chooses a random number between two numbers.

BOT PREFIX ->  $```""", color = 0x00FFFF)
	await ctx.channel.send(embed = embed)

@bot.command(name="hello")
async def hello(ctx):
	await ctx.send(f"Hello Ji, {ctx.author.name}")
	
@bot.command(name="hru")
async def howareyou(ctx):
	await ctx.channel.send("I'm tired af but my owner doesn't let me sleep :pensive:")

@bot.command(name="f")
async def F(ctx):
	await ctx.channel.send("""
FFFFFFFFFFFFFF
FFF
FFF
FFFFFFFFF
FFF
FFF
FFF
FFF""", color = 0x00FFFF)

@bot.command(name="random")
async def randomizer(ctx, num1, num2):
	num1final = int(num1)
	num2final = int(num2)
	embed = discord.Embed(title = f"Random Number Between {num1final} and {num2final}", description = random.randint(num1final, num2final), color = 0x00FFFF)
	await ctx.send(embed = embed)
	
@bot.command(name="coinflip")
async def coinflip(ctx):
	variable = [
	"Heads",
	"Tails"]
	
	embed = discord.Embed(title = "Coinflipper!", description = f"The Coin has flipped on.... {random.choice(variable)}", color = 0x00FFFF)
	await ctx.send(embed = embed)
	
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)