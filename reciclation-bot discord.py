import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

lista_materiales = {
    "plastic": "Amarillo (plásticos)",
    "plastico": "Amarillo (plásticos)",
    "botella": "Amarillo (plásticos)",
    "paper": "Azul (papel)",
    "papel": "Azul (papel)",
    "periodico": "Azul (papel)",
    "cardboard": "Azul (cartón)",
    "carton": "Azul (cartón)",
    "glass": "Verde (vidrio)",
    "vidrio": "Verde (vidrio)",
    "metal": "Amarillo (metales)",
    "lata": "Amarillo (metales)",
    "banana": "Basurero de residuos orgánicos",
    "comida": "Basurero de residuos orgánicos",
    "cascara": "Basurero de residuos orgánicos",
    "battery": "Punto especial de recolección",
    "bateria": "Punto especial de recolección",
    "diaper": "Basurero de residuos no reciclables",
    "pañal": "Basurero de residuos no reciclables"
}

@bot.event
async def on_ready():
    print("Bot conectado como", bot.user)

@bot.command()
async def materials(ctx):
    choices = random.sample(list(lista_materiales.keys()), 3)

    await ctx.send("♻️ **¡Aquí tienes 3 materiales!**")

    for material in choices:
        await ctx.send("• " + material)

@bot.command()
async def where(ctx, *, material):
    material = material.lower()

    if material in lista_materiales:
        await ctx.send("♻️ " + material + " va en: " + lista_materiales[material])
    else:
        await ctx.send("No conozco ese material todavía. ♻️")

@bot.command()
async def ayuda(ctx):
    await ctx.send("Comandos: $materials y $where + material")

bot.run("")

