import discord
from discord.ext import commands
import secreto
import os

''' VARIAVEIS'''

bot = commands.Bot(command_prefix='?', description='Bem vindos Ao discord.')
client = discord.Client()
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token
token = secreto.token
user = discord.Member
''' EVENTOS DO BOT'''
#MOSTRA NO TERMINAL ONDE TA LOGADO E MUDA STATUS DO BOT
@bot.event
async def on_ready():
    print('Logado em')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    return await bot.change_presence(game=discord.Game(name='Programando'))




#ENVIA UMA MENSAGEM PRIVADA AO ENTRAR NO SERVER
@bot.event
async def on_member_join(member):
    await bot.send_message(member,
                           'Bem Vindo ao ' + member.server.name + ' ' + member.mention + '\n Estou aqui para ajudar ,digite ?help para ver so comandos .')

    await bot.add_roles(member)

#MOSTRA UM GIF AO BANIR USUSARIO
@client.event
async def on_member_ban(user):
    channel = discord.utils.find(lambda c: c.name == 'banimentos', user.server.channels)
    embed = discord.Embed(title='Sinta o martelo!', description='Algum staff baniu o membro **@{0.name}** do servidor!\n\nO martelo deve ter doído :0'.format(user), color=0xff9d00)
    embed.set_image(url='https://i.imgur.com/O3DHIA5.gif')
    embed.set_thumbnail(url=user.avatar_url)
    await client.send_message(channel, embed=embed)






''' COMANDOS DO BOT'''

#MOSTRA INFORMAÇOES DO USUARIO
@bot.command(pass_context=True)
async def myinfo(ctx):
    user = ctx.message.author
    embedusu = discord.Embed(title="Suas info", color=0xeee657)
    embedusu.set_thumbnail(url=user.avatar_url)
    embedusu.add_field(name="Seu Nome", value=user.name)
    embedusu.add_field(name="Seu Id", value=user.id)
    embedusu.add_field(name="Status", value=user.status)
    embedusu.add_field(name="Entrou no serve em", value=user.joined_at)

    await bot.say(embed=embedusu)


#COMANDO PING PONG *SEM MOSTRAR MS
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")


#MOSTRA MENSAGEM DE BOAS VINDAS
@bot.command()
async def python():
     await bot.say("Python é uma linguagem de programação criada por Guido van Rossum em 1991.\n Os objetivos do projeto da linguagem eram: produtividade e legibilidade.\n Em outras palavras, Python é uma linguagem que foi criada para produzir código bom e fácil de manter de maneira rápida.")


#MOSTRA INFORMAÇÕES DO SERVIDOR
@bot.command()
async def info():
    embedin = discord.Embed(title="Olá sou pythozinho", description="convite e membros online.", color=0xeee657)
    embedin.add_field(name="Author", value="Vagner")
    embedin.add_field(name="Server count", value=f"{(len(bot.servers))}")
    embedin.add_field(name="Invite", value="https://discord.gg/vSFN3Zx")

    await bot.say(embed=embedin)



#ENVIA UM GATINHO EM GIF
@bot.command()
async def cat():
    await bot.say("https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif")


#EXIBE OS COMANDOS DO BOT
bot.remove_command('help')
@bot.command()
async def help():
    embedhelp = discord.Embed(title="Pythozinho", description="Olá eu fui criado em python, abaixo segue minha lista de comandos:", color=0xeee657)
    embedhelp.add_field(name="?python", value="Sobre o python", inline=False)
    embedhelp.add_field(name="?cat", value="Gatinho gif :3", inline=False)
    embedhelp.add_field(name="?info", value="Informaçoes", inline=False)
    embedhelp.add_field(name="?help", value="Ajuda", inline=False)
    embedhelp.add_field(name="?myinfo", value="Mostra suas informações", inline=False)

    await bot.say(embed=embedhelp)






'''TOKEN PARA RODAR BOT'''
bot.run(token)

