import os
import discord
from discord.ext import commands
from main import evaluar_objeto

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def reciclar(ctx: commands.Context, *, objeto: str):
    """Evalúa si un objeto es reciclable."""
    try:
        resultado = evaluar_objeto(objeto)
        await ctx.send(resultado)
    except Exception as e:
        await ctx.send("Ocurrió un error al evaluar el objeto.")
        print(f"Error: {e}")

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("Por favor, define la variable de entorno DISCORD_TOKEN.")
    else:
        bot.run(token)
