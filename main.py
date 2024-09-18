import discord
import random
import os
from discord.ext import commands
from bot_logic import  gen_pass
from bot_logic import gene_emodji
from bot_logic import get_duck_image_url
from bot_logic import get_dog_image_url
from bot_logic import get_weather_info_url
from bot_logic import get_random_meme
from bot_logic import info_list

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable bot y transferirle los privilegios
bot = commands.Bot(command_prefix= "$", intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

#Saludar
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi!")

#Despedirse
@bot.command()
async def bye(ctx):
    await ctx.send("😞")

#Generador de contraseñas
@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

#Enviar un meme (imagen)
@bot.command()
async def meme(ctx):
    with open("C:/Users/Jose Antonio/OneDrive/Escritorio/Python Proyects/3713/M1L3/images/mem1.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

#Enviar un meme aleatorio (imagen)
@bot.command()
async def meme_aleatorio(ctx):
    mem_alet = random.choice(os.listdir("C:/Users/Jose Antonio/OneDrive/Escritorio/Python Proyects/3713/M1L3/images"))

    with open(f"C:/Users/Jose Antonio/OneDrive/Escritorio/Python Proyects/3713/M1L3/images/{mem_alet}", "rb") as f:
        picture = discord.File(f)
    await ctx.send (file=picture)

#Enviar un emoji aleatorio
@bot.command()
async def gen_emodji(ctx):
    await ctx.send(gene_emodji())

#Enviar una imagen api de patos
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#Enviar una imagen api de perros
@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

#Enviar una info del tiempo
@bot.command('weather')
async def weather(ctx):
    info = get_weather_info_url()
    await ctx.send(info)
    
#Enviar una foto random de un meme
@bot.command("memeapi")
async def random_meme(ctx):
    meme = get_random_meme()
    await ctx.send(meme['url'])

@bot.command()
async def comandos(ctx):
    commands_list = info_list()
    await ctx.send(f"Lista de comandos:\n{commands_list}")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("")
