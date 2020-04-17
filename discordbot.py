from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = commands.Bot(command_prefix='.')
voice_client = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def join(ctx):
    #voicechannelを取得
    vc = ctx.author.voice.channel
    #voicechannelに接続
    await vc.connect()

@client.command()
async def bye(ctx):
    #切断
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass


bot.run(token)
