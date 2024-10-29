import os
from discord import app_commands, Intents, Client, Interaction
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener el token del bot desde las variables de entorno
my_secret = os.getenv('TOKEN')

# Definición de la clase principal del bot
class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)

# Crear una instancia del bot con intents predeterminados
bot = Bot(intents=Intents.default())

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")

# Definición del comando slash 'givemebadge'
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

# Verificar si el token está definido y ejecutar el bot
if my_secret:
    bot.run(my_secret) 
else:
    print("Error: El token no está definido en las variables de entorno.")
