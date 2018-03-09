import discord
from discord.ext import commands
import os
import time
import random

''' VARIAVEIS'''

bot = commands.Bot(command_prefix='?', description='Bem vindos Ao discord.')
client = discord.Client()
is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
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


''' COMANDOS DO BOT'''
#ROLA O DADO
@bot.command(pass_context=True, aliases=['dice'])
async def dado(ctx):
    choice  = random.randint(1,6)
    embeddad = discord.Embed(title = 'Dado', description = ' Joguei o dado, o resultado é :   {}'.format(choice), colour = 0x1abc9c)
    await bot.say(embed=embeddad)

#JOGA A MOEDA
@bot.command(pass_context=True, aliases=['coin'])
async def moeda(ctx):
    Coin = ["É CARA!", "É COROA!"]
    choice = random.choice(Coin)
    embedcon = discord.Embed(title='Moeda', description=choice, colour=0x1abc9c)
    await bot.say(embed=embedcon)

#ENVIA UM VIDEO ALEATORIO DO MEU CANAL
@bot.command(pass_context=True)
async def music(ctx):
    song = ['https://www.youtube.com/watch?v=XzK7nCUCHEA', 'https://www.youtube.com/watch?v=G684IQwqodM', 'https://www.youtube.com/watch?v=uukforYWCkk', 'https://www.youtube.com/watch?v=3_29xfehVgY']
    choice  = random.choice(song)
    await bot.say('{}, Aqui está sua musica aleátoria.\n'.format(ctx.message.author.name) + choice)


#GERA CONVITE
@bot.command(pass_context=True)
async def convite(context):
	invite = await bot.create_invite(context.message.server,max_uses=1,xkcd=True)
	await bot.send_message(context.message.author,"Seu convite é {}".format(invite.url))

#DELETA MENSAGENS
@bot.command(pass_context=True)
async def delete(context, number : int):
	deleted = await bot.purge_from(context.message.channel, limit=number)
	await bot.send_message(context.message.channel, 'Deletado {} message(s)'.format(len(deleted)))

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


#COMANDO PING PONG 
@bot.command(aliases=['p'])
async def ping():
    pingtime = time.time()
    e = discord.Embed(title = 'Ok espere', color = 0x1abc9c)
    pingus = await bot.say(embed=e)
    ping = time.time() - pingtime
    ping1 = discord.Embed(title = 'Pong!', description = ':ping_pong: Ping time - `%.01f seconds`' % ping, colour = 0x1abc9c)
    await bot.edit_message(pingus, embed=ping1)


#FALA SOBRE O PYTHON
@bot.command()
async def python():
     await bot.say("Python é uma linguagem de programação criada por Guido van Rossum em 1991.\n Os objetivos do projeto da linguagem eram: produtividade e legibilidade.\n Em outras palavras, Python é uma linguagem que foi criada para produzir código bom e fácil de manter de maneira rápida.")

#FALA SOBRE O JAVA
@bot.command()
async def java():
     await bot.say("é uma linguagem de programação e plataforma computacional lançada pela primeira vez pela Sun Microsystems em 1995.\n Existem muitas aplicações e sites que não funcionarão, a menos que você tenha o Java instalado, e mais desses são criados todos os dias..")


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
    embedhelp.add_field(name="?java", value="Sobre o java", inline=False)
    embedhelp.add_field(name="?cat", value="Gatinho gif :3", inline=False)
    embedhelp.add_field(name="?info", value="Informaçoes", inline=False)
    embedhelp.add_field(name="?help", value="Ajuda", inline=False)
    embedhelp.add_field(name="?music", value="Mostra um video aleátorio do meu canal/ obs: da like", inline=False)
    embedhelp.add_field(name="?moeda", value="Joga uma moeda", inline=False)
    embedhelp.add_field(name="?ping", value="Mostra o tempo de resposta entre o bot e o servirdor", inline=False)
    embedhelp.add_field(name="?dado", value="Rola um dado de 6 lados", inline=False)
    embedhelp.add_field(name="?convite", value="Envia o convite do serve no seu privado", inline=False)
    embedhelp.add_field(name="?delete", value="Deleta mensagem passando a quantidade", inline=False)
    embedhelp.add_field(name="?myinfo", value="Mostra suas informações", inline=False)

    await bot.say(embed=embedhelp)






'''TOKEN PARA RODAR BOT'''
bot.run(token)

