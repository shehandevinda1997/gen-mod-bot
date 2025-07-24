# https://t.me/Ultroid_Official/524



import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON , CHANNEL
from helper_func import *
from plugins.start import *
#from plugins.cmd import *

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start', 'users','addshort','resetshort','seeshort', 'getpremiumusers' , 'broadcast', 'batch', 'genlink', 'upi', 'myplan', 'plans', 'stats', 'removepr', 'addpr']))
#@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please wait...", quote=True)
    
    try:
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went wrong!")
        return

    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    vipstring = f"vip-{converted_id}"
    
    # Encode both normal and premium strings
    base64_string = await encode(string)
    vipbase64_string = await encode_premium(vipstring)
    
    # Generate normal and premium links
    normal_link = f"https://t.me/{client.username}?start={base64_string}"
    premium_link = f"https://t.me/{client.username}?start={vipbase64_string}"
    # website_link = f"https://phdlust.co/phdlust?{base64_string}"
    
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔁 Public", url=f'https://t.me/share/url?url={normal_link}'),
          InlineKeyboardButton("🔁 Premium", url=f'https://t.me/share/url?url={premium_link}')]]
    )

    await reply_text.edit(
        f"<b>Here are your links:</b>\n\n🤦‍♂️ Normal: {normal_link} \n\n✨ Premium: {premium_link}\n\nJoin @{CHANNEL}", 
        disable_web_page_preview=True
    )





@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass






# https://t.me/Ultroid_Official/524
