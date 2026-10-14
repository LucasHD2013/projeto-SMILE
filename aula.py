from pathlib import Path
import discord
from discord.ext import commands
from bot_logic import gen_pass, D20
from duck import get_duck_image_url
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    image_dir = Path(__file__).parent / "images"
    files = [
        discord.File(image_dir / image)
        for image in ("meme.png", "dinosseuro_programador.png", "sintax_switch.png")
    ]
    await ctx.send(files=files)

@bot.command(name="duck")
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.group()
async def caralegal(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'não, {ctx.subcommand_passed} não é legal')


@caralegal.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('sim o bot é legal.')

@caralegal.command(name='gojo')
async def _gojo(ctx):
    """Is Gojo cool?"""
    await ctx.send('insira o nome de alguém e não o nome de um kitkat.')

@caralegal.command(name='lucas')
async def _lucas(ctx):
    """Is Lucas cool?"""
    await ctx.send('sim,lucas é legal')

bot.run("não")
