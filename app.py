import os
import time

try:
    from discord import app_commands, Intents, Client, Interaction
except ImportError:
    print("Error: No se pudo importar la librería 'discord.py'.")
    time.sleep(5)   
    exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: No se pudo importar la librería 'python-dotenv'.")
    time.sleep(5)
    exit(1)

# Cargar variables de entorno desde el archivo .env
if not os.path.exists('.env'):
    with open('.env', 'w') as f:
        f.write("TOKEN=\n")
    print("Archivo .env creado, por favor ingrese el token del bot.")    

load_dotenv()

# Obtener el token del bot desde las variables de entorno
my_secret = os.getenv('TOKEN')

# Si el token no está definido, solicitarlo al usuario
if not my_secret:
    my_secret = input("Por favor, ingrese el token del bot: ")
    with open('.env', 'a') as f:
        f.write(f'TOKEN={my_secret}\n')
     
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

# Ejecutar el bot con el token
bot.run(my_secret) 