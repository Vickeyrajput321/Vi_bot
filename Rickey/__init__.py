from telethon import TelegramClient
import logging
import time 


openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6214863817:AAFel4BVolcED7-FInESOpRBOeZlDkTF1LM"
bot = TelegramClient("Rickey",api_id,api_hash).start(bot_token = bot_token)
    
if __name__ == "__main__":
  
    print(tgbot)