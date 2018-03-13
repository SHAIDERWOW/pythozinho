import discord
from discord.ext import commands
import os
import time
import random
import re
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
    return await bot.change_presence(game=discord.Game(name='Pedra na lua'))




#ENVIA UMA MENSAGEM PRIVADA AO ENTRAR NO SERVER
@bot.event
async def on_member_join(member):
    await bot.send_message(member,
                           'Bem Vindo ao ' + member.server.name + ' ' + member.mention + '\n Estou aqui para ajudar ,digite ?help para ver so comandos .')

    await bot.add_roles(member)


''' COMANDOS DO BOT'''
#INFO DO BOT
@bot.command(pass_context=True)
async def botinfo():
  embedbotin = discord.Embed(title="Olá sou pythozinho", description="Basic bot discord.", color=0xeee657)
  embedbotin.set_thumbnail(url=bot.user.default_avatar_url)
  embedbotin.add_field(name='GitHub',value='https://github.com/vagner2k18/pythozinho')
  embedbotin.add_field(name='Me adcione no seu server',value='goo.gl/q9hKzS')
  embedbotin.add_field(name='estou online em',value='--> '+(str(len(bot.servers)))+ ' <--Serve(s)')
  await bot.say(embed=embedbotin)

#KIKA UM MEMBRO DO SERVE
@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.kick_members :
        await bot.say("Kikado!")
        await bot.kick(member)
    else:
        embed = discord.Embed(title=":x: Erro na permissão!", description=" \n ", color=0xff0000)
        embed.add_field(name="Voce nao possui perrmissão para esse comando procure um administrador.".format(
            ctx.message.author.name), value='_Membro kikado_', inline=False)
        embed.set_thumbnail(url=member.avatar_url)

        await bot.say(embed=embed)

#REPETE O FOI DITO
@bot.command(pass_context=True)
async def diz(self, *, msg: str):
        msg = re.sub('´', '`', msg)
        await self.bot.say(msg)

#GERA EMBED COM PARAMTRO TEXTO E SUA FOTO
@bot.command(pass_context=True)
async def eco(ctx, *, phrase):
    try:
        embed3 = discord.Embed(title="Eco", description=" \n ", color=0x0000ff)
        embed3.add_field(name="{} Falou...".format(ctx.message.author.name), value="**{}**".format(phrase), inline=False)
        embed3.set_thumbnail(url=ctx.message.author.avatar_url)
        await bot.say(embed=embed3)

    except Exception as e:

        embed3 = discord.Embed(title="ERROR", description=" \n ", color=0xff0000)
        embed3.add_field(name="Falha ao executar.".format(ctx.message.author.name),
                        value="Se acontecer esse erro 3#0001\nA frase causadora do foi  `\"{}\"`".format(
                            phrase), inline=False)
        await bot.say(embed=embed3)

	
#GERA CONVITE
@bot.command(pass_context=True)
async def convite(ctx):
	invite = await bot.create_invite(ctx.message.channel,max_uses=1,xkcd=True)
	await bot.send_message(ctx.message.author,"Seu convite é {}".format(invite.url))
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
    song = ['https://www.youtube.com/watch?v=uukforYWCkk', 'https://www.youtube.com/watch?v=3_29xfehVgY','https://www.youtube.com/watch?v=RH_vE8eWWEs']
    choice  = random.choice(song)
    await bot.say('{}, Aqui está sua musica aleátoria.\n'.format(ctx.message.author.name) + choice)



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


#ENVIA UM GATINHO EM GIF
@bot.command()
async def cat():
    await bot.say("https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif")

#ENVI O GITHUB 
@bot.command()
async def github():
	await bot.say('https://github.com/vagner2k18/pythozinho')


#EXIBE OS COMANDOS DO BOT
bot.remove_command('help')
@bot.command()
async def help():
    embedhelp = discord.Embed(title="Pythozinho --Prefixo = ? ", description="Olá eu fui criado em python, abaixo segue minha lista de comandos:", color=0xeee657)
    embedhelp.add_field(name="Sobre o bot ", value="?github,?botinfo", inline=False)
    embedhelp.add_field(name="Moderação", value="?kick", inline=False)
    embedhelp.add_field(name="Diversao", value="?cat,?ping,?music,?dado,?moeda,?eco", inline=False)
    embedhelp.add_field(name="Gerar convite do serve", value="?convite", inline=False)
    embedhelp.add_field(name="Ultilidades", value="?myinfo,?delete", inline=False)
    await bot.say(embed=embedhelp)






'''TOKEN PARA RODAR BOT'''
bot.run(token)

