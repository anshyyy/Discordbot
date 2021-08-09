import discord
from discord.ext import commands

from music import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
   print(f"{bot.user.name} is ready.")

async def setup():
   await bot.wait_until_ready()
   bot.add_cog(Player(bot))
  
bot.loop.create_task(setup())
bot.run("ODc0MjA5ODMxMzU4MTkzNzA0.YRDpWQ.gVIeFiHQflxHhzqjFWRtTuO16LQ")