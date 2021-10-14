import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from discord import TextChannel
from youtube_dl import YoutubeDL
import youtube_dl
import asyncio

players = {}


bot = commands.Bot(command_prefix='==')

@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@bot.command()
async def add(ctx, num1:int, num2:int):
    await ctx.reply(num1+num2)

@bot.command(name= 'join' ,aliases = ['j'])
async def join(ctx):
    connected = ctx.author.voice
    if not connected:
        await ctx.send("You need to be connected in a voice channel to use this command!")
        return
    global vc
    vc = await connected.channel.connect()

@bot.command(name= 'leave' ,aliases = ['l'])
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name= 'play' ,aliases = ['p'])
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
    else:
        await ctx.send("Bot is already playing")
        return

@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')

@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')

@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")





bot.run('ODkwOTc3NzAzNDU1NTEwNTc4.YU3ppg.7AzLDLF2folidoSGpTkzWg6dQk8')
