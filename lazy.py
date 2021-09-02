import discord
from discord import User
import os
import time
import asyncio
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, BadArgument, MissingPermissions, Bot, guild_only
import random
import youtube_dl
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import json
import inspect
import io
import textwrap
import traceback
import aiohttp
from contextlib import redirect_stdout
import base64


intents = discord.Intents.default()
intents.members = True
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()
bot = commands.Bot(command_prefix=";", intents=intents)
bot.remove_command("help")

players = {}

# start


@bot.event  # check if bot is ready
async def on_ready():
    print('Bot online')
# /start

# onready


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=";help"))
# /onready

# shutdown


@bot.command(name="std")
async def shutdown(ctx):
    id = str(ctx.author.id)
    if id == '707783923844776047':
        await ctx.send('Shutting down the bot!')
        await ctx.bot.logout()
    else:
        await ctx.send("You dont have sufficient permissions to perform this action!")
# /shutdown

# ping


@bot.command(aliases=['Ping', 'ping'])
async def pinger(ctx):
    embed = discord.Embed(
        description=f':hourglass: Pong!  {round(bot.latency * 1000)}ms', color=0x00FFFF)
    await ctx.send(embed=embed)
# /ping

# bold


@bot.command(aliases=['bold', 'bd', 'Bold'])
async def bold_da_text(ctx, arg):
    await ctx.channel.send("**" + arg + "**")
# /bold

# italic


@bot.command(aliases=['italic', 'it', 'Italic'])
async def italic_da_text(ctx, arg):
    await ctx.channel.send("*" + arg + "*")
# /italic

# help


@bot.command(name="help")
async def commands(ctx):
    embed = discord.Embed(title="LazyBot Commands", description="""```
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

17. Avatar [user]
Displays user's avatar.
--> Alias: Av

BOT PREFIX ->  ;```""", color=0x00FFFF)
    await ctx.channel.send(embed=embed)
# /help

# hello


@bot.command(aliases=['Hello'])
async def hello(ctx, mention=None):
    if mention == None:
        await ctx.send(f"""Hello! {ctx.author.name} 
https://cdn.discordapp.com/attachments/766663041735196705/820997741269876766/tumblr_nt2axxI1no1tydz8to1_500.gif""")

    else:
        await ctx.send("""https://cdn.discordapp.com/attachments/766663041735196705/820997741269876766/tumblr_nt2axxI1no1tydz8to1_500.gif
||{}||""".format(mention))
# /hello

# hru


@bot.command(aliases=['Hru', 'hru'])
async def howareyou(ctx):
    await ctx.channel.send("I'm tired af but my owner doesn't let me sleep :pensive:")
# /hru

# F


@bot.command(aliases=['F', 'f'])
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
# /F

# random


@bot.command(aliases=['Random', 'random'])
async def randomizer(ctx, num1, num2):
    num1final = int(num1)
    num2final = int(num2)
    embed = discord.Embed(title=f"Random Number Between {num1final} and {num2final}", description=random.randint(
        num1final, num2final), color=0x00FFFF)
    await ctx.send(embed=embed)
# /random

# coinflip


@bot.command(aliases=['Coinflip', 'coinflip'])
async def flip_da_coin(ctx):
    variable = [
        "Heads",
        "Tails"]

    embed = discord.Embed(
        title="Coinflipper!", description=f"The Coin has flipped on.... {random.choice(variable)}", color=0x00FFFF)
    await ctx.send(embed=embed)
# /coinflip

# welcomer


@bot.command(aliases=['Welcome', 'welcome'])
async def welcomer_smol(ctx, user: discord.Member = None):
    if not user:
        await ctx.send("https://cdn.discordapp.com/attachments/784278783057854485/820594071567335434/welccome1.gif")
    else:
        await ctx.send("""||{}||
https://cdn.discordapp.com/attachments/784278783057854485/820594071567335434/welccome1.gif""".format(user.mention))


@bot.event
async def on_member_join(member):
    if member.guild.id == 799616295364198400:
        await bot.get_channel(799616295364198403).send(f"""Welcome {member.mention} to {member.guild}
https://cdn.discordapp.com/attachments/784278783057854485/820594071567335434/welccome1.gif""")

    elif member.guild.id == 807527480705548288:
        await bot.get_channel(815473543785480205).send(f"""Welcome {member.mention} to {member.guild}
https://cdn.discordapp.com/attachments/784278783057854485/820594071567335434/welccome1.gif""")
# /welcomer

# kick


@bot.command(aliases=['Kick'])
@has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
        title=f":white_check_mark: {member} has been Kicked!", description=f"Reason: {reason}", color=0x00FFFF)
    await ctx.send(embed=embed)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(
            description=f":x: You don't have enough permission to kick members.", color=0x00FFFF)
        await ctx.send(embed=embed)
    elif isinstance(error, BadArgument):
        embed = discord.Embed(
            description=f":x: Couldn't Identify Target.", color=0x00FFFF)
        await ctx.channel.send(embed=embed)
    else:
        raise error
# /kick

# ban


@bot.command(aliases=['Ban'])
@has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
        title=f":white_check_mark: {member} has been Banned!", description=f"Reason: {reason}", color=0x00FFFF)
    await ctx.send(embed=embed)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(
            description=f":x: You don't have enough permission to ban members.", color=0x00FFFF)
        await ctx.send(embed=embed)
    elif isinstance(error, BadArgument):
        embed = discord.Embed(
            description=f":x: Couldn't Identify Target.", color=0x00FFFF)
        await ctx.channel.send(embed=embed)
    else:
        raise error
# /ban

# purge


@bot.command(pass_context=True, aliases=['purge', 'Purge', 'Clean', 'Clear', 'clear'])
@has_permissions(administrator=True)
async def clean(ctx, limit: int):
    limit = int(limit + 1)
    await ctx.channel.purge(limit=limit)
    limit = int(limit - 1)
    await ctx.send('Cleared {} Chats by {}'.format(limit, ctx.author.mention), delete_after=2.0)
    await ctx.message.delete()
# /purge

# mute


@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(role)
        embed = discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(
            member, ctx.message.author), color=0x00FFFF)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.",
                              description="You don't have permission to use this command.", color=0x00FFFF)
        await ctx.channel.send(embed=embed)
# /mute

# unmute


@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.administrator:
        role = discord.utils.get(member.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed = discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(
            member, ctx.message.author), color=0x00FFFF)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Permission Denied.",
                              description="You don't have permission to use this command.", color=0x00FFFF)
        await ctx.send(embed=embed)
# /unmute

# tempmute


@bot.command(aliases=['tm', 'Tm', 'TM', 'Tempmute'])
async def tempmute(ctx, member: discord.Member, time0, *, reason=None):
    guild = ctx.guild
    time = time0[:-1]
    time_type = time0[-1:]
    time = int(time)

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)

            embed = discord.Embed(
                title="Muted!", description=f"{member.mention} has been tempmuted ", colour=0x00FFFF)
            embed.add_field(name="Reason:", value=reason, inline=False)
            embed.add_field(name="Time left for the mute:",
                            value=f"{time0}", inline=False)
            await ctx.send(embed=embed)

            if time_type == "s":
                await asyncio.sleep(time)

            if time_type == "m":
                await asyncio.sleep(time*60)

            if time_type == "h":
                await asyncio.sleep(time*60*60)

            if time_type == "d":
                await asyncio.sleep(time*60*60*24)

            await member.remove_roles(role)

            embed = discord.Embed(
                title="Unmuted (temp)! ", description=f"Unmuted -{member.mention} ", colour=0x00FFFF)
            await ctx.send(embed=embed)

            return
# / tempmute

# unban


@bot.command(pass_context=True)
@has_permissions(administrator=True)
@guild_only()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    embed = discord.Embed(
        title="Unbanned!", description=f"{user.name} has been unbanned.", color=0x00FFFF)
    await ctx.send(embed=embed)


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, CheckFailure):
        embed = discord.Embed(
            description=f":x: You don't have enough permission to unban members.", color=0x00FFFF)
        await ctx.send(embed=embed)
    elif isinstance(error, BadArgument):
        embed = discord.Embed(
            description=f":x: Couldn't Identify Target.", color=0x00FFFF)
        await ctx.channel.send(embed=embed)
    else:
        raise error
# /unban

# avatar


@bot.command(pass_context=True, aliases=['Avatar', 'Av', 'av'])
async def avatar(ctx, user: discord.Member = None):
    if user == None:
        author = ctx.message.author
        embed = discord.Embed(title=ctx.message.author.name, color=0x00FFFF)
        embed.set_image(url=author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=user.name, color=0x00FFFF)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)
# /avatar

# warn


@bot.command(aliases=['Warn'])
@has_permissions(administrator=True)
async def warn(ctx, user: discord.Member, *, reason=None):
    if reason == "None":
        f = open("warns.txt", "a")
        embed = discord.Embed(title={user}, description="None")
        await f.append(embed=embed)
        await ctx.send(embed=embed)
    else:
        f = open("warns.txt", "a")
        embed = discord.Embed(title={user}, description={reason})
        await f.append(embed=embed)
        await ctx.send(embed=embed)
# /warn


@bot.command(aliases=['Rules'])
@has_permissions(administrator=True)
async def rules(ctx):
    embed = discord.Embed(title='Rules', description='''#1:  No spamming(5+ lines). If you spam once you will be warned but after this warn the moderators can mute you immediately for a day.
- Copypasta is also prohibited.

#2: No interfering with moderator's duties, don't argue with them while they are actively moderate, and don't troll with fake evidence.

#3: Do not be racist. We don't care if you say "nigga" etc. Just don't use it offensively.

#4: Advertising or Self-Promotion isn't allowed anywhere(only managers+ can).

#5: NSFW (Not Safe For Work) Content and Media are not permitted inside chatrooms. Following the Discord TOS, NSFW avatars are also not allowed.

#6: Punishment evasion(bypass a punishment given to your main account) is not allowed. Any bypassing of rules of any kind is not permitted and will lead to serious actions.

#7: Ghostpinging (Tag and delete) is a serious offense and you can be muted without warning.

#8: Don't send any NSFW content and don't do dm ad, or u will get ban. 

#9: Use Introduction Channel wisely and no chatting is allowed there.

#10: No abusing offensively is allowed.

#11: Use the channels for their correct use. 
- <#799624713214492732> is used for bot commands ONLY.
- Keep <#799616295364198403>  is for general discussions(No bot command).

Punishment System:
3 warnings - Mute.
6 warnings - Kick.
15 warnings- Ban.

Moderators have the right to skip to a suspension or a ban, depending on the offense.
If you would like to report someone, please DM any staff members''', color=0x00FFFF)
    await ctx.send(embed=embed)

# MUSIC

# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


# command to play sound from a youtube URL
@bot.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return

# command to resume voice if it is paused


@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


# command to pause voice if it is playing
@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


# command to stop voice
@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

# /MUSIC

# Eval Code


@bot.command(name='eval')
async def _eval(ctx, *, body):
    if ctx.author.id == 477758607857942529:
        """Evaluates python code"""
        env = {
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            'source': inspect.getsource,
            'bot': bot
        }

        env.update(globals())

        body = cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        def paginate(text: str):
            '''Simple generator that paginates text.'''
            last = 0
            pages = []
            for curr in range(0, len(text)):
                if curr % 1980 == 0:
                    pages.append(text[last:curr])
                    last = curr
                    appd_index = curr
            if appd_index != len(text)-1:
                pages.append(text[last:curr])
            return list(filter(lambda a: a != '', pages))

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.reply(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await ctx.message.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.reply(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                        out = await ctx.reply(f'```py\n{value}\n```')
                    except:
                        paginated_text = paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.reply(f'```py\n{page}\n```')
                                break
                            await ctx.reply(f'```py\n{page}\n```')
            else:
                bot._last_result = ret
                try:
                    out = await ctx.reply(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.reply(f'```py\n{page}\n```')
                            break
                        await ctx.reply(f'```py\n{page}\n```')

        if out:
            await ctx.message.add_reaction('\u2705')  # tick
        elif err:
            await ctx.message.add_reaction('\u2049')  # !?
        else:
            await ctx.message.add_reaction('\u2705')
    else:
        await ctx.message.add_reaction('❌')  # x


def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')


def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'


#ping spam
@bot.command()
async def spam(ctx, times: int, *, mention):
    for i in range(0, times):
        await ctx.send(mention)
# /ping spam

bot.run(DISCORD_TOKEN)

