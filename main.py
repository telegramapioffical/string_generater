#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

print("an online StringSession generator")

print("p ==> Pyrogram (docs.pyrogram.org)")
print("PyroGramUserBot ==> https://GitHub.com/SpEcHiDe/PyroGramUserBot")

print("t ==> Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://GitHub.com/SpEcHiDe/UniBorg")

print("Select your required option: ")
s_l = input("enter p / t ? ?? ")

if s_l == "p":
  print("you selected Pyrogram")
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  import pyrogram
  with pyrogram.Client(
    ":memory:",
    api_id=APP_ID,
    api_hash=API_HASH
  ) as app:
    session_str = app.export_session_string()
    s_m = app.send_message("me", session_str)
    s_m.reply_text("⬆️ This StringSession is generated using https://GenerateStringSession.SpEcHIDe.repl.run \nPlease subscribe @UniBorg ", quote=True)
    print("please check your Telegram Saved Messages for the StringSession ")

elif s_l == "t":
  print("you selected Telethon")
  # (c) https://t.me/TelethonChat/37677
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("Enter APP ID here: "))
  API_HASH = input("Enter API HASH here: ")
  with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  ) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️ This StringSession is generated using https://GenerateStringSession.SpEcHIDe.repl.run! \nPlease subscribe @UniBorg ")
    print("please check your Telegram Saved Messages for the StringSession ")

else:
  print("?? please select only p / t, ")
