from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 49  inr

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 99  inr

**💎 Pro**
Daily Upload limit 100GB
Price Rs 179  inr

Payment Details :-
<b>➜ UPI ID :</b> <code>Narutoprit@fam/<code>

After Payment Send Screenshots Of Payment To Admin @Suh0_kang"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/Suh0_kang"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 49  inr

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 99  inr 

**💎 Pro**
Daily Upload limit 100GB
Price Rs 179  inr

Payment Details :-
<b>➜ UPI ID :</b> <code>narutoprit@fam/<code>
After Payment Send Screenshots Of Payment To Admin @Suh0_kang"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/Suh0_kang"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
    
	
    
    
    
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper & @MadflixOfficials
