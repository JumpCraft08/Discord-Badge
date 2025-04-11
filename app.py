import os, sys, subprocess, time, locale

# Obtener idioma del ordenador
try:
    locale.setlocale(locale.LC_ALL, '')
    language = locale.getlocale()[0]
    IDIOMA = "es" if language and language.startswith("es") else "fr" if language and language.startswith("fr") else "en"
except Exception as e:
    print(f"Error getting the system language: {e}. Using English by default")
    IDIOMA = "en"

# Diccionario de mensajes en español e inglés
lan = {
    "es": {
        "input_library": "La librería 'discord.py' no está instalada. ¿Deseas instalarla? (y/n): ",
        "downloading_library": "Descargando Discord.py. Espere unos segundos...",
        "download_cancelled": "Instalación cancelada. Cerrando...",
        "input_TOKEN": "Introduce el TOKEN: ",
        "badge": "¡Listo! Espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer",
        "bot_ready": "Conectado como: {user}"
    },
    "en": {
        "input_library": "The 'discord.py' library is not installed. Do you want to install it? (y/n): ",
        "downloading_library": "Downloading Discord.py. Please wait a few seconds...",
        "download_cancelled": "Installation cancelled. Closing...",
        "input_TOKEN": "Enter the TOKEN: ",
        "badge": "Done! Wait 24 hours to claim your badge\nYou can claim it here: https://discord.com/developers/active-developer",
        "bot_ready": "Connected as: {user}"
    },
    "fr": {
        "input_library": "La bibliothèque 'discord.py' n'est pas installée. Voulez-vous l'installer ? (y/n) : ",
        "downloading_library": "Téléchargement de Discord.py. Veuillez patienter quelques secondes...",
        "download_cancelled": "Installation annulée. Fermeture...",
        "input_TOKEN": "Entrez le TOKEN : ",
        "badge": "C'est fait ! Attendez 24 heures pour réclamer votre badge\nVous pouvez le réclamer ici : https://discord.com/developers/active-developer",
        "bot_ready": "Connecté en tant que : {user}"
    }
}

# Verificar si la librería está instalada, y si no, instalarla
try:
    from discord import app_commands, Intents, Client, Interaction
except ImportError:
    if input(lan[IDIOMA]["input_library"]).strip().lower() == "y":
        print(lan[IDIOMA]["downloading_library"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        from discord import app_commands, Intents, Client, Interaction
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(lan[IDIOMA]["download_cancelled"])
        time.sleep(2)
        sys.exit(1)

# Obtener el token del bot desde las variables de entorno
my_secret = "" or input(lan[IDIOMA]["input_TOKEN"])

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
    print(lan[IDIOMA]["bot_ready"].format(user=bot.user))

# Definición del comando slash 'givemebadge'
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message(lan[IDIOMA]["badge"])

# Verificar si el token está definido y ejecutar el bot
bot.run(my_secret)