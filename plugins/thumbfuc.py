from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("π __**ππΎπ π³πΎπ½π π·π°ππ΄ π°π½π ππ·ππΌπ±π½π°πΈπ»**__") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("βοΈ __**ππΎππ ππ·ππΌπ±π½π°πΈπ» πππ²π²π΄πππ΅ππ»π»π π³π΄π»π΄ππ΄π³**__")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("βοΈ __**ππΎππ ππ·ππΌπ±π½π°πΈπ» πππ²π²π΄ππππ΅ππ»π»π ππ°ππ΄π³**__")
	
