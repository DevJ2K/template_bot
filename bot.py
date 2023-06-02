###############################MODULES###############################
import nextcord
import json
from nextcord.ext import commands
from nextcord.ext import commands
from nextcord.utils import get
from nextcord import ButtonStyle, SelectOption
from nextcord.ui import Button, View, Modal, Select
import platform
import os
if platform.system() == "Windows":
    from dotenv import load_dotenv
    load_dotenv(dotenv_path="config")



###############################INTENTS###############################
intents = nextcord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.bans = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)



###########################IMPORTS CHANNELS##########################
with open("all_channels.json") as f:
    all_channels = json.load(f)



##############################CODE HERE##############################
@bot.event
async def on_ready():
    print(f"{bot.user} est prêt !")







###############################RUN BOT###############################
if platform.system() == "Windows":
    bot.run(os.getenv("TOKEN"))
elif platform.system() == "Darwin":
    token = ""
    with open("config", "r") as file:
        for line in file:
            if line.startswith(f"TOKEN="):
                token = line.strip().split('=')[1]
    bot.run(token)