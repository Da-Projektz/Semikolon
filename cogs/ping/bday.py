from nextcord.ext import commands

class Ping(commands.Cog, name="Bday"):
    def __init__(self, bot: commands.Bot):
        self._bot = bot

