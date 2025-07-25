# https://t.me/ultroid_official

import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6340284890:AAGj-EHyR0lHNFvWKV75VpYJPiACikFeMfU")
APP_ID = int(os.environ.get("APP_ID", "9111115"))
API_HASH = os.environ.get("API_HASH", "2a5342b0ef40f0a19d69852e076ff34b")
 
BAN = int(os.environ.get("BAN", "1865273490")) #Owner user id - dont chnge 
OWNER = os.environ.get("OWNER", "lucix_y_z") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1865273492")) #Owner user id
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', 'luciferx_y_z')
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "luciferx_y_z") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "@Jelly_Apps") # WITHOUR @

#pic
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/YvH.jpg")
START_PIC = os.environ.get("START_PIC", "https://envs.sh/Yv9.jpg")
TOKEN_PIC = os.environ.get("TOKEN_PIC", "https://envs.sh/y28.jpg")
PRM_PIC = os.environ.get("PRM_PIC", "https://envs.sh/FLU.jpg")

#auto delete
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", '2400')) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 30)) #seconds
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
GET_AGAIN = os.environ.get("GET_AGAIN", False) #ON/OFF
DELETE_INFORM = os.environ.get("INFORM" , "Successfully DELETED !!")
NOTIFICATION = os.environ.get("NOTIFICATION" ,"File will delete after 40 minutes.")
GET_INFORM = os.environ.get("GET_INFORM" ,"File was deleted after {DELETE_AFTER} seconds. Use the button below to GET FILE AGAIN.")


#Premium varibles
PAYMENT_QR = os.getenv('PAYMENT_QR', 'https://envs.sh/YfJ.jpg')
PAYMENT_TEXT = os.getenv('PAYMENT_TEXT', '<b>💢 Aᴠᴀɪʟᴀʙʟᴇ Pʟᴀɴs ‼️ \n\n'
                                      '➤ 20ʀs - 1 Wᴇᴇᴋ\n➤ 30ʀs - 15 Dᴀʏꜱ\n'
                                      '➤ 50ʀs - 1 Mᴏɴᴛʜ\n➤For Custom Plan Dm Below\n\n'
                                      '🎁 Pʀᴇᴍɪᴜᴍ Fᴇᴀᴛᴜʀᴇs 🎁\n\n'
                                      '○ Nᴏ Nᴇᴇᴅ Tᴏ ᴠᴇʀɪғʏ\n○ Nᴏ Nᴇᴇᴅ Tᴏ Oᴘᴇɴ Lɪɴᴋ\n'
                                      '○ Dɪʀᴇᴄᴛ Fɪʟᴇs\n○ Aᴅ-Fʀᴇᴇ Exᴘᴇʀɪᴇɴᴄᴇ\n'
                                      '○ Uɴʟɪᴍɪᴛᴇᴅ Aᴘᴘꜱ & Gᴀᴍᴇꜱ\n○ Fᴜʟʟ Aᴅᴍɪɴ Sᴜᴘᴘᴏʀᴛ\n\n'
                                      '✨ Uᴘɪ Iᴅ - <code>lucihere@apl</code>\n\n'
                                      'Cʟɪᴄᴋ Tᴏ Cʜᴇᴄᴋ Yᴏᴜʀ Aᴄᴛɪᴠᴇ Pʟᴀɴ /myplan\n\n'
                                      '💢 Mᴜsᴛ Sᴇɴᴅ Sᴄʀᴇᴇɴsʜᴏᴛ Aғᴛᴇʀ Pᴀʏᴍᴇɴᴛ\n\n'
                                      '‼️ Aғᴛᴇʀ Sᴇɴᴅɪɴɢ Sᴄʀᴇᴇɴsʜᴏᴛ Pʟᴇᴀsᴇ Gɪᴠᴇ Us Sᴏᴍᴇ Tɪᴍᴇ Tᴏ Aᴅᴅ Yᴏᴜ Iɴ Tʜᴇ Pʀᴇᴍɪᴜᴍ</b>')

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://luce36757:blQuzamKEQgEblAo@cluster0.a23ia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")
DB_DELETE = os.environ.get("DB_DELETE", "del11")
DB_SHORT = os.environ.get("DB_SHORT", "short11")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002359030584")) #database save channel id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001715975124"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002592025046"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

#Shortner (token system) 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "easysky.in") 
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8700018bffc724d4b39f7be1d60d680fbc2ab718")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 14)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "t.me/How2_openLink/21")




SHORTCAP = os.environ.get("SHORTCAP", "<b>Yᴏᴜʀ Aᴄᴄᴇꜱꜱ Tᴏᴋᴇɴ Iꜱ Exᴘɪʀᴇᴅ !!\nGᴇɴᴇʀᴀᴛᴇ Nᴇᴡ Tᴏᴋᴇɴ Fʀᴏᴍ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Fᴏʀ Fʀᴇᴇ\n\n~ Tᴏᴋᴇɴ Tɪᴍᴇᴏᴜᴛ: 24 Hrs\n\nWᴀᴛᴄʜ Tᴜᴛᴏʀɪᴀʟ Iꜰ Yᴏᴜ Aʀᴇ Fᴀᴄɪɴɢ Tʜᴇ Iꜱꜱᴜᴇ Yᴏᴜ Cᴀɴ Aʟꜱᴏ Sᴜʙꜱᴄʀɪʙᴇ Pʀᴇᴍɪᴜᴍ Tᴏ Aᴠᴏɪᴅ Dᴀɪʟʏ Tᴏᴋᴇɴ Gᴇɴᴇʀᴀᴛɪᴏɴ</b>") #token caption

# ignore this one
SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ 🙋,{first}\n\nI Aᴍ A Aᴘᴋ Sᴛᴏʀᴇ Bᴏᴛ Cʜᴇᴄᴋᴏᴜᴛ Oᴜʀ Cʜᴀɴɴᴇʟꜱ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇ Tʜʀᴏᴜɢʜ Mᴇ\n\n~ Bᴏᴛ Bʏ @Jelly_Apps")

try:
    ADMINS=[1865273492]
    for x in (os.environ.get("ADMINS", "1865273492").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>🙋‍♂ Hᴇʟʟᴏ,{first}</b>\n➖➖➖➖➖➖➖➖➖➖➖\n<b>🔎 Yᴏᴜ Mᴜsᴛ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Oᴜʀ Cʜᴀɴɴᴇʟs  Bʏ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs Iɴ Oʀᴅᴇʀ Tᴏ Usᴇ Mᴇ !!!</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "~ Join @Jelly_Apps") # remove None and fo this ->: "here come your txt" also with this " " 

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", False) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(1865273492)

LOG_FILE_NAME = "uxblogs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# https://t.me/ultroid_official
