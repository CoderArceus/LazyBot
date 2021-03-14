import discord
import os
import time
import asyncio
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, BadArgument, MissingPermissions
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
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$help"))

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
--> Alias: Bd

3. Italic <text>
Prints text in italics.
--> Alias: It

4. Help
Shows this menu.

5. Hello [user]
Says hello.

6. Hru
I'm lazy.
--> Alias: howareyou

7. F
FFFFFFF.

8. Random <num1> <num2>
Chooses a random number between two numbers.

9. Coinflip
Flips a coin.

11. Welcome [user]
Welcomes.

12. Kick <user>
kicks.

13. Ban <user>
Bans.

14. Purge <amount>
Clears a defined number of Chats.
--> Aliases: Clean, Clear.

15. Tempmute <user>
Temporarily mutes a user.
--> Alias: Tm

16. Unmute <user>
Unmutes a specific user.

BOT PREFIX ->  $```""", color = 0x00FFFF)
	await ctx.channel.send(embed = embed, delete_after=20.0)

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
	if member.guild.id == 799616295364198400:
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
	
	elif member.guild.id == 807527480705548288:
		await bot.get_channel(815473543785480205).send(f"""
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


@bot.command(aliases = ['Kick'])
@has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	embed = discord.Embed(title = f":white_check_mark: {member} has been Kicked!", description = f"Reason: {reason}", color = 0x00FFFF)
	await ctx.send(embed = embed)
  
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(description = f":x: You don't have enough permission to kick members.", color = 0x00FFFF)
        await ctx.send(embed = embed)
    elif isinstance(error, BadArgument):
    	embed = discord.Embed(description = f":x: Couldn't Identify Target.", color = 0x00FFFF)
    	await ctx.channel.send(embed=embed)
    else:
    	raise error

@bot.command(aliases = ['Ban'])
@has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	embed = discord.Embed(title = f":white_check_mark: {member} has been Banned!", description = f"Reason: {reason}", color = 0x00FFFF)
	await ctx.send(embed = embed)
  
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(description = f":x: You don't have enough permission to ban members.", color = 0x00FFFF)
        await ctx.send(embed = embed)
    elif isinstance(error, BadArgument):
    	embed = discord.Embed(description = f":x: Couldn't Identify Target.", color = 0x00FFFF)
    	await ctx.channel.send(embed=embed)
    else:
    	raise error


@bot.command(pass_context=True, aliases = ['purge', 'Purge', 'Clean', 'Clear', 'clear'])
@has_permissions(administrator=True)
async def clean(ctx, limit: int):
        limit = int(limit + 1)
        await ctx.channel.purge(limit=limit)
        limit = int(limit - 1)
        await ctx.send('Cleared {} Chats by {}'.format(limit, ctx.author.mention), delete_after=2.0)
        await ctx.message.delete()

#mute
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0x00FFFF)
        await ctx.channel.send(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x00FFFF)
        await ctx.channel.send(embed=embed)
# /mute

#unmute
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0x00FFFF)
        await ctx.send(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0x00FFFF)
        await ctx.send(embed=embed)
# /unmute

#tempmute
@bot.command(aliases = ['tm', 'Tm', 'TM', 'Tempmute'])
async def tempmute(ctx, member: discord.Member, time0, *, reason=None):
    guild = ctx.guild
    time = time0[:-1]
    time_type = time0[-1:]
    time = int(time)

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)

            embed = discord.Embed(title="Muted!", description=f"{member.mention} has been tempmuted ", colour=0x00FFFF)
            embed.add_field(name="Reason:", value=reason, inline=False)
            embed.add_field(name="Time left for the mute:", value=f"{time0}", inline=False)
            await ctx.send(embed=embed)

            if time_type == "s":
                await asyncio.sleep(time)

            if time_type== "m":
                await asyncio.sleep(time*60)

            if time_type == "h":
                await asyncio.sleep(time*60*60)

            if time_type == "d":
                await asyncio.sleep(time*60*60*24)

            await member.remove_roles(role)

            embed = discord.Embed(title="Unmuted (temp)! ", description=f"Unmuted -{member.mention} ", colour=0x00FFFF)
            await ctx.send(embed=embed)

            return

# / tempmute

bot.run(DISCORD_TOKEN)