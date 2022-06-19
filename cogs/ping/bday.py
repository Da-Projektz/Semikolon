from nextcord.ext import commands

class Bday(commands.Cog, name="bday"):
    def __init__(self, bot: commands.Bot):
        self._bot = bot
    
    #Someone says happy birthday?
    @commands.Cog.listener()
    async def on_message(message):
        if message.contains == "birthday":
            await message.channel.send('¡you old hag!')

def setup(bot: commands.Bot):
    bot.add_cog(Bday(bot))