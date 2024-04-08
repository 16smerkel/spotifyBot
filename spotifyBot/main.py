from nextcord.ext import commands
import nextcord
from config import TOKEN
import os
import wavelink

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is up and ready!")
    bot.loop.create_task(node.connect())

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"Node {node.identifier} is ready!")

async def node_connect():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot, host='lavalinkinc.ml', port=443,password='incognito', https=True)

@bot.command()
async def play(ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    if not ctx.voice_client:
        vc: wavelink.Player = await ctx.author.voice.channel.connect(cLs=wavelink.Player)
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("join a voice channel first")
    else:
        vc: wavelink.Player = ctx.voice_client
    
    await vc.play(search)
    await vc.send("Now playing `{search.title}`")

@bot.command()
async def pause(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send("You are not playing any music")
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("join a voice channel first")
    else:
        vc: wavelink.Player = ctx.voice_client
    
    await vc.pause()
    await ctx.send("music has been paused")

@bot.command()
async def resume(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send("You are not playing any music")
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("join a voice channel first")
    else:
        vc: wavelink.Player = ctx.voice_client
    
    await vc.resume()
    await ctx.send("music has been resumed")

@bot.command()
async def stop(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send("You are not playing any music")
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("join a voice channel first")
    else:
        vc: wavelink.Player = ctx.voice_client
    
    await vc.stop()
    await ctx.send("music has been stopped")

@bot.command()
async def disconnect(ctx: commands.Context):
    if not ctx.voice_client:
        return await ctx.send("You are not playing any music")
    elif not getattr(ctx.author.voice, "channel", None):
        return await ctx.send("join a voice channel first")
    else:
        vc: wavelink.Player = ctx.voice_client
    
    await vc.disconnect()
    await ctx.send("music has been paused")

bot.run(TOKEN)