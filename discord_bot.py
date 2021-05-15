import discord
from pytube import YouTube
from datetime import date

client = discord.Client()


@client.event
async def on_ready():
    print("Bot ID: " + str(client.user.id) + " - Online - (" +
          client.user.name + ")")
    await client.change_presence(activity=discord.Game(name="Minecraft"))
    

@client.event
async def on_message(message):
    if not message.guild and message.author != client.user and message.content.startswith(''):
        # Ignora mensagens de servidores e a propria mensagem.

        msg = message.content
        hoje = date.today()
        msgrecebida = ("\n Mensagem recebida: " + message.content + " de: " +
                       message.author.display_name + " - " +
                       str(message.author.id) + " " + str(hoje))

        archive = open("videos_solicitados.txt", "a")
        archive.write(msgrecebida)
        print(msgrecebida)


        video = YouTube(msg)

        stream = video.streams.get_highest_resolution()
        stream.download()

        if int(stream.filesize / 1024 / 1024) >= 8:
                await message.channel.send('O video possui mais de 8 MB')

        else:
                await message.channel.send(file=discord.File(stream.download()))

client.run('TOKEN', bot=True)

