from SJM.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""Salam [✨](https://telegra.ph/file/ea8d4bee1c0fac3814e11.jpg) **xoş gəldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
 **Qruplarda video zengli oxuda bilərsiz !!**
 **Sadəcə meni qrupa əlavə et və yetki ver 💫**
 **Hər hansı yardım üçün @king_sohbet_33 qoşulun**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Məni qrupa əlavə et",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "• Əmrlər", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("• Sahib", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("• Tərtibatçı ", url=f"https://t.me/nihat_33"),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "• Sᴏᴜʀᴄᴇ Cᴏᴅᴇ •", url="https://github.com/nihat870/TrickyMusic"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam !**
» **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴs 🔭 !**
⚡ Powered by [N İ H A T](https://t.me/Nihat_33)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅ", callback_data="cb_basic"),
                    InlineKeyboardButton("sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ᴄᴏᴍᴍᴀɴᴅs", callback_data="cb_advance"),
                ],
                [InlineKeyboardButton("sᴏᴍᴇ ғᴜɴ ᴄᴏᴍᴍᴀɴᴅ", callback_data="cb_fun")],
               
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f""" SADƏ ƏMRLƏR 
        
        
•  `/play (mahnı adı)` 
•  `/vplay (mahnı adı)` 
•  `/vstream (mahnı adı)` 
•  `/skip` - mahnını ötürün
•  `/end` - mahnını dayandır 
•  `/pause` - mahnını müvəqqəti dayandır
•  `/resume` - mahnını dawam etdirir
•  `/mute` - vc-də səssiz köməkçi
•  `/lyrics - (mahnı adı`

⚡ Powered By [N İ H A T](https://t.me/Nihat_33) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f""" ƏLAVƏ ƏMRLƏR 
• `/ping` pong !!
• `/start` - Alive msg ~group 
• `/id` - Find out your grp and your id // stickers id also
• `/uptime` - 💻
• `/rmd` clean all downloads
• `/clean` - clear storage 

⚡ Powered By [N İ H A T](https://t.me/Nihat_33) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_fun"))
async def cb_fun(_, query: CallbackQuery):
    await query.edit_message_text(  
        f""" ƏYLƏNCƏLİ ƏMRLƏR 
• `/truth` 🌝
• `/dare`  🌝
• `/sjm`    🌝
• `/abhi`   🌝
• `/tricky` 🌝   

⚡ Powered By [N İ H A T](https://t.me/nihat_33) .""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cb_cmd")]]
        ),
    )
        

    
    
    
        


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ɴɪᴋᴀʟ ʙsᴅᴋ ᴛᴜ ᴀᴅᴍɪɴ ɴᴀʜɪ ʜᴀɪ ɢʀᴘ ᴋᴀ !", show_alert=True)
    await query.message.delete()
