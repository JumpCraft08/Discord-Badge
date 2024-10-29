import os
from discord import app_commands, Intents, Client, Interaction
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

my_secret = os.getenv('TOKEN')

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)

bot = Bot(intents=Intents.default())

@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")

@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

if my_secret:  # Asegúrate de que el token esté definido
    bot.run(my_secret)
else:
    print("Error: El token no está definido en las variables de entorno.")


