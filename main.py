from tkinter import BOTH
import discord
from discord.ext import commands,tasks
import youtube_dl
import os

Bot = commands.Bot(command_prefix="!")

@Bot.event
async def on_ready():
    start.start()
    await Bot.change_presence(activity=discord.Game(name='Cs 1.6 oynuyor'))
    print("Ben Hazırım !")


@Bot.command()
async def bruh(ctx):
    for bruh in range(5): # ard arda 5 defa bruh yazar
        await ctx.send("bruh")

@Bot.command()
async def selam(ctx):
    for bruh in range(5):   # Selam yazarsan bunu söyler
        await ctx.send("selam sahip naber")


@tasks.loop(minutes=60)
async def Gulucuk():
    for c in Bot.get_all_channels():   # her 60 dakikaya  bir bunu yazar
        if c.id == 933419503545618503:
            await c.send(':)')

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelenler")
    await channel.send(f"{member} Hoşgeldin..........") # Giren kişiye hoşgeldin der
    print(f"{member} hoşgeldin uzun zamandır seni bekliyordum...")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gidenler")
    await channel.send(f"{member} Gitmee dur ne olursun........")
    print(f"{member}  Gitmee dur ne olursun........")

@Bot.command()
async def komutlar(ctx):   # komutlar
    await ctx.send(
        "Komut Listemiz => selam,bruh,erolegemen,katya,dans,kadimana\n,kadimanaegleniyor,olaylarım,sewgi,roket,katyabebü,iyigeceler\n,oniki,clone,kick,ban,unban,play,pause,resume,leave")


@Bot.command()
async def erolegemen(ctx):
    await ctx.send("KİM ULAN BU EROL EGEMEN \nKİM LAN BU LAVUK ÇIKSIN ORTAYA")  # komik gifler

@Bot.command()
async def katya(ctx):
    await ctx.send("https://c.tenor.com/XRSRZvtKaHwAAAAM/clumsykitty-katya.gif")

@Bot.command()
async def dans(ctx):
    await ctx.send("https://c.tenor.com/3_rmPoHTQdoAAAAd/toqtir-toqtirdans.gif")

@Bot.command()
async def kadimana(ctx):
    await ctx.send("https://pbs.twimg.com/profile_images/1463218359454027787/exnRLpoF_400x400.jpg")

@Bot.command()
async def kadimanaegleniyor(ctx):
    await ctx.send("https://media.tenor.com/images/3a64b660f706ff077f6d02938ca94ad9/tenor.gif")

@Bot.command()
async def olaylarım(ctx):
    await ctx.send("https://media1.tenor.com/images/5d045eae5f3c6d88f646ea5b689ff617/tenor.gif?itemid=25117029")

@Bot.command()
async def sewgi(ctx):
    await ctx.send("https://tenor.com/view/gif-25117018")

@Bot.command()
async def roket(ctx):
    await ctx.send("https://clips-media-assets2.twitch.tv/42106121132-offset-3934-preview-480x272.jpg")

@Bot.command()
async def katyabebü(ctx):
    await ctx.send("https://tenor.com/view/clumsykitty-toqtir-sedat-sakmar-irem-sakmar-kato-gif-22836771") # komik gifler

@Bot.command()
async def iyigeceler(ctx):
        await ctx.send("sana da iyi geceler kardesim")  # iyi geceler mesajı

@Bot.command()
async def oniki(ctx, *args):
    await ctx.send("0000 seviliyorsun... :clock12: :heart:") # 0000 mesajı

@Bot.command(aliases=["copy"])
async def clone(ctx, amount=1):    # channel kopyalama
    for i in range(amount):     
        await ctx.channel.clone()


@Bot.command()
async def kick(ctx, member: discord.Member, *, reason="Yok"): # kickleme
    await member.kick(reason=reason) 


@Bot.command()
async def ban(ctx, member: discord.Member, *, reason="Yok"):  # ban
    await member.ban(reason=reason)


@Bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()  # unban
    member_name, member_discriminator = member.split("#")

    for bans in banned_users:
        user = bans.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Banın Kalktı {user.mention}")
            return

@Bot.command()
async def play(ctx, url : str):  
    song_there = os.path.isfile("song.mp3") # başlatma
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("bekle veya dur komutunu kullan ustam")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='bruh2')
    await voiceChannel.connect()
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@Bot.command()
async def leave(ctx):
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()  # durdurma
    else:
        await ctx.send("botumuz ses kanalından ayrılamıyor... neden")


@Bot.command()
async def pause(ctx):
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()  # pause
    else:
        await ctx.send("şarkı duramıyor ustam")


@Bot.command()
async def resume(ctx):
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():  # sarki devam ettirme
        voice.resume()
    else:
        await ctx.send("Şarkı devam edemiyor ustam ne oldu")


@Bot.command()
async def stop(ctx):  # durdurma
    voice = discord.utils.get(Bot.voice_clients, guild=ctx.guild)
    voice.stop()




Bot.run('buraya tokeni yazın')
