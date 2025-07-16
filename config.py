# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "19822764"))
API_HASH = getenv("API_HASH", "b240e413364b8608a542a7cafc6903be")
BOT_TOKEN = getenv("BOT_TOKEN", "8061755858:AAEjt1axJXPpVGLCjzzFYZaWZhynPGKNF9w")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1418213560").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority&appName=sanjisama")
LOG_GROUP = getenv("LOG_GROUP", "-1002710230763")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002302871218"))
