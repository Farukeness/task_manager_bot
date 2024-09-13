import discord
from discord.ext import commands
from commands import setup_commands
from database import create_table
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} olarak giriş yaptı!")
    await create_table()
    


setup_commands(bot)


bot.run("TOKEN")
